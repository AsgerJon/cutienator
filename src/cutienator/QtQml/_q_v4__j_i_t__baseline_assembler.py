"""
QV4::JIT::BaselineAssembler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4baselineassembler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QV4::JIT::BaselineAssembler to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class BaselineAssembler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::JIT::BaselineAssembler: a plain Python object
  standing in front of one C++ QV4::JIT::BaselineAssembler.

  What exists
  -----------

  No function of Qt's QV4::JIT::BaselineAssembler yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  84 of the 84 functions Qt declares: 84 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QV4::JIT::BaselineAssembler is created at the first use, not by
    'QV4::JIT::BaselineAssembler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::JIT::BaselineAssembler.
  - Each name of Qt's QV4::JIT::BaselineAssembler that has no cute function
    yet, '__init__', 'add', 'addLabel', 'bitAnd', 'bitAndConst', 'bitOr',
    'bitOrConst', 'bitXor', 'bitXorConst', 'callRuntime', 'checkException',
    'clearUnwindHandler', 'cmp', 'cmpStrictEqual', 'cmpStrictNotEqual',
    'cmpeq', 'cmpeqInt', 'cmpeqNull', 'cmpge', 'cmpgt', 'cmple', 'cmplt',
    'cmpne', 'cmpneInt', 'cmpneNull', 'copyConst', 'deadTemporalZoneCheck',
    'dec', 'div', 'generateEpilogue', 'generatePrologue', 'getException',
    'gotoCatchException', 'inc', 'jsTailCall', 'jump', 'jumpEqNull',
    'jumpFalse', 'jumpNoException', 'jumpNotUndefined', 'jumpTrue', 'link',
    'loadAccumulatorFromFrame', 'loadConst', 'loadImport', 'loadLocal',
    'loadReg', 'loadString', 'loadValue', 'mod', 'moveReg', 'mul',
    'passAccumulatorAsArg', 'passCppFrameAsArg', 'passEngineAsArg',
    'passFunctionAsArg', 'passInt32AsArg', 'passJSSlotAsArg',
    'passPointerAsArg', 'popContext', 'prepareCallWithArgCount',
    'pushCatchContext', 'ret', 'saveAccumulatorInFrame', 'setException',
    'setUnwindHandler', 'shl', 'shlConst', 'shr', 'shrConst',
    'storeHeapObject', 'storeInstructionPointer', 'storeLocal', 'storeReg',
    'sub', 'toNumber', 'ucompl', 'uminus', 'unot', 'unwindDispatch',
    'unwindToLabel', 'ushr', 'ushrConst', holds a function that raises
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
  __qt_class__ = 'QV4::JIT::BaselineAssembler'

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
    Qt's 'QV4::JIT::BaselineAssembler::BaselineAssembler(const Value
    *constantTable)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: cannot initialize a new
    value of type 'PlatformAssembler' (aka 'int') with an lvalue of type
    'const Value *'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.__init__' has no cute function yet. "
        "Qt's 'QV4::JIT::BaselineAssembler::BaselineAssembler(const Value "
        "*constantTable)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: cannot "
        "initialize a new value of type 'PlatformAssembler' (aka 'int') "
        "with an lvalue of type 'const Value *'.")

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

  @staticmethod
  def add(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::add(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.add' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::add(int lhs)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def addLabel(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::addLabel(int offset)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.addLabel' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::addLabel(int offset)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pasm'.")

  @staticmethod
  def bitAnd(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::bitAnd(int lhs)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.bitAnd' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::bitAnd(int lhs)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'PlatformAssembler'.")

  @staticmethod
  def bitAndConst(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::bitAndConst(int rhs)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.bitAndConst' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::bitAndConst(int rhs)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pasm'.")

  @staticmethod
  def bitOr(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::bitOr(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.bitOr' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::bitOr(int lhs)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'PlatformAssembler'.")

  @staticmethod
  def bitOrConst(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::bitOrConst(int rhs)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.bitOrConst' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::bitOrConst(int rhs)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def bitXor(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::bitXor(int lhs)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.bitXor' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::bitXor(int lhs)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'PlatformAssembler'.")

  @staticmethod
  def bitXorConst(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::bitXorConst(int rhs)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.bitXorConst' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::bitXorConst(int rhs)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pasm'.")

  @staticmethod
  def callRuntime(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::callRuntime(const void *funcPtr,
    CallResultDestination dest)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.callRuntime' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::callRuntime(const void "
        "*funcPtr, CallResultDestination dest)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def checkException(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::checkException()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.checkException' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::checkException()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pasm'.")

  @staticmethod
  def clearUnwindHandler(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::clearUnwindHandler()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.clearUnwindHandler' has no cute "
        "function yet. Qt's 'void "
        "QV4::JIT::BaselineAssembler::clearUnwindHandler()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def cmp(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmp(int cond, CmpFunc function,
    int lhs)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmp' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::cmp(int cond, CmpFunc function, "
        "int lhs)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'PlatformAssembler'.")

  @staticmethod
  def cmpStrictEqual(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmpStrictEqual(int lhs)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmpStrictEqual' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::cmpStrictEqual(int "
        "lhs)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'PlatformAssembler'.")

  @staticmethod
  def cmpStrictNotEqual(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmpStrictNotEqual(int lhs)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmpStrictNotEqual' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::cmpStrictNotEqual(int "
        "lhs)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'PlatformAssembler'.")

  @staticmethod
  def cmpeq(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmpeq(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmpeq' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::cmpeq(int lhs)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'PlatformAssembler'.")

  @staticmethod
  def cmpeqInt(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmpeqInt(int lhs)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmpeqInt' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::cmpeqInt(int lhs)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def cmpeqNull(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmpeqNull()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmpeqNull' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::cmpeqNull()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def cmpge(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmpge(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmpge' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::cmpge(int lhs)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'PlatformAssembler'.")

  @staticmethod
  def cmpgt(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmpgt(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmpgt' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::cmpgt(int lhs)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'PlatformAssembler'.")

  @staticmethod
  def cmple(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmple(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmple' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::cmple(int lhs)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'PlatformAssembler'.")

  @staticmethod
  def cmplt(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmplt(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmplt' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::cmplt(int lhs)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'PlatformAssembler'.")

  @staticmethod
  def cmpne(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmpne(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmpne' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::cmpne(int lhs)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'PlatformAssembler'.")

  @staticmethod
  def cmpneInt(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmpneInt(int lhs)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmpneInt' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::cmpneInt(int lhs)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def cmpneNull(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::cmpneNull()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.cmpneNull' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::cmpneNull()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def copyConst(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::copyConst(int constIndex, int
    destReg)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.copyConst' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::copyConst(int constIndex, "
        "int destReg)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'pasm'.")

  @staticmethod
  def deadTemporalZoneCheck(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::deadTemporalZoneCheck(int
    offsetForSavedIP, int variableName)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.deadTemporalZoneCheck' has no cute "
        "function yet. Qt's 'void "
        "QV4::JIT::BaselineAssembler::deadTemporalZoneCheck(int "
        "offsetForSavedIP, int variableName)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def dec(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::dec()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.dec' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::dec()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def div(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::div(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.div' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::div(int lhs)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def generateEpilogue(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::generateEpilogue()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.generateEpilogue' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::generateEpilogue()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pasm'.")

  @staticmethod
  def generatePrologue(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::generatePrologue()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.generatePrologue' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::generatePrologue()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pasm'.")

  @staticmethod
  def getException(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::getException()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: unknown type name 'Address'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.getException' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::getException()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name 'Address'.")

  @staticmethod
  def gotoCatchException(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::gotoCatchException()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.gotoCatchException' has no cute "
        "function yet. Qt's 'void "
        "QV4::JIT::BaselineAssembler::gotoCatchException()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def inc(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::inc()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.inc' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::inc()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def jsTailCall(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::jsTailCall(int func, int
    thisObject, int argc, int argv)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: unknown
    type name 'Address'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.jsTailCall' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::jsTailCall(int func, int "
        "thisObject, int argc, int argv)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "unknown type name 'Address'.")

  @staticmethod
  def jump(*__, **_) -> Never:
    """
    Qt's 'int QV4::JIT::BaselineAssembler::jump(int offset)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.jump' has no cute function yet. Qt's "
        "'int QV4::JIT::BaselineAssembler::jump(int offset)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def jumpEqNull(*__, **_) -> Never:
    """
    Qt's 'int QV4::JIT::BaselineAssembler::jumpEqNull(int offset)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.jumpEqNull' has no cute function yet. "
        "Qt's 'int QV4::JIT::BaselineAssembler::jumpEqNull(int offset)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pasm'.")

  @staticmethod
  def jumpFalse(*__, **_) -> Never:
    """
    Qt's 'int QV4::JIT::BaselineAssembler::jumpFalse(int offset)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.jumpFalse' has no cute function yet. "
        "Qt's 'int QV4::JIT::BaselineAssembler::jumpFalse(int offset)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pasm'.")

  @staticmethod
  def jumpNoException(*__, **_) -> Never:
    """
    Qt's 'int QV4::JIT::BaselineAssembler::jumpNoException(int offset)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.jumpNoException' has no cute function "
        "yet. Qt's 'int QV4::JIT::BaselineAssembler::jumpNoException(int "
        "offset)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'pasm'.")

  @staticmethod
  def jumpNotUndefined(*__, **_) -> Never:
    """
    Qt's 'int QV4::JIT::BaselineAssembler::jumpNotUndefined(int offset)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.jumpNotUndefined' has no cute function "
        "yet. Qt's 'int QV4::JIT::BaselineAssembler::jumpNotUndefined(int "
        "offset)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'pasm'.")

  @staticmethod
  def jumpTrue(*__, **_) -> Never:
    """
    Qt's 'int QV4::JIT::BaselineAssembler::jumpTrue(int offset)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.jumpTrue' has no cute function yet. "
        "Qt's 'int QV4::JIT::BaselineAssembler::jumpTrue(int offset)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def link(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::link(Function *function)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.link' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::link(Function *function)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def loadAccumulatorFromFrame(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::loadAccumulatorFromFrame()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.loadAccumulatorFromFrame' has no cute "
        "function yet. Qt's 'void "
        "QV4::JIT::BaselineAssembler::loadAccumulatorFromFrame()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def loadConst(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::loadConst(int constIndex)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.loadConst' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::loadConst(int "
        "constIndex)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'pasm'.")

  @staticmethod
  def loadImport(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::loadImport(int index)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.loadImport' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::loadImport(int index)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pasm'.")

  @staticmethod
  def loadLocal(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::loadLocal(int index, int level)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.loadLocal' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::loadLocal(int index, int "
        "level)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'pasm'.")

  @staticmethod
  def loadReg(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::loadReg(int reg)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.loadReg' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::loadReg(int reg)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def loadString(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::loadString(int stringId)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.loadString' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::loadString(int stringId)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pasm'.")

  @staticmethod
  def loadValue(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::loadValue(ReturnedValue value)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.loadValue' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::loadValue(ReturnedValue "
        "value)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'pasm'.")

  @staticmethod
  def mod(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::mod(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.mod' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::mod(int lhs)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def moveReg(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::moveReg(int sourceReg, int
    destReg)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.moveReg' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::moveReg(int sourceReg, int "
        "destReg)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'pasm'.")

  @staticmethod
  def mul(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::mul(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.mul' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::mul(int lhs)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def passAccumulatorAsArg(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::passAccumulatorAsArg(int arg)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.passAccumulatorAsArg' has no cute "
        "function yet. Qt's 'void "
        "QV4::JIT::BaselineAssembler::passAccumulatorAsArg(int arg)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def passCppFrameAsArg(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::passCppFrameAsArg(int arg)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.passCppFrameAsArg' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::passCppFrameAsArg(int "
        "arg)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'pasm'.")

  @staticmethod
  def passEngineAsArg(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::passEngineAsArg(int arg)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.passEngineAsArg' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::passEngineAsArg(int "
        "arg)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'pasm'.")

  @staticmethod
  def passFunctionAsArg(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::passFunctionAsArg(int arg)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.passFunctionAsArg' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::passFunctionAsArg(int "
        "arg)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'pasm'.")

  @staticmethod
  def passInt32AsArg(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::passInt32AsArg(int value, int
    arg)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.passInt32AsArg' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::passInt32AsArg(int "
        "value, int arg)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'pasm'.")

  @staticmethod
  def passJSSlotAsArg(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::passJSSlotAsArg(int reg, int
    arg)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.passJSSlotAsArg' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::passJSSlotAsArg(int "
        "reg, int arg)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'pasm'.")

  @staticmethod
  def passPointerAsArg(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::passPointerAsArg(void *ptr, int
    arg)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.passPointerAsArg' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::passPointerAsArg(void "
        "*ptr, int arg)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'pasm'.")

  @staticmethod
  def popContext(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::popContext()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.popContext' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::popContext()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def prepareCallWithArgCount(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::prepareCallWithArgCount(int
    argc)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.prepareCallWithArgCount' has no cute "
        "function yet. Qt's 'void "
        "QV4::JIT::BaselineAssembler::prepareCallWithArgCount(int argc)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pasm'.")

  @staticmethod
  def pushCatchContext(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::pushCatchContext(int index, int
    name)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.pushCatchContext' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::pushCatchContext(int "
        "index, int name)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'pasm'.")

  @staticmethod
  def ret(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::ret()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.ret' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::ret()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def saveAccumulatorInFrame(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::saveAccumulatorInFrame()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.saveAccumulatorInFrame' has no cute "
        "function yet. Qt's 'void "
        "QV4::JIT::BaselineAssembler::saveAccumulatorInFrame()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def setException(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::setException()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.setException' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::setException()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def setUnwindHandler(*__, **_) -> Never:
    """
    Qt's 'int QV4::JIT::BaselineAssembler::setUnwindHandler(int offset)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.setUnwindHandler' has no cute function "
        "yet. Qt's 'int QV4::JIT::BaselineAssembler::setUnwindHandler(int "
        "offset)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'pasm'.")

  @staticmethod
  def shl(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::shl(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.shl' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::shl(int lhs)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'PlatformAssembler'.")

  @staticmethod
  def shlConst(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::shlConst(int rhs)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.shlConst' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::shlConst(int rhs)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def shr(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::shr(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.shr' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::shr(int lhs)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'PlatformAssembler'.")

  @staticmethod
  def shrConst(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::shrConst(int rhs)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.shrConst' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::shrConst(int rhs)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def storeHeapObject(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::storeHeapObject(int reg)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.storeHeapObject' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::storeHeapObject(int "
        "reg)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'pasm'.")

  @staticmethod
  def storeInstructionPointer(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::storeInstructionPointer(int
    instructionOffset)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.storeInstructionPointer' has no cute "
        "function yet. Qt's 'void "
        "QV4::JIT::BaselineAssembler::storeInstructionPointer(int "
        "instructionOffset)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'pasm'.")

  @staticmethod
  def storeLocal(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::storeLocal(int index, int
    level)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.storeLocal' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::storeLocal(int index, int "
        "level)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'pasm'.")

  @staticmethod
  def storeReg(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::storeReg(int reg)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.storeReg' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::storeReg(int reg)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def sub(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::sub(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.sub' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::sub(int lhs)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def toNumber(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::toNumber()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.toNumber' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::toNumber()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def ucompl(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::ucompl()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.ucompl' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::ucompl()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def uminus(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::uminus()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.uminus' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::uminus()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def unot(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::unot()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.unot' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::unot()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'pasm'.")

  @staticmethod
  def unwindDispatch(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::unwindDispatch()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.unwindDispatch' has no cute function "
        "yet. Qt's 'void QV4::JIT::BaselineAssembler::unwindDispatch()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pasm'.")

  @staticmethod
  def unwindToLabel(*__, **_) -> Never:
    """
    Qt's 'int QV4::JIT::BaselineAssembler::unwindToLabel(int level, int
    offset)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.unwindToLabel' has no cute function "
        "yet. Qt's 'int QV4::JIT::BaselineAssembler::unwindToLabel(int "
        "level, int offset)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'pasm'.")

  @staticmethod
  def ushr(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::ushr(int lhs)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'PlatformAssembler'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.ushr' has no cute function yet. Qt's "
        "'void QV4::JIT::BaselineAssembler::ushr(int lhs)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'PlatformAssembler'.")

  @staticmethod
  def ushrConst(*__, **_) -> Never:
    """
    Qt's 'void QV4::JIT::BaselineAssembler::ushrConst(int rhs)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'pasm'.
    """
    raise NotImplementedError(
        "'QV4.JIT.BaselineAssembler.ushrConst' has no cute function yet. "
        "Qt's 'void QV4::JIT::BaselineAssembler::ushrConst(int rhs)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'pasm'.")
