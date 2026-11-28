"""
QLocalSocketPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qlocalsocket_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLocalSocketPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QIODevicePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLocalSocket


class QLocalSocketPrivate(QIODevicePrivate):
  """
  The cute side of Qt's QLocalSocketPrivate: a plain Python object standing
  in front of one C++ QLocalSocketPrivate.

  It is built on the cute 'QIODevicePrivate', as Qt's QLocalSocketPrivate is
  built on Qt's QIODevicePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLocalSocketPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'q_func',
  '_q_abortConnectionAttempt', 'cancelDelayedConnect', 'describeSocket',
  '_qt_property_socketOptions_offset'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QLocalSocket *QLocalSocketPrivate::q_func() const': takes in
    Python what 'QLocalSocket *QLocalSocketPrivate::q_func()' takes.
  - Qt's 'bool QLocalSocketPrivate::parseSockaddr(const sockaddr_un &addr,
    uint len, QString &fullServerName, QString &serverName, bool
    &abstractNamespace)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  7 of the 14 functions Qt declares: 6 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 leans on
  'QLocalSocketPrivate.

  What to expect
  --------------

  - The C++ QLocalSocketPrivate is created at the first use, not by
    'QLocalSocketPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLocalSocketPrivate.
  - Each name of Qt's QLocalSocketPrivate that has no cute function yet,
    '__init__', '_q_connectToSocket', '_q_errorOccurred', '_q_stateChanged',
    'generateErrorString', 'init', 'parseSockaddr', 'setErrorAndEmit', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _qt_property_socketOptions_offset() -> int:
    """
    Calls Qt's 'size_t
    QLocalSocketPrivate::_qt_property_socketOptions_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalsocketprivate.html
    """
    #  size_t QLocalSocketPrivate::_qt_property_socketOptions_offset()
    return Rituals.call(
        'ritual_ZN19QLocalSocketPrivate33_qt_property_socketOptions_offsetE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLocalSocketPrivate'

  #  A C++ QLocalSocketPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLocalSocketPrivate'

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
    Qt's 'QLocalSocketPrivate::QLocalSocketPrivate()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLocalSocketPrivate.__init__' has no cute function yet. Qt's "
        "'QLocalSocketPrivate::QLocalSocketPrivate()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

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

  def q_func(self) -> Optional[QLocalSocket]:
    """
    Calls Qt's 'QLocalSocket *QLocalSocketPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlocalsocketprivate.html#q_func

    Returns
    -------

    Optional[QLocalSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLocalSocket *QLocalSocketPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QLocalSocketPrivate6q_funcEv')
    from . import QLocalSocket
    return QLocalSocket._cuteAt(address)

  def _q_abortConnectionAttempt(self) -> None:
    """
    Calls Qt's 'void QLocalSocketPrivate::_q_abortConnectionAttempt()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalsocketprivate.html#_q_abortConnectionAttempt
    """
    #  void QLocalSocketPrivate::_q_abortConnectionAttempt()
    self.uglySide.call(
        'ritual_ZN19QLocalSocketPrivate25_q_abortConnectionAttemptEv',
    )

  def cancelDelayedConnect(self) -> None:
    """
    Calls Qt's 'void QLocalSocketPrivate::cancelDelayedConnect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalsocketprivate.html#cancelDelayedConnect
    """
    #  void QLocalSocketPrivate::cancelDelayedConnect()
    self.uglySide.call(
        'ritual_ZN19QLocalSocketPrivate20cancelDelayedConnectEv',
    )

  @overload(int)
  def describeSocket(self, socketDescriptor: int) -> None:
    """
    Calls Qt's 'void QLocalSocketPrivate::describeSocket(qintptr
    socketDescriptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlocalsocketprivate.html#describeSocket

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.
    """
    #  void QLocalSocketPrivate::describeSocket(qintptr socketDescriptor)
    self.uglySide.call(
        'ritual_ZN19QLocalSocketPrivate14describeSocketEx', socketDescriptor,
    )

  @staticmethod
  def _q_connectToSocket(*__, **_) -> Never:
    """
    Qt's 'void QLocalSocketPrivate::_q_connectToSocket()': leans on
    'QLocalSocketPrivate::setErrorAndEmit(QLocalSocket::LocalSocketError,
    QString const&)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLocalSocketPrivate._q_connectToSocket' has no cute function yet. "
        "Qt's 'void QLocalSocketPrivate::_q_connectToSocket()': leans on "
        "'QLocalSocketPrivate::setErrorAndEmit(QLocalSocket::LocalSocketErro"
        "r, QString const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_errorOccurred(*__, **_) -> Never:
    """
    Qt's 'void
    QLocalSocketPrivate::_q_errorOccurred(QAbstractSocket::SocketError
    newError)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLocalSocketPrivate._q_errorOccurred' has no cute function yet. "
        "Qt's 'void "
        "QLocalSocketPrivate::_q_errorOccurred(QAbstractSocket::SocketError "
        "newError)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def _q_stateChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QLocalSocketPrivate::_q_stateChanged(QAbstractSocket::SocketState
    newState)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLocalSocketPrivate._q_stateChanged' has no cute function yet. "
        "Qt's 'void "
        "QLocalSocketPrivate::_q_stateChanged(QAbstractSocket::SocketState "
        "newState)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def generateErrorString(*__, **_) -> Never:
    """
    Qt's 'QString
    QLocalSocketPrivate::generateErrorString(QLocalSocket::LocalSocketError
    a0, const QString &function) const': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLocalSocketPrivate.generateErrorString' has no cute function "
        "yet. Qt's 'QString "
        "QLocalSocketPrivate::generateErrorString(QLocalSocket::LocalSocketE"
        "rror a0, const QString &function) const': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QLocalSocketPrivate::init()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLocalSocketPrivate.init' has no cute function yet. Qt's 'void "
        "QLocalSocketPrivate::init()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def parseSockaddr(*__, **_) -> Never:
    """
    Qt's 'bool QLocalSocketPrivate::parseSockaddr(const sockaddr_un &addr,
    uint len, QString &fullServerName, QString &serverName, bool
    &abstractNamespace)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLocalSocketPrivate.parseSockaddr' has no cute function yet. Qt's "
        "'bool QLocalSocketPrivate::parseSockaddr(const sockaddr_un &addr, "
        "uint len, QString &fullServerName, QString &serverName, bool "
        "&abstractNamespace)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setErrorAndEmit(*__, **_) -> Never:
    """
    Qt's 'void
    QLocalSocketPrivate::setErrorAndEmit(QLocalSocket::LocalSocketError a0,
    const QString &function)': cannot be called and cannot be called through
    the meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLocalSocketPrivate.setErrorAndEmit' has no cute function yet. "
        "Qt's 'void "
        "QLocalSocketPrivate::setErrorAndEmit(QLocalSocket::LocalSocketError"
        " a0, const QString &function)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")
