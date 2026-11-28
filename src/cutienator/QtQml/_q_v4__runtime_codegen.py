"""
QV4::RuntimeCodegen binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4runtimecodegen_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::RuntimeCodegen to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlJS, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RuntimeCodegen(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::RuntimeCodegen: a plain Python object standing
  in front of one C++ QV4::RuntimeCodegen.

  What exists
  -----------

  Every function of Qt's QV4::RuntimeCodegen that has a ritual and that
  Python can call so far, 2 names in all: 'throwSyntaxError',
  'throwReferenceError'. It can be made from Python, in 1 way; see
  '__init__'.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::RuntimeCodegen is created at the first use, not by
    'QV4::RuntimeCodegen(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::RuntimeCodegen.
  - Each name of Qt's QV4::RuntimeCodegen that has no cute function yet,
    'generateFromFunctionExpression', holds a function that raises
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
  __qt_class__ = 'QV4::RuntimeCodegen'

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
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Compiler.JSUnitGenerator'],
      bool,
  )
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, bool)
  @overload(NoneType, WAIT['QV4.Compiler.JSUnitGenerator'], bool)
  @overload(NoneType, NoneType, bool)
  def __init__(
      self,
      engine: Optional[QV4.ExecutionEngine],
      jsUnitGenerator: Optional[QV4.Compiler.JSUnitGenerator],
      strict: bool,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::RuntimeCodegen::RuntimeCodegen(ExecutionEngine *engine,
    Compiler::JSUnitGenerator *jsUnitGenerator, bool strict)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimecodegen.html#RuntimeCodegen

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    jsUnitGenerator : Optional[QV4.Compiler.JSUnitGenerator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    strict : bool
      Passed on as it is.
    """
    #  QV4::RuntimeCodegen::RuntimeCodegen(ExecutionEngine *engine,
    #      Compiler::JSUnitGenerator *jsUnitGenerator, bool strict)
    self._noteCreation(RuntimeCodegen, lambda: Rituals.call(
        'ritual_ZN3QV414RuntimeCodegenC1EPNS_15ExecutionEngineEPNS_8Compile'
        'r15JSUnitGeneratorEb',
        self._addressOf(engine), self._addressOf(jsUnitGenerator), strict,
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

  @overload(WAIT['QQmlJS.SourceLocation'], str)
  def throwSyntaxError(
      self,
      loc: QQmlJS.SourceLocation,
      detail: str,
  ) -> None:
    """
    Calls Qt's 'void QV4::RuntimeCodegen::throwSyntaxError(const
    QQmlJS::SourceLocation &loc, const QString &detail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimecodegen.html#throwSyntaxError

    Parameters
    ----------

    loc : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    detail : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QV4::RuntimeCodegen::throwSyntaxError(const
    #      QQmlJS::SourceLocation &loc, const QString &detail)
    ritual = (
        'ritual_ZN3QV414RuntimeCodegen16throwSyntaxErrorERKN6QQmlJS14Source'
        'LocationERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV414RuntimeCodegen16throwSyntaxErrorERKN6QQmlJS14'
          'SourceLocationERK7QString')
    self.uglySide.call(ritual, self._valueOf(loc), detail)

  @overload(WAIT['QQmlJS.SourceLocation'], str)
  def throwReferenceError(
      self,
      loc: QQmlJS.SourceLocation,
      detail: str,
  ) -> None:
    """
    Calls Qt's 'void QV4::RuntimeCodegen::throwReferenceError(const
    QQmlJS::SourceLocation &loc, const QString &detail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-runtimecodegen.html#throwReferenceError

    Parameters
    ----------

    loc : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    detail : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QV4::RuntimeCodegen::throwReferenceError(const
    #      QQmlJS::SourceLocation &loc, const QString &detail)
    ritual = (
        'ritual_ZN3QV414RuntimeCodegen19throwReferenceErrorERKN6QQmlJS14Sou'
        'rceLocationERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV414RuntimeCodegen19throwReferenceErrorERKN6QQmlJ'
          'S14SourceLocationERK7QString')
    self.uglySide.call(ritual, self._valueOf(loc), detail)

  @staticmethod
  def generateFromFunctionExpression(*__, **_) -> Never:
    """
    Qt's 'void QV4::RuntimeCodegen::generateFromFunctionExpression(const
    QString &sourceCode, QQmlJS::AST::FunctionExpression *ast,
    Compiler::Module *module)': leans on
    'QV4::Compiler::ScanFunctions::operator()(QQmlJS::AST::Node*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QV4.RuntimeCodegen.generateFromFunctionExpression' has no cute "
        "function yet. Qt's 'void "
        "QV4::RuntimeCodegen::generateFromFunctionExpression(const QString "
        "&sourceCode, QQmlJS::AST::FunctionExpression *ast, "
        "Compiler::Module *module)': leans on "
        "'QV4::Compiler::ScanFunctions::operator()(QQmlJS::AST::Node*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
