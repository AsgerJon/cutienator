"""
QSystemError binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsystemerror_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSystemError to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QSystemError(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSystemError: a plain Python object standing in front
  of one C++ QSystemError.

  C++ hands a QSystemError around as a copy, so every C++ QSystemError behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSystemError that has a ritual and that Python can
  call so far, 7 names in all: 'toString', 'scope', 'error', 'ok',
  'stdError', 'string', 'stdString'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSystemError::~QSystemError()': the destructor: Python removes its
    C++ QSystemError by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSystemError is created at the first use, not by
    'QSystemError(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSystemError back gives a copy the ritual made for
    Python, in a new cute QSystemError.
  """

  #  The enums Qt writes inside QSystemError, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ErrorScope(CuteNum):
    """
    The enum 'QSystemError::ErrorScope' of Qt, with the 3 names Qt gives in
    it.
    """

    NoError = Kee[int](0)
    StandardLibraryError = Kee[int](1)
    NativeError = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def stdError(error: int) -> QSystemError:
    """
    Calls Qt's 'QSystemError QSystemError::stdError(int error)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemerror.html#stdError

    Parameters
    ----------

    error : int
      Passed on as it is.

    Returns
    -------

    QSystemError
      A new cute QSystemError around the copy Qt gave back. Python owns it.
    """
    #  QSystemError QSystemError::stdError(int error)
    address = Rituals.call('ritual_ZN12QSystemError8stdErrorEi', error)
    return QSystemError._cuteOwning(address)

  @staticmethod
  @overload(ErrorScope, int)
  def string(errorScope: ErrorScope, errorCode: int) -> str:
    """
    Calls Qt's 'QString QSystemError::string(ErrorScope errorScope, int
    errorCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemerror.html#string

    Parameters
    ----------

    errorScope : ErrorScope
      Passed on as its number.

    errorCode : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSystemError::string(ErrorScope errorScope, int errorCode)
    return Rituals.call(
        'ritual_ZN12QSystemError6stringENS_10ErrorScopeEi',
        errorScope.value, errorCode,
    )

  @staticmethod
  @overload()
  @overload(int)
  def stdString(errorCode: int = -1) -> str:
    """
    Calls Qt's 'QString QSystemError::stdString(int errorCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemerror.html#stdString

    Parameters
    ----------

    errorCode : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSystemError::stdString(int errorCode)
    return Rituals.call('ritual_ZN12QSystemError9stdStringEi', errorCode)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSystemError'

  #  Qt's '~QSystemError()'. Naming it makes this a value class: Python owns
  #  every C++ QSystemError behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QSystemErrorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QSystemError::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemerror.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSystemError::toString() const
    return self.uglySide.call('ritual_ZNK12QSystemError8toStringEv')

  def scope(self) -> ErrorScope:
    """
    Calls Qt's 'ErrorScope QSystemError::scope() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemerror.html#scope

    Returns
    -------

    ErrorScope
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ErrorScope(number)'
      gives.
    """
    #  ErrorScope QSystemError::scope() const
    return QSystemError.ErrorScope(self.uglySide.call(
        'ritual_ZNK12QSystemError5scopeEv',
    ))

  def error(self) -> int:
    """
    Calls Qt's 'int QSystemError::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemerror.html#error
    """
    #  int QSystemError::error() const
    return self.uglySide.call('ritual_ZNK12QSystemError5errorEv')

  def ok(self) -> bool:
    """
    Calls Qt's 'bool QSystemError::ok() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsystemerror.html#ok
    """
    #  bool QSystemError::ok() const
    return self.uglySide.call('ritual_ZNK12QSystemError2okEv')

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

  @overload(int, ErrorScope)
  def __init__(self, error: int, scope: ErrorScope) -> None:
    """
    Notes what was given, for Qt's 'QSystemError::QSystemError(int error,
    ErrorScope scope)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsystemerror.html#QSystemError

    Parameters
    ----------

    error : int
      Passed on as it is.

    scope : ErrorScope
      Passed on as its number.
    """
    #  QSystemError::QSystemError(int error, ErrorScope scope)
    self._noteCreation(QSystemError, lambda: Rituals.call(
        'ritual_ZN12QSystemErrorC1EiNS_10ErrorScopeE', error, scope.value,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSystemError::QSystemError()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsystemerror.html#QSystemError
    """
    #  QSystemError::QSystemError()
    self._noteCreation(QSystemError, lambda: Rituals.call(
        'ritual_ZN12QSystemErrorC1Ev',
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
