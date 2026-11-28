"""
QV4::Compiler::Module binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Compiler::Module to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Module(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Compiler::Module: a plain Python object standing
  in front of one C++ QV4::Compiler::Module.

  C++ hands a QV4::Compiler::Module around as a copy, so every C++
  QV4::Compiler::Module behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QV4::Compiler::Module yet. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::Compiler::Module::~Module()': the destructor: Python removes
    its C++ QV4::Compiler::Module by it, and has no other use for it.
  - Qt's 'Context *QV4::Compiler::Module::newContext(QQmlJS::AST::Node *node,
    Context *parent, ContextType compilationMode)': names
    'QQmlJS::AST::Node', which has no cute class yet.

  What to expect
  --------------

  - The C++ QV4::Compiler::Module is created at the first use, not by
    'QV4::Compiler::Module(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Compiler::Module back gives a copy the ritual
    made for Python, in a new cute QV4::Compiler::Module.
  - Each name of Qt's QV4::Compiler::Module that has no cute function yet,
    'newContext', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QV4::Compiler::Module'

  #  Qt's '~QV4::Compiler::Module()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::Compiler::Module behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV48Compiler6ModuleD1Ev'

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

  @overload(str, str, bool)
  def __init__(self, fileName: str, finalUrl: str, debugMode: bool) -> None:
    """
    Notes what was given, for Qt's 'QV4::Compiler::Module::Module(const
    QString &fileName, const QString &finalUrl, bool debugMode)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compiler-module.html#Module

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    finalUrl : str
      Passed on as it is: a QString is made of it for the call.

    debugMode : bool
      Passed on as it is.
    """
    #  QV4::Compiler::Module::Module(const QString &fileName, const QString
    #      &finalUrl, bool debugMode)
    self._noteCreation(Module, lambda: Rituals.call(
        'ritual_ZN3QV48Compiler6ModuleC1ERK7QStringS4_b',
        fileName, finalUrl, debugMode,
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

  @staticmethod
  def newContext(*__, **_) -> Never:
    """
    Qt's 'Context *QV4::Compiler::Module::newContext(QQmlJS::AST::Node *node,
    Context *parent, ContextType compilationMode)': names
    'QQmlJS::AST::Node', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Compiler.Module.newContext' has no cute function yet. Qt's "
        "'Context *QV4::Compiler::Module::newContext(QQmlJS::AST::Node "
        "*node, Context *parent, ContextType compilationMode)': names "
        "'QQmlJS::AST::Node', which has no cute class yet.")
