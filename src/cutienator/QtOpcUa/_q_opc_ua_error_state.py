"""
QOpcUaErrorState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaerrorstate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QOpcUa


class QOpcUaErrorState(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaErrorState: a plain Python object standing in
  front of one C++ QOpcUaErrorState.

  C++ hands a QOpcUaErrorState around as a copy, so every C++
  QOpcUaErrorState behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaErrorState that has a ritual and that Python
  can call so far, 8 names in all: 'connectionStep', 'setConnectionStep',
  'errorCode', 'setErrorCode', 'isClientSideError', 'setClientSideError',
  'setIgnoreError', 'ignoreError'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaErrorState &QOpcUaErrorState::operator=(const
    QOpcUaErrorState &rhs)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QOpcUaErrorState::~QOpcUaErrorState()': the destructor: Python
    removes its C++ QOpcUaErrorState by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaErrorState is created at the first use, not by
    'QOpcUaErrorState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaErrorState back gives a copy the ritual made
    for Python, in a new cute QOpcUaErrorState.
  """

  #  The enums Qt writes inside QOpcUaErrorState, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ConnectionStep(CuteNum, scoped=True):
    """
    The enum 'QOpcUaErrorState::ConnectionStep' of Qt, with the 5 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Unknown = Kee[int](0)
    CertificateValidation = Kee[int](1)
    OpenSecureChannel = Kee[int](2)
    CreateSession = Kee[int](3)
    ActivateSession = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaErrorState'

  #  Qt's '~QOpcUaErrorState()'. Naming it makes this a value class: Python
  #  owns every C++ QOpcUaErrorState behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QOpcUaErrorStateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def connectionStep(self) -> ConnectionStep:
    """
    Calls Qt's 'ConnectionStep QOpcUaErrorState::connectionStep() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaerrorstate.html#connectionStep

    Returns
    -------

    ConnectionStep
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ConnectionStep(number)'
      gives.
    """
    #  ConnectionStep QOpcUaErrorState::connectionStep() const
    return QOpcUaErrorState.ConnectionStep(self.uglySide.call(
        'ritual_ZNK16QOpcUaErrorState14connectionStepEv',
    ))

  def errorCode(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode QOpcUaErrorState::errorCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaerrorstate.html#errorCode

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaErrorState::errorCode() const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK16QOpcUaErrorState9errorCodeEv',
    ))

  def isClientSideError(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaErrorState::isClientSideError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaerrorstate.html#isClientSideError
    """
    #  bool QOpcUaErrorState::isClientSideError() const
    return self.uglySide.call(
        'ritual_ZNK16QOpcUaErrorState17isClientSideErrorEv',
    )

  def ignoreError(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaErrorState::ignoreError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaerrorstate.html#ignoreError
    """
    #  bool QOpcUaErrorState::ignoreError() const
    return self.uglySide.call('ritual_ZNK16QOpcUaErrorState11ignoreErrorEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ConnectionStep)
  def setConnectionStep(self, step: ConnectionStep) -> None:
    """
    Calls Qt's 'void QOpcUaErrorState::setConnectionStep(ConnectionStep
    step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaerrorstate.html#setConnectionStep

    Parameters
    ----------

    step : ConnectionStep
      Passed on as its number.
    """
    #  void QOpcUaErrorState::setConnectionStep(ConnectionStep step)
    self.uglySide.call(
        'ritual_ZN16QOpcUaErrorState17setConnectionStepENS_14ConnectionStep'
        'E',
        step.value,
    )

  @overload(QOpcUa.UaStatusCode)
  def setErrorCode(self, error: QOpcUa.UaStatusCode) -> None:
    """
    Calls Qt's 'void QOpcUaErrorState::setErrorCode(QOpcUa::UaStatusCode
    error)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaerrorstate.html#setErrorCode

    Parameters
    ----------

    error : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaErrorState::setErrorCode(QOpcUa::UaStatusCode error)
    self.uglySide.call(
        'ritual_ZN16QOpcUaErrorState12setErrorCodeEN6QOpcUa12UaStatusCodeE',
        error.value,
    )

  @overload(bool)
  def setClientSideError(self, clientSideError: bool) -> None:
    """
    Calls Qt's 'void QOpcUaErrorState::setClientSideError(bool
    clientSideError)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaerrorstate.html#setClientSideError

    Parameters
    ----------

    clientSideError : bool
      Passed on as it is.
    """
    #  void QOpcUaErrorState::setClientSideError(bool clientSideError)
    self.uglySide.call(
        'ritual_ZN16QOpcUaErrorState18setClientSideErrorEb', clientSideError,
    )

  @overload()
  @overload(bool)
  def setIgnoreError(self, ignore: bool = True) -> None:
    """
    Calls Qt's 'void QOpcUaErrorState::setIgnoreError(bool ignore)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaerrorstate.html#setIgnoreError

    Parameters
    ----------

    ignore : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QOpcUaErrorState::setIgnoreError(bool ignore)
    self.uglySide.call(
        'ritual_ZN16QOpcUaErrorState14setIgnoreErrorEb', ignore,
    )

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
    Notes what was given, for Qt's 'QOpcUaErrorState::QOpcUaErrorState()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaerrorstate.html#QOpcUaErrorState
    """
    #  QOpcUaErrorState::QOpcUaErrorState()
    self._noteCreation(QOpcUaErrorState, lambda: Rituals.call(
        'ritual_ZN16QOpcUaErrorStateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaErrorState) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaErrorState::QOpcUaErrorState(const
    QOpcUaErrorState &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaerrorstate.html#QOpcUaErrorState

    Parameters
    ----------

    other : QOpcUaErrorState
      Passed on as a value: Qt reads the C++ QOpcUaErrorState, which stays
      Python's own.
    """
    #  QOpcUaErrorState::QOpcUaErrorState(const QOpcUaErrorState &other)
    self._noteCreation(QOpcUaErrorState, lambda: Rituals.call(
        'ritual_ZN16QOpcUaErrorStateC1ERKS_', self._valueOf(other),
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
