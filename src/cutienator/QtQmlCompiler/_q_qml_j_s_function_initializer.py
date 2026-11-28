"""
QQmlJSFunctionInitializer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsfunctioninitializer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSFunctionInitializer to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQml import QQmlJS, QV4
from . import QQmlJSCompilePass

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


class QQmlJSFunctionInitializer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSFunctionInitializer: a plain Python object
  standing in front of one C++ QQmlJSFunctionInitializer.

  What exists
  -----------

  Every function of Qt's QQmlJSFunctionInitializer that has a ritual and that
  Python can call so far, 1 name in all: 'populateSignature'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSCompilePass::Function QQmlJSFunctionInitializer::run(const
    QV4::Compiler::Context *context, const QString &propertyName,
    QQmlJS::AST::Node *astNode, const QmlIR::Binding &irBinding)': names
    'QQmlJS::AST::Node', which has no cute class yet.
  - Qt's 'QQmlJSCompilePass::Function QQmlJSFunctionInitializer::run(const
    QV4::Compiler::Context *context, const QString &functionName,
    QQmlJS::AST::Node *astNode)': names 'QQmlJS::AST::Node', which has no
    cute class yet.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QQmlJSFunctionInitializer is created at the first use, not by
    'QQmlJSFunctionInitializer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSFunctionInitializer.
  - Each name of Qt's QQmlJSFunctionInitializer that has no cute function
    yet, 'run', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QQmlJSFunctionInitializer'

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
      QQmlJSTypeResolver, WAIT['QV4.CompiledData.Location'],
      WAIT['QV4.CompiledData.Location'], QQmlJSLogger,
  )
  @overload(
      QQmlJSTypeResolver, WAIT['QV4.CompiledData.Location'],
      WAIT['QV4.CompiledData.Location'], NoneType,
  )
  @overload(
      NoneType, WAIT['QV4.CompiledData.Location'],
      WAIT['QV4.CompiledData.Location'], QQmlJSLogger,
  )
  @overload(
      NoneType, WAIT['QV4.CompiledData.Location'],
      WAIT['QV4.CompiledData.Location'], NoneType,
  )
  def __init__(
      self,
      typeResolver: Optional[QQmlJSTypeResolver],
      objectLocation: QV4.CompiledData.Location,
      scopeLocation: QV4.CompiledData.Location,
      logger: Optional[QQmlJSLogger],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSFunctionInitializer::QQmlJSFunctionInitializer(const
    QQmlJSTypeResolver *typeResolver, const QV4::CompiledData::Location
    &objectLocation, const QV4::CompiledData::Location &scopeLocation,
    QQmlJSLogger *logger)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfunctioninitializer.html

    Parameters
    ----------

    typeResolver : Optional[QQmlJSTypeResolver]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    objectLocation : QV4.CompiledData.Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.

    scopeLocation : QV4.CompiledData.Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.

    logger : Optional[QQmlJSLogger]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJSFunctionInitializer::QQmlJSFunctionInitializer(const
    #      QQmlJSTypeResolver *typeResolver, const
    #      QV4::CompiledData::Location &objectLocation, const
    #      QV4::CompiledData::Location &scopeLocation, QQmlJSLogger *logger)
    self._noteCreation(QQmlJSFunctionInitializer, lambda: Rituals.call(
        'ritual_ZN25QQmlJSFunctionInitializerC1EPK18QQmlJSTypeResolverRKN3Q'
        'V412CompiledData8LocationES7_P12QQmlJSLogger',
        self._addressOf(typeResolver), self._valueOf(objectLocation),
        self._valueOf(scopeLocation), self._addressOf(logger),
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

  @overload(
      WAIT['QV4.Compiler.Context'], WAIT['QQmlJS.AST.FunctionExpression'],
      QQmlJSCompilePass.Function,
  )
  @overload(
      WAIT['QV4.Compiler.Context'], WAIT['QQmlJS.AST.FunctionExpression'],
      NoneType,
  )
  @overload(
      WAIT['QV4.Compiler.Context'], NoneType, QQmlJSCompilePass.Function,
  )
  @overload(WAIT['QV4.Compiler.Context'], NoneType, NoneType)
  @overload(
      NoneType, WAIT['QQmlJS.AST.FunctionExpression'],
      QQmlJSCompilePass.Function,
  )
  @overload(NoneType, WAIT['QQmlJS.AST.FunctionExpression'], NoneType)
  @overload(NoneType, NoneType, QQmlJSCompilePass.Function)
  @overload(NoneType, NoneType, NoneType)
  def populateSignature(
      self,
      context: Optional[QV4.Compiler.Context],
      ast: Optional[QQmlJS.AST.FunctionExpression],
      function: Optional[QQmlJSCompilePass.Function],
  ) -> None:
    """
    Calls Qt's 'void QQmlJSFunctionInitializer::populateSignature(const
    QV4::Compiler::Context *context, QQmlJS::AST::FunctionExpression *ast,
    QQmlJSCompilePass::Function *function)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsfunctioninitializer.html#populateSignature

    Parameters
    ----------

    context : Optional[QV4.Compiler.Context]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ast : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : Optional[QQmlJSCompilePass.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSFunctionInitializer::populateSignature(const
    #      QV4::Compiler::Context *context, QQmlJS::AST::FunctionExpression
    #      *ast, QQmlJSCompilePass::Function *function)
    self.uglySide.call(
        'ritual_ZN25QQmlJSFunctionInitializer17populateSignatureEPKN3QV48Co'
        'mpiler7ContextEPN6QQmlJS3AST18FunctionExpressionEPN17QQmlJSCompile'
        'Pass8FunctionE',
        self._addressOf(context), self._addressOf(ast),
        self._addressOf(function),
    )

  @staticmethod
  def run(*__, **_) -> Never:
    """
    - Qt's 'QQmlJSCompilePass::Function QQmlJSFunctionInitializer::run(const
      QV4::Compiler::Context *context, const QString &propertyName,
      QQmlJS::AST::Node *astNode, const QmlIR::Binding &irBinding)': names
      'QQmlJS::AST::Node', which has no cute class yet.
    - Qt's 'QQmlJSCompilePass::Function QQmlJSFunctionInitializer::run(const
      QV4::Compiler::Context *context, const QString &functionName,
      QQmlJS::AST::Node *astNode)': names 'QQmlJS::AST::Node', which has no
      cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJSFunctionInitializer.run' has no cute function yet. Qt's "
        "'QQmlJSCompilePass::Function QQmlJSFunctionInitializer::run(const "
        "QV4::Compiler::Context *context, const QString &propertyName, "
        "QQmlJS::AST::Node *astNode, const QmlIR::Binding &irBinding)': "
        "names 'QQmlJS::AST::Node', which has no cute class yet. Qt's "
        "'QQmlJSCompilePass::Function QQmlJSFunctionInitializer::run(const "
        "QV4::Compiler::Context *context, const QString &functionName, "
        "QQmlJS::AST::Node *astNode)': names 'QQmlJS::AST::Node', which has "
        "no cute class yet.")
