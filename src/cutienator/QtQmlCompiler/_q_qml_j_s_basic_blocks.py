"""
QQmlJSBasicBlocks binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsbasicblocks_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSBasicBlocks to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQml import QV4
from . import QQmlJSAotCompiler, QQmlJSCompilePass

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlJSLogger, QQmlJSTypeResolver
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSLogger = WAIT['QQmlJSLogger']
  QQmlJSTypeResolver = WAIT['QQmlJSTypeResolver']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSBasicBlocks(QQmlJSCompilePass):
  """
  The cute side of Qt's QQmlJSBasicBlocks: a plain Python object standing in
  front of one C++ QQmlJSBasicBlocks.

  It is built on the cute 'QQmlJSCompilePass', as Qt's QQmlJSBasicBlocks is
  built on Qt's QQmlJSCompilePass, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlJSBasicBlocks that has a ritual and that Python
  can call so far, 16 names in all: 'basicBlocksValidation',
  'endInstruction', 'generate_Jump', 'generate_JumpTrue',
  'generate_JumpFalse', 'generate_JumpNoException',
  'generate_JumpNotUndefined', 'generate_IteratorNext',
  'generate_GetOptionalLookup', 'generate_Ret', 'generate_ThrowException',
  'generate_DefineArray', 'generate_DefineObjectLiteral',
  'generate_Construct', 'dumpBasicBlocks', 'dumpDOTGraph'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSBasicBlocks::~QQmlJSBasicBlocks()': the destructor: Python
    never removes a C++ QQmlJSBasicBlocks.
  - Qt's 'QQmlJSCompilePass::BlocksAndAnnotations
    QQmlJSBasicBlocks::run(const Function *function, QQmlJSAotCompiler::Flags
    compileFlags, bool &basicBlocksValidationFailed)': takes a number to
    change where it is.
  - Qt's 'QList<ObjectOrArrayDefinition>
    QQmlJSBasicBlocks::objectAndArrayDefinitions() const': gives a type
    Python has no way to take yet.
  - Qt's 'QV4::Moth::ByteCodeHandler::Verdict
    QQmlJSBasicBlocks::startInstruction(QV4::Moth::Instr::Type type)': gives
    the enum 'QV4::Moth::ByteCodeHandler::Verdict', whose class cannot be
    named here.
  - Qt's 'void QQmlJSBasicBlocks::processJump(int offset, JumpMode mode)':
    names the enum 'QQmlJSBasicBlocks::JumpMode', whose class cannot be named
    here.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here; 1 a template.

  What to expect
  --------------

  - The C++ QQmlJSBasicBlocks is created at the first use, not by
    'QQmlJSBasicBlocks(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSBasicBlocks.
  - Each name of Qt's QQmlJSBasicBlocks that has no cute function yet,
    'basicBlockForInstruction', 'constBasicBlockForInstruction',
    'findBasicBlockForInstruction', 'objectAndArrayDefinitions',
    'processJump', 'run', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QQmlJSBasicBlocks, each a class in here as
  #  in C++.

  class BasicBlocksValidationResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSBasicBlocks::BasicBlocksValidationResult: a
    plain Python object standing in front of one C++
    QQmlJSBasicBlocks::BasicBlocksValidationResult.

    C++ hands a QQmlJSBasicBlocks::BasicBlocksValidationResult around as a
    copy, so every C++ QQmlJSBasicBlocks::BasicBlocksValidationResult behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlJSBasicBlocks::BasicBlocksValidationResult yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSBasicBlocks::BasicBlocksValidationResult::
      ~BasicBlocksValidationResult()': the destructor: Python removes its C++
      QQmlJSBasicBlocks::BasicBlocksValidationResult by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QQmlJSBasicBlocks::BasicBlocksValidationResult is created at
      the first use, not by
      'QQmlJSBasicBlocks::BasicBlocksValidationResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSBasicBlocks::BasicBlocksValidationResult back
      gives a copy the ritual made for Python, in a new cute
      QQmlJSBasicBlocks::BasicBlocksValidationResult.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSBasicBlocks::BasicBlocksValidationResult'

    #  Qt's '~QQmlJSBasicBlocks::BasicBlocksValidationResult()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QQmlJSBasicBlocks::BasicBlocksValidationResult behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN17QQmlJSBasicBlocks27BasicBlocksValidationResultD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSBasicBlocks'

  #  A C++ QQmlJSBasicBlocks Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJSBasicBlocks'

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

  @overload(
      WAIT['QV4.Compiler.Context'], WAIT['QV4.Compiler.JSUnitGenerator'],
      QQmlJSTypeResolver, QQmlJSLogger,
  )
  @overload(
      WAIT['QV4.Compiler.Context'], WAIT['QV4.Compiler.JSUnitGenerator'],
      QQmlJSTypeResolver, NoneType,
  )
  @overload(
      WAIT['QV4.Compiler.Context'], WAIT['QV4.Compiler.JSUnitGenerator'],
      NoneType, QQmlJSLogger,
  )
  @overload(
      WAIT['QV4.Compiler.Context'], WAIT['QV4.Compiler.JSUnitGenerator'],
      NoneType, NoneType,
  )
  @overload(
      WAIT['QV4.Compiler.Context'], NoneType, QQmlJSTypeResolver,
      QQmlJSLogger,
  )
  @overload(
      WAIT['QV4.Compiler.Context'], NoneType, QQmlJSTypeResolver, NoneType,
  )
  @overload(WAIT['QV4.Compiler.Context'], NoneType, NoneType, QQmlJSLogger)
  @overload(WAIT['QV4.Compiler.Context'], NoneType, NoneType, NoneType)
  @overload(
      NoneType, WAIT['QV4.Compiler.JSUnitGenerator'], QQmlJSTypeResolver,
      QQmlJSLogger,
  )
  @overload(
      NoneType, WAIT['QV4.Compiler.JSUnitGenerator'], QQmlJSTypeResolver,
      NoneType,
  )
  @overload(
      NoneType, WAIT['QV4.Compiler.JSUnitGenerator'], NoneType, QQmlJSLogger,
  )
  @overload(
      NoneType, WAIT['QV4.Compiler.JSUnitGenerator'], NoneType, NoneType,
  )
  @overload(NoneType, NoneType, QQmlJSTypeResolver, QQmlJSLogger)
  @overload(NoneType, NoneType, QQmlJSTypeResolver, NoneType)
  @overload(NoneType, NoneType, NoneType, QQmlJSLogger)
  @overload(NoneType, NoneType, NoneType, NoneType)
  def __init__(
      self,
      context: Optional[QV4.Compiler.Context],
      unitGenerator: Optional[QV4.Compiler.JSUnitGenerator],
      typeResolver: Optional[QQmlJSTypeResolver],
      logger: Optional[QQmlJSLogger],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSBasicBlocks::QQmlJSBasicBlocks(const QV4::Compiler::Context
    *context, const QV4::Compiler::JSUnitGenerator *unitGenerator, const
    QQmlJSTypeResolver *typeResolver, QQmlJSLogger *logger)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#QQmlJSBasicBlocks

    Parameters
    ----------

    context : Optional[QV4.Compiler.Context]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    unitGenerator : Optional[QV4.Compiler.JSUnitGenerator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeResolver : Optional[QQmlJSTypeResolver]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    logger : Optional[QQmlJSLogger]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJSBasicBlocks::QQmlJSBasicBlocks(const QV4::Compiler::Context
    #      *context, const QV4::Compiler::JSUnitGenerator *unitGenerator,
    #      const QQmlJSTypeResolver *typeResolver, QQmlJSLogger *logger)
    self._noteCreation(QQmlJSBasicBlocks, lambda: Rituals.call(
        'ritual_ZN17QQmlJSBasicBlocksC1EPKN3QV48Compiler7ContextEPKNS1_15JS'
        'UnitGeneratorEPK18QQmlJSTypeResolverP12QQmlJSLogger',
        self._addressOf(context), self._addressOf(unitGenerator),
        self._addressOf(typeResolver), self._addressOf(logger),
    ))

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

  def basicBlocksValidation(self) -> BasicBlocksValidationResult:
    """
    Calls Qt's 'BasicBlocksValidationResult
    QQmlJSBasicBlocks::basicBlocksValidation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#basicBlocksValidation

    Returns
    -------

    BasicBlocksValidationResult
      A new cute QQmlJSBasicBlocks::BasicBlocksValidationResult around the
      copy Qt gave back. Python owns it.
    """
    #  BasicBlocksValidationResult QQmlJSBasicBlocks::basicBlocksValidation()
    address = self.uglySide.call(
        'ritual_ZN17QQmlJSBasicBlocks21basicBlocksValidationEv',
    )
    return QQmlJSBasicBlocks.BasicBlocksValidationResult._cuteOwning(address)

  @overload(QV4.Moth.Instr.Type)
  def endInstruction(self, type: QV4.Moth.Instr.Type) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::endInstruction(QV4::Moth::Instr::Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#endInstruction

    Parameters
    ----------

    type : QV4.Moth.Instr.Type
      Passed on as its number.
    """
    #  void QQmlJSBasicBlocks::endInstruction(QV4::Moth::Instr::Type type)
    ritual = (
        'ritual_ZN17QQmlJSBasicBlocks14endInstructionEN3QV44Moth5Instr4Type'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSBasicBlocks14endInstructionEN3QV44Moth5Inst'
          'r4TypeE')
    self.uglySide.call(ritual, type.value)

  @overload(int)
  def generate_Jump(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::generate_Jump(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#generate_Jump

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSBasicBlocks::generate_Jump(int offset)
    ritual = 'ritual_ZN17QQmlJSBasicBlocks13generate_JumpEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSBasicBlocks13generate_JumpEi'
    self.uglySide.call(ritual, offset)

  @overload(int)
  def generate_JumpTrue(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::generate_JumpTrue(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#generate_JumpTrue

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSBasicBlocks::generate_JumpTrue(int offset)
    ritual = 'ritual_ZN17QQmlJSBasicBlocks17generate_JumpTrueEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSBasicBlocks17generate_JumpTrueEi'
    self.uglySide.call(ritual, offset)

  @overload(int)
  def generate_JumpFalse(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::generate_JumpFalse(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#generate_JumpFalse

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSBasicBlocks::generate_JumpFalse(int offset)
    ritual = 'ritual_ZN17QQmlJSBasicBlocks18generate_JumpFalseEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSBasicBlocks18generate_JumpFalseEi'
    self.uglySide.call(ritual, offset)

  @overload(int)
  def generate_JumpNoException(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::generate_JumpNoException(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#generate_JumpNoException

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSBasicBlocks::generate_JumpNoException(int offset)
    ritual = 'ritual_ZN17QQmlJSBasicBlocks24generate_JumpNoExceptionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSBasicBlocks24generate_JumpNoExceptionEi'
    self.uglySide.call(ritual, offset)

  @overload(int)
  def generate_JumpNotUndefined(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::generate_JumpNotUndefined(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#generate_JumpNotUndefined

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSBasicBlocks::generate_JumpNotUndefined(int offset)
    ritual = 'ritual_ZN17QQmlJSBasicBlocks25generate_JumpNotUndefinedEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSBasicBlocks25generate_JumpNotUndefinedEi')
    self.uglySide.call(ritual, offset)

  @overload(int, int)
  def generate_IteratorNext(self, value: int, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::generate_IteratorNext(int value, int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#generate_IteratorNext

    Parameters
    ----------

    value : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSBasicBlocks::generate_IteratorNext(int value, int offset)
    ritual = 'ritual_ZN17QQmlJSBasicBlocks21generate_IteratorNextEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSBasicBlocks21generate_IteratorNextEii'
    self.uglySide.call(ritual, value, offset)

  @overload(int, int)
  def generate_GetOptionalLookup(self, index: int, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::generate_GetOptionalLookup(int index,
    int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#generate_GetOptionalLookup

    Parameters
    ----------

    index : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSBasicBlocks::generate_GetOptionalLookup(int index, int
    #      offset)
    ritual = 'ritual_ZN17QQmlJSBasicBlocks26generate_GetOptionalLookupEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSBasicBlocks26generate_GetOptionalLookupEii')
    self.uglySide.call(ritual, index, offset)

  def generate_Ret(self) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::generate_Ret()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#generate_Ret
    """
    #  void QQmlJSBasicBlocks::generate_Ret()
    ritual = 'ritual_ZN17QQmlJSBasicBlocks12generate_RetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSBasicBlocks12generate_RetEv'
    self.uglySide.call(ritual)

  def generate_ThrowException(self) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::generate_ThrowException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#generate_ThrowException
    """
    #  void QQmlJSBasicBlocks::generate_ThrowException()
    ritual = 'ritual_ZN17QQmlJSBasicBlocks23generate_ThrowExceptionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSBasicBlocks23generate_ThrowExceptionEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_DefineArray(self, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::generate_DefineArray(int argc, int
    argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#generate_DefineArray

    Parameters
    ----------

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSBasicBlocks::generate_DefineArray(int argc, int argv)
    ritual = 'ritual_ZN17QQmlJSBasicBlocks20generate_DefineArrayEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSBasicBlocks20generate_DefineArrayEii'
    self.uglySide.call(ritual, argc, argv)

  @overload(int, int, int)
  def generate_DefineObjectLiteral(
      self,
      internalClassId: int,
      argc: int,
      args: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::generate_DefineObjectLiteral(int
    internalClassId, int argc, int args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html

    Parameters
    ----------

    internalClassId : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    args : int
      Passed on as it is.
    """
    #  void QQmlJSBasicBlocks::generate_DefineObjectLiteral(int
    #      internalClassId, int argc, int args)
    ritual = 'ritual_ZN17QQmlJSBasicBlocks28generate_DefineObjectLiteralEiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSBasicBlocks28generate_DefineObjectLiteralEi'
          'ii')
    self.uglySide.call(ritual, internalClassId, argc, args)

  @overload(int, int, int)
  def generate_Construct(self, func: int, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::generate_Construct(int func, int
    argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#generate_Construct

    Parameters
    ----------

    func : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSBasicBlocks::generate_Construct(int func, int argc, int
    #      argv)
    ritual = 'ritual_ZN17QQmlJSBasicBlocks18generate_ConstructEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSBasicBlocks18generate_ConstructEiii'
    self.uglySide.call(ritual, func, argc, argv)

  def dumpBasicBlocks(self) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::dumpBasicBlocks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#dumpBasicBlocks
    """
    #  void QQmlJSBasicBlocks::dumpBasicBlocks()
    self.uglySide.call('ritual_ZN17QQmlJSBasicBlocks15dumpBasicBlocksEv')

  def dumpDOTGraph(self) -> None:
    """
    Calls Qt's 'void QQmlJSBasicBlocks::dumpDOTGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsbasicblocks.html#dumpDOTGraph
    """
    #  void QQmlJSBasicBlocks::dumpDOTGraph()
    self.uglySide.call('ritual_ZN17QQmlJSBasicBlocks12dumpDOTGraphEv')

  @staticmethod
  def basicBlockForInstruction(*__, **_) -> Never:
    """
    Qt's 'BasicBlocks::iterator
    QQmlJSBasicBlocks::basicBlockForInstruction(BasicBlocks &blocks, int
    offset)': the compiler refuses its ritual as it would be written here:
    use of undeclared identifier 'BasicBlocks'; did you mean
    'CuteQQmlJSBasicBlocks::BasicBlocks'?.
    """
    raise NotImplementedError(
        "'QQmlJSBasicBlocks.basicBlockForInstruction' has no cute function "
        "yet. Qt's 'BasicBlocks::iterator "
        "QQmlJSBasicBlocks::basicBlockForInstruction(BasicBlocks &blocks, "
        "int offset)': the compiler refuses its ritual as it would be "
        "written here: use of undeclared identifier 'BasicBlocks'; did you "
        "mean 'CuteQQmlJSBasicBlocks::BasicBlocks'?.")

  @staticmethod
  def constBasicBlockForInstruction(*__, **_) -> Never:
    """
    Qt's 'BasicBlocks::const_iterator
    QQmlJSBasicBlocks::constBasicBlockForInstruction(const BasicBlocks
    &blocks, int offset)': the compiler refuses its ritual as it would be
    written here: use of undeclared identifier 'BasicBlocks'; did you mean
    'CuteQQmlJSBasicBlocks::BasicBlocks'?.
    """
    raise NotImplementedError(
        "'QQmlJSBasicBlocks.constBasicBlockForInstruction' has no cute "
        "function yet. Qt's 'BasicBlocks::const_iterator "
        "QQmlJSBasicBlocks::constBasicBlockForInstruction(const BasicBlocks "
        "&blocks, int offset)': the compiler refuses its ritual as it would "
        "be written here: use of undeclared identifier 'BasicBlocks'; did "
        "you mean 'CuteQQmlJSBasicBlocks::BasicBlocks'?.")

  @staticmethod
  def findBasicBlockForInstruction(*__, **_) -> Never:
    """
    Qt's 'QQmlJSBasicBlocks::findBasicBlockForInstruction': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlJSBasicBlocks.findBasicBlockForInstruction' has no cute "
        "function yet. Qt's "
        "'QQmlJSBasicBlocks::findBasicBlockForInstruction': a template: a "
        "pattern and no single function.")

  @staticmethod
  def objectAndArrayDefinitions(*__, **_) -> Never:
    """
    Qt's 'QList<ObjectOrArrayDefinition>
    QQmlJSBasicBlocks::objectAndArrayDefinitions() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSBasicBlocks.objectAndArrayDefinitions' has no cute function "
        "yet. Qt's 'QList<ObjectOrArrayDefinition> "
        "QQmlJSBasicBlocks::objectAndArrayDefinitions() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def processJump(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSBasicBlocks::processJump(int offset, JumpMode mode)':
    names the enum 'QQmlJSBasicBlocks::JumpMode', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QQmlJSBasicBlocks.processJump' has no cute function yet. Qt's "
        "'void QQmlJSBasicBlocks::processJump(int offset, JumpMode mode)': "
        "names the enum 'QQmlJSBasicBlocks::JumpMode', whose class cannot "
        "be named here.")

  @staticmethod
  def run(*__, **_) -> Never:
    """
    Qt's 'QQmlJSCompilePass::BlocksAndAnnotations
    QQmlJSBasicBlocks::run(const Function *function, QQmlJSAotCompiler::Flags
    compileFlags, bool &basicBlocksValidationFailed)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QQmlJSBasicBlocks.run' has no cute function yet. Qt's "
        "'QQmlJSCompilePass::BlocksAndAnnotations "
        "QQmlJSBasicBlocks::run(const Function *function, "
        "QQmlJSAotCompiler::Flags compileFlags, bool "
        "&basicBlocksValidationFailed)': takes a number to change where it "
        "is.")
