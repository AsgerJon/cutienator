"""
QQmlScriptData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlscriptdata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlScriptData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlScriptData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlScriptData: a plain Python object standing in
  front of one C++ QQmlScriptData.

  What exists
  -----------

  No function of Qt's QQmlScriptData yet. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::ReturnedValue QQmlScriptData::scriptValueForContext(const
    QQmlRefPointer<QQmlContextData> &parentCtxt)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit>
    QQmlScriptData::compilationUnit() const': gives a type Python has no way
    to take yet.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 a template; 1 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QQmlScriptData is created at the first use, not by
    'QQmlScriptData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlScriptData.
  - Each name of Qt's QQmlScriptData that has no cute function yet,
    'compilationUnit', 'handleOwnScriptValueOrExecutableCU',
    'qmlContextDataForContext', 'scriptValueForContext', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlScriptData'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlScriptData::QQmlScriptData()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlscriptdata.html#QQmlScriptData
    """
    #  QQmlScriptData::QQmlScriptData()
    self._noteCreation(QQmlScriptData, lambda: Rituals.call(
        'ritual_ZN14QQmlScriptDataC1Ev',
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
  def compilationUnit(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit>
    QQmlScriptData::compilationUnit() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQmlScriptData.compilationUnit' has no cute function yet. Qt's "
        "'QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "QQmlScriptData::compilationUnit() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def handleOwnScriptValueOrExecutableCU(*__, **_) -> Never:
    """
    Qt's 'QQmlScriptData::handleOwnScriptValueOrExecutableCU': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlScriptData.handleOwnScriptValueOrExecutableCU' has no cute "
        "function yet. Qt's "
        "'QQmlScriptData::handleOwnScriptValueOrExecutableCU': a template: "
        "a pattern and no single function.")

  @staticmethod
  def qmlContextDataForContext(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlScriptData::qmlContextDataForContext(const
    QQmlRefPointer<QQmlContextData> &parentQmlContextData)': the compiler
    refuses its ritual as it would be written here: member access into
    incomplete type 'QQmlContextData'.
    """
    raise NotImplementedError(
        "'QQmlScriptData.qmlContextDataForContext' has no cute function "
        "yet. Qt's 'QQmlRefPointer<QQmlContextData> "
        "QQmlScriptData::qmlContextDataForContext(const "
        "QQmlRefPointer<QQmlContextData> &parentQmlContextData)': the "
        "compiler refuses its ritual as it would be written here: member "
        "access into incomplete type 'QQmlContextData'.")

  @staticmethod
  def scriptValueForContext(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlScriptData::scriptValueForContext(const
    QQmlRefPointer<QQmlContextData> &parentCtxt)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlScriptData.scriptValueForContext' has no cute function yet. "
        "Qt's 'QV4::ReturnedValue "
        "QQmlScriptData::scriptValueForContext(const "
        "QQmlRefPointer<QQmlContextData> &parentCtxt)': takes a type Python "
        "has no way to hand over yet.")
