"""
QQmlJSCompileError binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompiler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSCompileError to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtQml import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlJSCompileError(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSCompileError: a plain Python object standing in
  front of one C++ QQmlJSCompileError.

  C++ hands a QQmlJSCompileError around as a copy, so every C++
  QQmlJSCompileError behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSCompileError that has a ritual and that Python
  can call so far, 3 names in all: 'print', 'augment', 'appendDiagnostic'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJSCompileError::appendDiagnostics(const QString
    &inputFileName, const QList<QQmlJS::DiagnosticMessage> &diagnostics)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSCompileError::~QQmlJSCompileError()': the destructor: Python
    removes its C++ QQmlJSCompileError by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJSCompileError is created at the first use, not by
    'QQmlJSCompileError(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSCompileError back gives a copy the ritual made
    for Python, in a new cute QQmlJSCompileError.
  - Each name of Qt's QQmlJSCompileError that has no cute function yet,
    'appendDiagnostics', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSCompileError'

  #  Qt's '~QQmlJSCompileError()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJSCompileError behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlJSCompileErrorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def augment(self, contextErrorMessage: str) -> QQmlJSCompileError:
    """
    Calls Qt's 'QQmlJSCompileError QQmlJSCompileError::augment(const QString
    &contextErrorMessage) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljscompileerror.html#augment

    Parameters
    ----------

    contextErrorMessage : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlJSCompileError
      A new cute QQmlJSCompileError around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSCompileError QQmlJSCompileError::augment(const QString
    #      &contextErrorMessage) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSCompileError7augmentERK7QString',
        contextErrorMessage,
    )
    return QQmlJSCompileError._cuteOwning(address)

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

  def print(self) -> None:
    """
    Calls Qt's 'void QQmlJSCompileError::print()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljscompileerror.html#print
    """
    #  void QQmlJSCompileError::print()
    self.uglySide.call('ritual_ZN18QQmlJSCompileError5printEv')

  @overload(str, WAIT['QQmlJS.DiagnosticMessage'])
  def appendDiagnostic(
      self,
      inputFileName: str,
      diagnostic: QQmlJS.DiagnosticMessage,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCompileError::appendDiagnostic(const QString
    &inputFileName, const QQmlJS::DiagnosticMessage &diagnostic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscompileerror.html#appendDiagnostic

    Parameters
    ----------

    inputFileName : str
      Passed on as it is: a QString is made of it for the call.

    diagnostic : QQmlJS.DiagnosticMessage
      Passed on as a value: Qt reads the C++ QQmlJS::DiagnosticMessage, which
      stays Python's own.
    """
    #  void QQmlJSCompileError::appendDiagnostic(const QString
    #      &inputFileName, const QQmlJS::DiagnosticMessage &diagnostic)
    self.uglySide.call(
        'ritual_ZN18QQmlJSCompileError16appendDiagnosticERK7QStringRKN6QQml'
        'JS17DiagnosticMessageE',
        inputFileName, self._valueOf(diagnostic),
    )

  @staticmethod
  def appendDiagnostics(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSCompileError::appendDiagnostics(const QString
    &inputFileName, const QList<QQmlJS::DiagnosticMessage> &diagnostics)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCompileError.appendDiagnostics' has no cute function yet. "
        "Qt's 'void QQmlJSCompileError::appendDiagnostics(const QString "
        "&inputFileName, const QList<QQmlJS::DiagnosticMessage> "
        "&diagnostics)': takes a type Python has no way to hand over yet.")
