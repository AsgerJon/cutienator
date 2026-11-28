"""
QV4::Compiler::ScanFunctions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compilerscanfunctions_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QV4::Compiler::ScanFunctions to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QV4, QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ScanFunctions(QQmlJS.AST.Visitor):
  """
  The cute side of Qt's QV4::Compiler::ScanFunctions: a plain Python object
  standing in front of one C++ QV4::Compiler::ScanFunctions.

  It is built on the cute 'QQmlJS::AST::Visitor', as Qt's
  QV4::Compiler::ScanFunctions is built on Qt's QQmlJS::AST::Visitor, and has
  everything that class has.

  C++ hands a QV4::Compiler::ScanFunctions around as a copy, so every C++
  QV4::Compiler::ScanFunctions behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::Compiler::ScanFunctions that has a ritual and
  that Python can call so far, 9 names in all:
  'handleTopLevelFunctionFormals', 'enterGlobalEnvironment',
  'leaveEnvironment', 'enterQmlFunction', 'checkDirectivePrologue',
  'checkName', 'visit', 'endVisit', 'throwRecursionDepthError'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    QV4::Compiler::ScanFunctions::enterEnvironment(QQmlJS::AST::Node *node,
    ContextType compilationMode, const QString &name)': names
    'QQmlJS::AST::Node', which has no cute class yet.
  - Qt's 'bool QV4::Compiler::ScanFunctions::enterFunction(QQmlJS::AST::
    FunctionExpression *ast, FunctionNameContext nameContext)': names the
    enum 'QV4::Compiler::ScanFunctions::FunctionNameContext', whose class
    cannot be named here.
  - Qt's 'bool QV4::Compiler::ScanFunctions::enterFunction(QQmlJS::AST::Node
    *ast, const QString &name, QQmlJS::AST::FormalParameterList *formals,
    QQmlJS::AST::StatementList *body, FunctionNameContext nameContext)':
    names 'QQmlJS::AST::Node', which has no cute class yet.
  - Qt's 'QV4::Compiler::ScanFunctions::~ScanFunctions()': the destructor:
    Python removes its C++ QV4::Compiler::ScanFunctions by it, and has no
    other use for it.

  What has no ritual
  ------------------

  3 of the 53 functions Qt declares: 2 leans on 'QV4; 1 Qt's library has no
  name for it, and its code in Qt's source does not compile apart from its
  file.

  What to expect
  --------------

  - The C++ QV4::Compiler::ScanFunctions is created at the first use, not by
    'QV4::Compiler::ScanFunctions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Compiler::ScanFunctions back gives a copy the
    ritual made for Python, in a new cute QV4::Compiler::ScanFunctions.
  - Each name of Qt's QV4::Compiler::ScanFunctions that has no cute function
    yet, '__init__', 'calcEscapingVariables', 'enterEnvironment',
    'enterFunction', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Compiler::ScanFunctions'

  #  Qt's '~QV4::Compiler::ScanFunctions()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::Compiler::ScanFunctions behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV48Compiler13ScanFunctionsD1Ev'

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
    Qt's 'QV4::Compiler::ScanFunctions::ScanFunctions(Codegen *cg, const
    QString &sourceCode, ContextType defaultProgramType)': leans on
    'QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ExportDeclaration*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Compiler.ScanFunctions.__init__' has no cute function yet. "
        "Qt's 'QV4::Compiler::ScanFunctions::ScanFunctions(Codegen *cg, "
        "const QString &sourceCode, ContextType defaultProgramType)': leans "
        "on "
        "'QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ExportDeclaration"
        "*)', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

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

  @overload(WAIT['QQmlJS.AST.FunctionExpression'])
  @overload(NoneType)
  def handleTopLevelFunctionFormals(
      self,
      node: Optional[QQmlJS.AST.FunctionExpression],
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::handleTopLevelFunctionFormals(QQmlJS::
    AST::FunctionExpression *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html

    Parameters
    ----------

    node : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::handleTopLevelFunctionFormals(
    #      QQmlJS::AST::FunctionExpression *node)
    self.uglySide.call(
        'ritual_ZN3QV48Compiler13ScanFunctions29handleTopLevelFunctionForma'
        'lsEPN6QQmlJS3AST18FunctionExpressionE',
        self._addressOf(node),
    )

  @overload(QV4.Compiler.ContextType)
  def enterGlobalEnvironment(
      self,
      compilationMode: QV4.Compiler.ContextType,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::enterGlobalEnvironment(ContextType
    compilationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html

    Parameters
    ----------

    compilationMode : QV4.Compiler.ContextType
      Passed on as its number.
    """
    #  void QV4::Compiler::ScanFunctions::enterGlobalEnvironment(ContextType
    #      compilationMode)
    self.uglySide.call(
        'ritual_ZN3QV48Compiler13ScanFunctions22enterGlobalEnvironmentENS0_'
        '11ContextTypeE',
        compilationMode.value,
    )

  def leaveEnvironment(self) -> None:
    """
    Calls Qt's 'void QV4::Compiler::ScanFunctions::leaveEnvironment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#leaveEnvironment
    """
    #  void QV4::Compiler::ScanFunctions::leaveEnvironment()
    self.uglySide.call(
        'ritual_ZN3QV48Compiler13ScanFunctions16leaveEnvironmentEv',
    )

  @overload(WAIT['QQmlJS.AST.FunctionExpression'])
  @overload(NoneType)
  def enterQmlFunction(
      self,
      ast: Optional[QQmlJS.AST.FunctionExpression],
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::enterQmlFunction(QQmlJS::AST::
    FunctionExpression *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#enterQmlFunction

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::enterQmlFunction(QQmlJS::AST::
    #      FunctionExpression *ast)
    self.uglySide.call(
        'ritual_ZN3QV48Compiler13ScanFunctions16enterQmlFunctionEPN6QQmlJS3'
        'AST18FunctionExpressionE',
        self._addressOf(ast),
    )

  @overload(WAIT['QQmlJS.AST.StatementList'])
  @overload(NoneType)
  def checkDirectivePrologue(
      self,
      ast: Optional[QQmlJS.AST.StatementList],
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::checkDirectivePrologue(QQmlJS::AST::
    StatementList *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.StatementList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::checkDirectivePrologue(QQmlJS::
    #      AST::StatementList *ast)
    self.uglySide.call(
        'ritual_ZN3QV48Compiler13ScanFunctions22checkDirectivePrologueEPN6Q'
        'QmlJS3AST13StatementListE',
        self._addressOf(ast),
    )

  @overload(str, WAIT['QQmlJS.SourceLocation'])
  def checkName(self, name: str, loc: QQmlJS.SourceLocation) -> None:
    """
    Calls Qt's 'void QV4::Compiler::ScanFunctions::checkName(QStringView
    name, const QQmlJS::SourceLocation &loc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#checkName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    loc : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QV4::Compiler::ScanFunctions::checkName(QStringView name, const
    #      QQmlJS::SourceLocation &loc)
    self.uglySide.call(
        'ritual_ZN3QV48Compiler13ScanFunctions9checkNameE11QStringViewRKN6Q'
        'QmlJS14SourceLocationE',
        name, self._valueOf(loc),
    )

  @overload(WAIT['QQmlJS.AST.Program'])
  @overload(NoneType)
  def visit(self, ast: Optional[QQmlJS.AST.Program]) -> bool:
    """
    Calls Qt's 'bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::Program
    *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.Program]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::Program *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST7ProgramE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST7Pr'
          'ogramE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.ESModule'])
  def visit(self, ast: Optional[QQmlJS.AST.ESModule]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ESModule *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ESModule]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ESModule *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST8ESModule'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST8ES'
          'ModuleE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.ExportDeclaration'])
  def visit(
      self,
      declaration: Optional[QQmlJS.AST.ExportDeclaration],
  ) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ExportDeclaration
    *declaration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    declaration : Optional[QQmlJS.AST.ExportDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool
    #      QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ExportDeclaration
    #      *declaration)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST17ExportD'
        'eclarationE',
        self._addressOf(declaration),
    )

  @overload(WAIT['QQmlJS.AST.ImportDeclaration'])
  def visit(
      self,
      declaration: Optional[QQmlJS.AST.ImportDeclaration],
  ) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ImportDeclaration
    *declaration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    declaration : Optional[QQmlJS.AST.ImportDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool
    #      QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ImportDeclaration
    #      *declaration)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST17ImportD'
        'eclarationE',
        self._addressOf(declaration),
    )

  @overload(WAIT['QQmlJS.AST.CallExpression'])
  def visit(self, ast: Optional[QQmlJS.AST.CallExpression]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::CallExpression *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.CallExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::CallExpression
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14CallExp'
        'ressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14C'
          'allExpressionE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.PatternElement'])
  def visit(self, ast: Optional[QQmlJS.AST.PatternElement]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::PatternElement *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.PatternElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::PatternElement
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14Pattern'
        'ElementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14P'
          'atternElementE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.IdentifierExpression'])
  def visit(self, ast: Optional[QQmlJS.AST.IdentifierExpression]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::IdentifierExpression
    *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.IdentifierExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::
    #      IdentifierExpression *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST20Identif'
        'ierExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST20I'
          'dentifierExpressionE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.ExpressionStatement'])
  def visit(self, ast: Optional[QQmlJS.AST.ExpressionStatement]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ExpressionStatement
    *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ExpressionStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::
    #      ExpressionStatement *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST19Express'
        'ionStatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST19E'
          'xpressionStatementE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.FunctionExpression'])
  def visit(self, ast: Optional[QQmlJS.AST.FunctionExpression]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::FunctionExpression
    *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::
    #      FunctionExpression *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST18Functio'
        'nExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST18F'
          'unctionExpressionE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.TemplateLiteral'])
  def visit(self, ast: Optional[QQmlJS.AST.TemplateLiteral]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::TemplateLiteral *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.TemplateLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::TemplateLiteral
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15Templat'
        'eLiteralE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15T'
          'emplateLiteralE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.SuperLiteral'])
  def visit(self, a0: Optional[QQmlJS.AST.SuperLiteral]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::SuperLiteral *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.SuperLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::SuperLiteral
    #      *a0)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12SuperLi'
        'teralE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12S'
          'uperLiteralE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FieldMemberExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.FieldMemberExpression]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::FieldMemberExpression
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FieldMemberExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::
    #      FieldMemberExpression *a0)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST21FieldMe'
        'mberExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST21F'
          'ieldMemberExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ArrayPattern'])
  def visit(self, a0: Optional[QQmlJS.AST.ArrayPattern]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ArrayPattern *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ArrayPattern]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ArrayPattern
    #      *a0)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12ArrayPa'
        'tternE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12A'
          'rrayPatternE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ObjectPattern'])
  def visit(self, ast: Optional[QQmlJS.AST.ObjectPattern]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ObjectPattern *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ObjectPattern]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ObjectPattern
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST13ObjectP'
        'atternE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST13O'
          'bjectPatternE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.PatternProperty'])
  def visit(self, ast: Optional[QQmlJS.AST.PatternProperty]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::PatternProperty *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.PatternProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::PatternProperty
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15Pattern'
        'PropertyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15P'
          'atternPropertyE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.FunctionDeclaration'])
  def visit(self, ast: Optional[QQmlJS.AST.FunctionDeclaration]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::FunctionDeclaration
    *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.FunctionDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::
    #      FunctionDeclaration *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST19Functio'
        'nDeclarationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST19F'
          'unctionDeclarationE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.ClassExpression'])
  def visit(self, ast: Optional[QQmlJS.AST.ClassExpression]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ClassExpression *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ClassExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ClassExpression
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15ClassEx'
        'pressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15C'
          'lassExpressionE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.ClassDeclaration'])
  def visit(self, ast: Optional[QQmlJS.AST.ClassDeclaration]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ClassDeclaration *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ClassDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ClassDeclaration
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16ClassDe'
        'clarationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16C'
          'lassDeclarationE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.DoWhileStatement'])
  def visit(self, ast: Optional[QQmlJS.AST.DoWhileStatement]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::DoWhileStatement *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.DoWhileStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::DoWhileStatement
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16DoWhile'
        'StatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16D'
          'oWhileStatementE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.ForStatement'])
  def visit(self, ast: Optional[QQmlJS.AST.ForStatement]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ForStatement *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ForStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ForStatement
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12ForStat'
        'ementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12F'
          'orStatementE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.ForEachStatement'])
  def visit(self, ast: Optional[QQmlJS.AST.ForEachStatement]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ForEachStatement *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ForEachStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ForEachStatement
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16ForEach'
        'StatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16F'
          'orEachStatementE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.ThisExpression'])
  def visit(self, ast: Optional[QQmlJS.AST.ThisExpression]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ThisExpression *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ThisExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ThisExpression
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14ThisExp'
        'ressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14T'
          'hisExpressionE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.Block'])
  def visit(self, ast: Optional[QQmlJS.AST.Block]) -> bool:
    """
    Calls Qt's 'bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::Block
    *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.Block]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::Block *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST5BlockE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST5Bl'
          'ockE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.CaseBlock'])
  def visit(self, ast: Optional[QQmlJS.AST.CaseBlock]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::CaseBlock *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.CaseBlock]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::CaseBlock *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST9CaseBloc'
        'kE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST9Ca'
          'seBlockE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.Catch'])
  def visit(self, ast: Optional[QQmlJS.AST.Catch]) -> bool:
    """
    Calls Qt's 'bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::Catch
    *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.Catch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::Catch *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST5CatchE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST5Ca'
          'tchE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.WithStatement'])
  def visit(self, ast: Optional[QQmlJS.AST.WithStatement]) -> bool:
    """
    Calls Qt's 'bool
    QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::WithStatement *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.WithStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::WithStatement
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST13WithSta'
        'tementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST13W'
          'ithStatementE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.Program'])
  @overload(NoneType)
  def endVisit(self, a0: Optional[QQmlJS.AST.Program]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::Program *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Program]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::Program *a0)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST7Progr'
        'amE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '7ProgramE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ESModule'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ESModule]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ESModule *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ESModule]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ESModule *a0)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST8ESMod'
        'uleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '8ESModuleE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FunctionExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.FunctionExpression]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::FunctionExpression
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::
    #      FunctionExpression *a0)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST18Func'
        'tionExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '18FunctionExpressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PatternProperty'])
  def endVisit(self, a0: Optional[QQmlJS.AST.PatternProperty]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::PatternProperty
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PatternProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::
    #      PatternProperty *a0)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST15Patt'
        'ernPropertyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '15PatternPropertyE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FunctionDeclaration'])
  def endVisit(self, a0: Optional[QQmlJS.AST.FunctionDeclaration]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::FunctionDeclaration
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FunctionDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::
    #      FunctionDeclaration *a0)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST19Func'
        'tionDeclarationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '19FunctionDeclarationE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ClassExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ClassExpression]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ClassExpression
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ClassExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::
    #      ClassExpression *a0)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST15Clas'
        'sExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '15ClassExpressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ClassDeclaration'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ClassDeclaration]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ClassDeclaration
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ClassDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::
    #      ClassDeclaration *a0)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST16Clas'
        'sDeclarationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '16ClassDeclarationE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ForStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ForStatement]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ForStatement *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ForStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ForStatement
    #      *a0)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST12ForS'
        'tatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '12ForStatementE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ForEachStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ForEachStatement]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ForEachStatement
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ForEachStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::
    #      ForEachStatement *a0)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST16ForE'
        'achStatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '16ForEachStatementE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Block'])
  def endVisit(self, ast: Optional[QQmlJS.AST.Block]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::Block *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.Block]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::Block *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST5Block'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '5BlockE')
    self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.CaseBlock'])
  def endVisit(self, ast: Optional[QQmlJS.AST.CaseBlock]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::CaseBlock *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.CaseBlock]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::CaseBlock
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST9CaseB'
        'lockE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '9CaseBlockE')
    self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.Catch'])
  def endVisit(self, ast: Optional[QQmlJS.AST.Catch]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::Catch *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.Catch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::Catch *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST5Catch'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '5CatchE')
    self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.WithStatement'])
  def endVisit(self, ast: Optional[QQmlJS.AST.WithStatement]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::WithStatement *ast)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html#endVisit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.WithStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::WithStatement
    #      *ast)
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST13With'
        'StatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST'
          '13WithStatementE')
    self.uglySide.call(ritual, self._addressOf(ast))

  def throwRecursionDepthError(self) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::ScanFunctions::throwRecursionDepthError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-scanfunctions.html
    """
    #  void QV4::Compiler::ScanFunctions::throwRecursionDepthError()
    ritual = (
        'ritual_ZN3QV48Compiler13ScanFunctions24throwRecursionDepthErrorEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler13ScanFunctions24throwRecursionDepthEr'
          'rorEv')
    self.uglySide.call(ritual)

  @staticmethod
  def calcEscapingVariables(*__, **_) -> Never:
    """
    Qt's 'void QV4::Compiler::ScanFunctions::calcEscapingVariables()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'Iteration'; did you
    mean 'QtTaskTree::Iterator'?.
    """
    raise NotImplementedError(
        "'QV4.Compiler.ScanFunctions.calcEscapingVariables' has no cute "
        "function yet. Qt's 'void "
        "QV4::Compiler::ScanFunctions::calcEscapingVariables()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'Iteration'; did you mean 'QtTaskTree::Iterator'?.")

  @staticmethod
  def enterEnvironment(*__, **_) -> Never:
    """
    Qt's 'void
    QV4::Compiler::ScanFunctions::enterEnvironment(QQmlJS::AST::Node *node,
    ContextType compilationMode, const QString &name)': names
    'QQmlJS::AST::Node', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Compiler.ScanFunctions.enterEnvironment' has no cute function "
        "yet. Qt's 'void "
        "QV4::Compiler::ScanFunctions::enterEnvironment(QQmlJS::AST::Node "
        "*node, ContextType compilationMode, const QString &name)': names "
        "'QQmlJS::AST::Node', which has no cute class yet.")

  @staticmethod
  def enterFunction(*__, **_) -> Never:
    """
    - Qt's 'bool QV4::Compiler::ScanFunctions::enterFunction(QQmlJS::AST::
      FunctionExpression *ast, FunctionNameContext nameContext)': names the
      enum 'QV4::Compiler::ScanFunctions::FunctionNameContext', whose class
      cannot be named here.
    - Qt's 'bool
      QV4::Compiler::ScanFunctions::enterFunction(QQmlJS::AST::Node *ast,
      const QString &name, QQmlJS::AST::FormalParameterList *formals,
      QQmlJS::AST::StatementList *body, FunctionNameContext nameContext)':
      names 'QQmlJS::AST::Node', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Compiler.ScanFunctions.enterFunction' has no cute function "
        "yet. Qt's 'bool "
        "QV4::Compiler::ScanFunctions::enterFunction(QQmlJS::AST::FunctionEx"
        "pression *ast, FunctionNameContext nameContext)': names the enum "
        "'QV4::Compiler::ScanFunctions::FunctionNameContext', whose class "
        "cannot be named here. Qt's 'bool "
        "QV4::Compiler::ScanFunctions::enterFunction(QQmlJS::AST::Node "
        "*ast, const QString &name, QQmlJS::AST::FormalParameterList "
        "*formals, QQmlJS::AST::StatementList *body, FunctionNameContext "
        "nameContext)': names 'QQmlJS::AST::Node', which has no cute class "
        "yet.")
