"""
QQmlJSAOTIRBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsaotirbuilder_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSAOTIRBuilder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQml import QQmlJS, QmlIR

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSAOTIRBuilder(QmlIR.IRBuilder):
  """
  The cute side of Qt's QQmlJSAOTIRBuilder: a plain Python object standing in
  front of one C++ QQmlJSAOTIRBuilder.

  It is built on the cute 'QmlIR::IRBuilder', as Qt's QQmlJSAOTIRBuilder is
  built on Qt's QmlIR::IRBuilder, and has everything that class has.

  C++ hands a QQmlJSAOTIRBuilder around as a copy, so every C++
  QQmlJSAOTIRBuilder behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSAOTIRBuilder that has a ritual and that Python
  can call so far, 2 names in all: 'visit', 'registerFunctionExpr'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJSAOTIRBuilder::setBindingValue(QV4::CompiledData::Binding
    *binding, QQmlJS::AST::Statement *statement, QQmlJS::AST::Node
    *parentNode)': names 'QQmlJS::AST::Statement', which has no cute class
    yet.
  - Qt's 'QQmlJSAOTIRBuilder::~QQmlJSAOTIRBuilder()': the destructor: Python
    removes its C++ QQmlJSAOTIRBuilder by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJSAOTIRBuilder is created at the first use, not by
    'QQmlJSAOTIRBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSAOTIRBuilder back gives a copy the ritual made
    for Python, in a new cute QQmlJSAOTIRBuilder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSAOTIRBuilder'

  #  A C++ QQmlJSAOTIRBuilder Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJSAOTIRBuilder'

  #  Qt's '~QQmlJSAOTIRBuilder()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJSAOTIRBuilder behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlJSAOTIRBuilderD1Ev'

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

  @overload(WAIT['QQmlJS.AST.FunctionExpression'])
  @overload(NoneType)
  def visit(self, ast: Optional[QQmlJS.AST.FunctionExpression]) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSAOTIRBuilder::visit(QQmlJS::AST::FunctionExpression *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsaotirbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::FunctionExpression *ast)
    ritual = (
        'ritual_ZN18QQmlJSAOTIRBuilder5visitEPN6QQmlJS3AST18FunctionExpress'
        'ionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQmlJSAOTIRBuilder5visitEPN6QQmlJS3AST18FunctionE'
          'xpressionE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.FunctionDeclaration'])
  def visit(self, ast: Optional[QQmlJS.AST.FunctionDeclaration]) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSAOTIRBuilder::visit(QQmlJS::AST::FunctionDeclaration *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsaotirbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.FunctionDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::FunctionDeclaration *ast)
    ritual = (
        'ritual_ZN18QQmlJSAOTIRBuilder5visitEPN6QQmlJS3AST19FunctionDeclara'
        'tionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQmlJSAOTIRBuilder5visitEPN6QQmlJS3AST19FunctionD'
          'eclarationE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiSourceElement'])
  def visit(self, node: Optional[QQmlJS.AST.UiSourceElement]) -> bool:
    """
    Calls Qt's 'bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::UiSourceElement
    *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsaotirbuilder.html#visit

    Parameters
    ----------

    node : Optional[QQmlJS.AST.UiSourceElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::UiSourceElement *node)
    ritual = (
        'ritual_ZN18QQmlJSAOTIRBuilder5visitEPN6QQmlJS3AST15UiSourceElement'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQmlJSAOTIRBuilder5visitEPN6QQmlJS3AST15UiSourceE'
          'lementE')
    return self.uglySide.call(ritual, self._addressOf(node))

  @overload(
      WAIT['QQmlJS.AST.FunctionExpression'], QmlIR.IRBuilder.IsQmlFunction,
  )
  @overload(NoneType, QmlIR.IRBuilder.IsQmlFunction)
  def registerFunctionExpr(
      self,
      fexp: Optional[QQmlJS.AST.FunctionExpression],
      a1: QmlIR.IRBuilder.IsQmlFunction,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSAOTIRBuilder::registerFunctionExpr(QQmlJS::AST::FunctionExpression
    *fexp, IsQmlFunction a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsaotirbuilder.html#registerFunctionExpr

    Parameters
    ----------

    fexp : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QmlIR.IRBuilder.IsQmlFunction
      Passed on as its number.
    """
    #  void QQmlJSAOTIRBuilder::registerFunctionExpr(QQmlJS::AST::
    #      FunctionExpression *fexp, IsQmlFunction a1)
    ritual = (
        'ritual_ZN18QQmlJSAOTIRBuilder20registerFunctionExprEPN6QQmlJS3AST1'
        '8FunctionExpressionEN5QmlIR9IRBuilder13IsQmlFunctionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQmlJSAOTIRBuilder20registerFunctionExprEPN6QQmlJ'
          'S3AST18FunctionExpressionEN5QmlIR9IRBuilder13IsQmlFunctionE')
    self.uglySide.call(ritual, self._addressOf(fexp), a1.value)
