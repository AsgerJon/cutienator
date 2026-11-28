"""
QQmlJSShadowCheck binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsshadowcheck_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSShadowCheck to be private: it declares the class in a
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

  from . import QQmlJSRegisterContent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSRegisterContent = WAIT['QQmlJSRegisterContent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSShadowCheck(QQmlJSCompilePass):
  """
  The cute side of Qt's QQmlJSShadowCheck: a plain Python object standing in
  front of one C++ QQmlJSShadowCheck.

  It is built on the cute 'QQmlJSCompilePass', as Qt's QQmlJSShadowCheck is
  built on Qt's QQmlJSCompilePass, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlJSShadowCheck that has a ritual and that Python
  can call so far, 11 names in all: 'run', 'handleStore',
  'generate_LoadProperty', 'generate_GetLookup',
  'generate_GetOptionalLookup', 'generate_StoreProperty',
  'generate_SetLookup', 'generate_CallProperty',
  'generate_CallPropertyLookup', 'endInstruction', 'checkResettable'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSShadowCheck::QQmlJSShadowCheck(const
    QV4::Compiler::JSUnitGenerator *jsUnitGenerator, const QQmlJSTypeResolver
    *typeResolver, QQmlJSLogger *logger, const BasicBlocks &basicBlocks,
    const InstructionAnnotations &annotations)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QQmlJSShadowCheck::~QQmlJSShadowCheck()': the destructor: Python
    never removes a C++ QQmlJSShadowCheck.
  - Qt's 'QV4::Moth::ByteCodeHandler::Verdict
    QQmlJSShadowCheck::startInstruction(QV4::Moth::Instr::Type a0)': gives
    the enum 'QV4::Moth::ByteCodeHandler::Verdict', whose class cannot be
    named here.
  - Qt's 'Shadowability
    QQmlJSShadowCheck::checkShadowing(QQmlJSRegisterContent baseType, const
    QString &propertyName, int baseRegister)': gives the enum
    'QQmlJSShadowCheck::Shadowability', whose class cannot be named here.
  - Qt's 'Shadowability
    QQmlJSShadowCheck::checkBaseType(QQmlJSRegisterContent baseType)': gives
    the enum 'QQmlJSShadowCheck::Shadowability', whose class cannot be named
    here.

  What to expect
  --------------

  - The C++ QQmlJSShadowCheck is created at the first use, not by
    'QQmlJSShadowCheck(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSShadowCheck.
  - Each name of Qt's QQmlJSShadowCheck that has no cute function yet,
    '__init__', 'checkBaseType', 'checkShadowing', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSShadowCheck'

  #  A C++ QQmlJSShadowCheck Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJSShadowCheck'

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
    Qt's 'QQmlJSShadowCheck::QQmlJSShadowCheck(const
    QV4::Compiler::JSUnitGenerator *jsUnitGenerator, const QQmlJSTypeResolver
    *typeResolver, QQmlJSLogger *logger, const BasicBlocks &basicBlocks,
    const InstructionAnnotations &annotations)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSShadowCheck.__init__' has no cute function yet. Qt's "
        "'QQmlJSShadowCheck::QQmlJSShadowCheck(const "
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
    Calls Qt's 'BlocksAndAnnotations QQmlJSShadowCheck::run(const Function
    *function)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsshadowcheck.html#run

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
    #  BlocksAndAnnotations QQmlJSShadowCheck::run(const Function *function)
    address = self.uglySide.call(
        'ritual_ZN17QQmlJSShadowCheck3runEPKN17QQmlJSCompilePass8FunctionE',
        self._addressOf(function),
    )
    return QQmlJSCompilePass.BlocksAndAnnotations._cuteOwning(address)

  @overload(int, str)
  def handleStore(self, base: int, memberName: str) -> None:
    """
    Calls Qt's 'void QQmlJSShadowCheck::handleStore(int base, const QString
    &memberName)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsshadowcheck.html#handleStore

    Parameters
    ----------

    base : int
      Passed on as it is.

    memberName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSShadowCheck::handleStore(int base, const QString
    #      &memberName)
    self.uglySide.call(
        'ritual_ZN17QQmlJSShadowCheck11handleStoreEiRK7QString',
        base, memberName,
    )

  @overload(int)
  def generate_LoadProperty(self, nameIndex: int) -> None:
    """
    Calls Qt's 'void QQmlJSShadowCheck::generate_LoadProperty(int
    nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsshadowcheck.html#generate_LoadProperty

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.
    """
    #  void QQmlJSShadowCheck::generate_LoadProperty(int nameIndex)
    ritual = 'ritual_ZN17QQmlJSShadowCheck21generate_LoadPropertyEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSShadowCheck21generate_LoadPropertyEi'
    self.uglySide.call(ritual, nameIndex)

  @overload(int)
  def generate_GetLookup(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSShadowCheck::generate_GetLookup(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsshadowcheck.html#generate_GetLookup

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSShadowCheck::generate_GetLookup(int index)
    ritual = 'ritual_ZN17QQmlJSShadowCheck18generate_GetLookupEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSShadowCheck18generate_GetLookupEi'
    self.uglySide.call(ritual, index)

  @overload(int, int)
  def generate_GetOptionalLookup(self, index: int, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSShadowCheck::generate_GetOptionalLookup(int index,
    int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsshadowcheck.html#generate_GetOptionalLookup

    Parameters
    ----------

    index : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSShadowCheck::generate_GetOptionalLookup(int index, int
    #      offset)
    ritual = 'ritual_ZN17QQmlJSShadowCheck26generate_GetOptionalLookupEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSShadowCheck26generate_GetOptionalLookupEii')
    self.uglySide.call(ritual, index, offset)

  @overload(int, int)
  def generate_StoreProperty(self, nameIndex: int, base: int) -> None:
    """
    Calls Qt's 'void QQmlJSShadowCheck::generate_StoreProperty(int nameIndex,
    int base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsshadowcheck.html#generate_StoreProperty

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.

    base : int
      Passed on as it is.
    """
    #  void QQmlJSShadowCheck::generate_StoreProperty(int nameIndex, int
    #      base)
    ritual = 'ritual_ZN17QQmlJSShadowCheck22generate_StorePropertyEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSShadowCheck22generate_StorePropertyEii'
    self.uglySide.call(ritual, nameIndex, base)

  @overload(int, int)
  def generate_SetLookup(self, index: int, base: int) -> None:
    """
    Calls Qt's 'void QQmlJSShadowCheck::generate_SetLookup(int index, int
    base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsshadowcheck.html#generate_SetLookup

    Parameters
    ----------

    index : int
      Passed on as it is.

    base : int
      Passed on as it is.
    """
    #  void QQmlJSShadowCheck::generate_SetLookup(int index, int base)
    ritual = 'ritual_ZN17QQmlJSShadowCheck18generate_SetLookupEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSShadowCheck18generate_SetLookupEii'
    self.uglySide.call(ritual, index, base)

  @overload(int, int, int, int)
  def generate_CallProperty(
      self,
      nameIndex: int,
      base: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSShadowCheck::generate_CallProperty(int nameIndex,
    int base, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsshadowcheck.html#generate_CallProperty

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.

    base : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSShadowCheck::generate_CallProperty(int nameIndex, int base,
    #      int argc, int argv)
    ritual = 'ritual_ZN17QQmlJSShadowCheck21generate_CallPropertyEiiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQmlJSShadowCheck21generate_CallPropertyEiiii'
    self.uglySide.call(ritual, nameIndex, base, argc, argv)

  @overload(int, int, int, int)
  def generate_CallPropertyLookup(
      self,
      nameIndex: int,
      base: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSShadowCheck::generate_CallPropertyLookup(int
    nameIndex, int base, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsshadowcheck.html#generate_CallPropertyLookup

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.

    base : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSShadowCheck::generate_CallPropertyLookup(int nameIndex, int
    #      base, int argc, int argv)
    ritual = 'ritual_ZN17QQmlJSShadowCheck27generate_CallPropertyLookupEiiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSShadowCheck27generate_CallPropertyLookupEii'
          'ii')
    self.uglySide.call(ritual, nameIndex, base, argc, argv)

  @overload(QV4.Moth.Instr.Type)
  def endInstruction(self, a0: QV4.Moth.Instr.Type) -> None:
    """
    Calls Qt's 'void QQmlJSShadowCheck::endInstruction(QV4::Moth::Instr::Type
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsshadowcheck.html#endInstruction

    Parameters
    ----------

    a0 : QV4.Moth.Instr.Type
      Passed on as its number.
    """
    #  void QQmlJSShadowCheck::endInstruction(QV4::Moth::Instr::Type a0)
    ritual = (
        'ritual_ZN17QQmlJSShadowCheck14endInstructionEN3QV44Moth5Instr4Type'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSShadowCheck14endInstructionEN3QV44Moth5Inst'
          'r4TypeE')
    self.uglySide.call(ritual, a0.value)

  @overload(QQmlJSRegisterContent, int)
  def checkResettable(
      self,
      accumulatorIn: QQmlJSRegisterContent,
      instructionOffset: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSShadowCheck::checkResettable(QQmlJSRegisterContent
    accumulatorIn, int instructionOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsshadowcheck.html#checkResettable

    Parameters
    ----------

    accumulatorIn : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    instructionOffset : int
      Passed on as it is.
    """
    #  void QQmlJSShadowCheck::checkResettable(QQmlJSRegisterContent
    #      accumulatorIn, int instructionOffset)
    self.uglySide.call(
        'ritual_ZN17QQmlJSShadowCheck15checkResettableE21QQmlJSRegisterCont'
        'enti',
        self._valueOf(accumulatorIn), instructionOffset,
    )

  @staticmethod
  def checkBaseType(*__, **_) -> Never:
    """
    Qt's 'Shadowability
    QQmlJSShadowCheck::checkBaseType(QQmlJSRegisterContent baseType)': gives
    the enum 'QQmlJSShadowCheck::Shadowability', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QQmlJSShadowCheck.checkBaseType' has no cute function yet. Qt's "
        "'Shadowability "
        "QQmlJSShadowCheck::checkBaseType(QQmlJSRegisterContent baseType)': "
        "gives the enum 'QQmlJSShadowCheck::Shadowability', whose class "
        "cannot be named here.")

  @staticmethod
  def checkShadowing(*__, **_) -> Never:
    """
    Qt's 'Shadowability
    QQmlJSShadowCheck::checkShadowing(QQmlJSRegisterContent baseType, const
    QString &propertyName, int baseRegister)': gives the enum
    'QQmlJSShadowCheck::Shadowability', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQmlJSShadowCheck.checkShadowing' has no cute function yet. Qt's "
        "'Shadowability "
        "QQmlJSShadowCheck::checkShadowing(QQmlJSRegisterContent baseType, "
        "const QString &propertyName, int baseRegister)': gives the enum "
        "'QQmlJSShadowCheck::Shadowability', whose class cannot be named "
        "here.")
