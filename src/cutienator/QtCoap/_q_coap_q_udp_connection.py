"""
QCoapQUdpConnection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapqudpconnection_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCoapQUdpConnection to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtNetwork import QAbstractSocket
from . import QCoapConnection

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
  from ..QtNetwork import QSslPreSharedKeyAuthenticator, QUdpSocket
  from . import QCoapQUdpConnectionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoapQUdpConnection(QCoapConnection):
  """
  The cute side of Qt's QCoapQUdpConnection: a plain Python object standing
  in front of one C++ QCoapQUdpConnection.

  It is built on the cute 'QCoapConnection', as Qt's QCoapQUdpConnection is
  built on Qt's QCoapConnection, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapQUdpConnection that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'socket',
  'setSocketOption', 'pskRequired', 'handshakeTimeout', 'bind', 'writeData',
  'close', 'd_func'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCoapQUdpConnection::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QCoapQUdpConnection::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QCoapQUdpConnection::~QCoapQUdpConnection()': the destructor:
    Python never removes a C++ QCoapQUdpConnection.
  - Qt's 'const QCoapQUdpConnectionPrivate *QCoapQUdpConnection::d_func()
    const': takes in Python what 'QCoapQUdpConnectionPrivate
    *QCoapQUdpConnection::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 19 functions Qt declares: 3 leans on 'QCoapConnection; 2 not a
  gap; 1 leans on 'QCoapQUdpConnection.

  What to expect
  --------------

  - The C++ QCoapQUdpConnection is created at the first use, not by
    'QCoapQUdpConnection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapQUdpConnection.
  - Qt tells when it has removed the C++ QCoapQUdpConnection. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCoapQUdpConnection that has no cute function yet,
    '__init__', 'createSocket', holds a function that raises
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
  __qt_class__ = 'QCoapQUdpConnection'

  #  A C++ QCoapQUdpConnection Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoapQUdpConnection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCoapQUdpConnection::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapqudpconnection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCoapQUdpConnection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QCoapQUdpConnection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def socket(self) -> Optional[QUdpSocket]:
    """
    Calls Qt's 'QUdpSocket *QCoapQUdpConnection::socket() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapqudpconnection.html#socket

    Returns
    -------

    Optional[QUdpSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUdpSocket *QCoapQUdpConnection::socket() const
    address = self.uglySide.call('ritual_ZNK19QCoapQUdpConnection6socketEv')
    from ..QtNetwork import QUdpSocket
    return QUdpSocket._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractSocket.SocketOption, QVariant)
  def setSocketOption(
      self,
      a0: QAbstractSocket.SocketOption,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QCoapQUdpConnection::setSocketOption(QAbstractSocket::SocketOption a0,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapqudpconnection.html#setSocketOption

    Parameters
    ----------

    a0 : QAbstractSocket.SocketOption
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void
    #      QCoapQUdpConnection::setSocketOption(QAbstractSocket::SocketOption
    #      a0, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN19QCoapQUdpConnection15setSocketOptionEN15QAbstractSocket'
        '12SocketOptionERK8QVariant',
        a0.value, self._valueOf(value),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QCoapQUdpConnection::QCoapQUdpConnection(QtCoap::SecurityMode
      security, QObject *parent)': leans on
      'QCoapConnection::staticMetaObject', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    - Qt's
      'QCoapQUdpConnection::QCoapQUdpConnection(QCoapQUdpConnectionPrivate
      &dd, QObject *parent)': leans on 'QCoapConnection::staticMetaObject',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapQUdpConnection.__init__' has no cute function yet. Qt's "
        "'QCoapQUdpConnection::QCoapQUdpConnection(QtCoap::SecurityMode "
        "security, QObject *parent)': leans on "
        "'QCoapConnection::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken. Qt's "
        "'QCoapQUdpConnection::QCoapQUdpConnection(QCoapQUdpConnectionPrivat"
        "e &dd, QObject *parent)': leans on "
        "'QCoapConnection::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QSslPreSharedKeyAuthenticator)
  @overload(NoneType)
  def pskRequired(
      self,
      authenticator: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void
    QCoapQUdpConnection::pskRequired(QSslPreSharedKeyAuthenticator
    *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapqudpconnection.html#pskRequired

    Parameters
    ----------

    authenticator : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCoapQUdpConnection::pskRequired(QSslPreSharedKeyAuthenticator
    #      *authenticator)
    self.uglySide.call(
        'ritual_ZN19QCoapQUdpConnection11pskRequiredEP29QSslPreSharedKeyAut'
        'henticator',
        self._addressOf(authenticator),
    )

  def handshakeTimeout(self) -> None:
    """
    Calls Qt's 'void QCoapQUdpConnection::handshakeTimeout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapqudpconnection.html#handshakeTimeout
    """
    #  void QCoapQUdpConnection::handshakeTimeout()
    self.uglySide.call('ritual_ZN19QCoapQUdpConnection16handshakeTimeoutEv')

  @overload(str, int)
  def bind(self, host: str, port: int) -> None:
    """
    Calls Qt's 'void QCoapQUdpConnection::bind(const QString &host, quint16
    port)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapqudpconnection.html#bind

    Parameters
    ----------

    host : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.
    """
    #  void QCoapQUdpConnection::bind(const QString &host, quint16 port)
    self.uglySide.call(
        'ritual_ZN19QCoapQUdpConnection4bindERK7QStringt', host, port,
    )

  @overload(QByteArray, str, int)
  def writeData(self, data: QByteArray, host: str, port: int) -> None:
    """
    Calls Qt's 'void QCoapQUdpConnection::writeData(const QByteArray &data,
    const QString &host, quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapqudpconnection.html#writeData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    host : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.
    """
    #  void QCoapQUdpConnection::writeData(const QByteArray &data, const
    #      QString &host, quint16 port)
    ritual = (
        'ritual_ZN19QCoapQUdpConnection9writeDataERK10QByteArrayRK7QStringt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QCoapQUdpConnection9writeDataERK10QByteArrayRK7QS'
          'tringt')
    self.uglySide.call(ritual, self._valueOf(data), host, port)

  def close(self) -> None:
    """
    Calls Qt's 'void QCoapQUdpConnection::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapqudpconnection.html#close
    """
    #  void QCoapQUdpConnection::close()
    ritual = 'ritual_ZN19QCoapQUdpConnection5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QCoapQUdpConnection5closeEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QCoapQUdpConnectionPrivate]:
    """
    Calls Qt's 'QCoapQUdpConnectionPrivate *QCoapQUdpConnection::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapqudpconnection.html#d_func

    Returns
    -------

    Optional[QCoapQUdpConnectionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapQUdpConnectionPrivate *QCoapQUdpConnection::d_func()
    address = self.uglySide.call('ritual_ZN19QCoapQUdpConnection6d_funcEv')
    from . import QCoapQUdpConnectionPrivate
    return QCoapQUdpConnectionPrivate._cuteAt(address)

  @staticmethod
  def createSocket(*__, **_) -> Never:
    """
    Qt's 'void QCoapQUdpConnection::createSocket()': leans on
    'QCoapConnection::error(QAbstractSocket::SocketError)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QCoapQUdpConnection.createSocket' has no cute function yet. Qt's "
        "'void QCoapQUdpConnection::createSocket()': leans on "
        "'QCoapConnection::error(QAbstractSocket::SocketError)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
