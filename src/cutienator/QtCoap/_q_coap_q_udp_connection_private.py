"""
QCoapQUdpConnectionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapqudpconnection_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCoapQUdpConnectionPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QtCoap, QCoapConnectionPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from ..QtNetwork import QNetworkDatagram, QUdpSocket
  from . import QCoapQUdpConnection, QCoapSecurityConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCoapSecurityConfiguration = WAIT['QCoapSecurityConfiguration']
  QNetworkDatagram = WAIT['QNetworkDatagram']


class QCoapQUdpConnectionPrivate(QCoapConnectionPrivate):
  """
  The cute side of Qt's QCoapQUdpConnectionPrivate: a plain Python object
  standing in front of one C++ QCoapQUdpConnectionPrivate.

  It is built on the cute 'QCoapConnectionPrivate', as Qt's
  QCoapQUdpConnectionPrivate is built on Qt's QCoapConnectionPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapQUdpConnectionPrivate that has a ritual and
  that Python can call so far, 6 names in all: 'bind', 'writeToSocket',
  'socket', 'setSecurityConfiguration', 'datagramMatchesNetworkInterface',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoapQUdpConnectionPrivate::~QCoapQUdpConnectionPrivate()': the
    destructor: Python never removes a C++ QCoapQUdpConnectionPrivate.
  - Qt's 'std::optional<QNetworkDatagram>
    QCoapQUdpConnectionPrivate::receiveDatagramDecrypted() const': gives a
    type Python has no way to take yet.
  - Qt's 'const QCoapQUdpConnection *QCoapQUdpConnectionPrivate::q_func()
    const': takes in Python what 'QCoapQUdpConnection
    *QCoapQUdpConnectionPrivate::q_func()' takes.

  What has no ritual
  ------------------

  3 of the 13 functions Qt declares: 3 leans on 'QCoapConnection.

  What to expect
  --------------

  - The C++ QCoapQUdpConnectionPrivate is created at the first use, not by
    'QCoapQUdpConnectionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapQUdpConnectionPrivate.
  - Each name of Qt's QCoapQUdpConnectionPrivate that has no cute function
    yet, 'bindSocket', 'handleEncryptedDatagram', 'receiveDatagramDecrypted',
    'socketReadyRead', holds a function that raises 'NotImplementedError',
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
  __qt_class__ = 'QCoapQUdpConnectionPrivate'

  #  A C++ QCoapQUdpConnectionPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoapQUdpConnectionPrivate'

  #  The functions Qt calls itself that QCoapQUdpConnectionPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'bind': (
          ('_ZN26QCoapQUdpConnectionPrivate4bindEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def socket(self) -> Optional[QUdpSocket]:
    """
    Calls Qt's 'QUdpSocket *QCoapQUdpConnectionPrivate::socket() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapqudpconnectionprivate.html#socket

    Returns
    -------

    Optional[QUdpSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUdpSocket *QCoapQUdpConnectionPrivate::socket() const
    address = self.uglySide.call(
        'ritual_ZNK26QCoapQUdpConnectionPrivate6socketEv',
    )
    from ..QtNetwork import QUdpSocket
    return QUdpSocket._cuteAt(address)

  @overload(QNetworkDatagram)
  def datagramMatchesNetworkInterface(
      self,
      datagram: QNetworkDatagram,
  ) -> bool:
    """
    Calls Qt's 'bool
    QCoapQUdpConnectionPrivate::datagramMatchesNetworkInterface(const
    QNetworkDatagram &datagram) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapqudpconnectionprivate.html

    Parameters
    ----------

    datagram : QNetworkDatagram
      Passed on as a value: Qt reads the C++ QNetworkDatagram, which stays
      Python's own.
    """
    #  bool QCoapQUdpConnectionPrivate::datagramMatchesNetworkInterface(const
    #      QNetworkDatagram &datagram) const
    return self.uglySide.call(
        'ritual_ZNK26QCoapQUdpConnectionPrivate31datagramMatchesNetworkInte'
        'rfaceERK16QNetworkDatagram',
        self._valueOf(datagram),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCoapSecurityConfiguration)
  def setSecurityConfiguration(
      self,
      configuration: QCoapSecurityConfiguration,
  ) -> None:
    """
    Calls Qt's 'void
    QCoapQUdpConnectionPrivate::setSecurityConfiguration(const
    QCoapSecurityConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapqudpconnectionprivate.html

    Parameters
    ----------

    configuration : QCoapSecurityConfiguration
      Passed on as a value: Qt reads the C++ QCoapSecurityConfiguration,
      which stays Python's own.
    """
    #  void QCoapQUdpConnectionPrivate::setSecurityConfiguration(const
    #      QCoapSecurityConfiguration &configuration)
    self.uglySide.call(
        'ritual_ZN26QCoapQUdpConnectionPrivate24setSecurityConfigurationERK'
        '26QCoapSecurityConfiguration',
        self._valueOf(configuration),
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
  @overload(QtCoap.SecurityMode)
  def __init__(
      self,
      security: QtCoap.SecurityMode = QtCoap.SecurityMode.NoSecurity,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCoapQUdpConnectionPrivate::QCoapQUdpConnectionPrivate(QtCoap::
    SecurityMode security)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapqudpconnectionprivate.html

    Parameters
    ----------

    security : QtCoap.SecurityMode
      Passed on as its number. May be left out, as in Qt: it is then
      QtCoap.SecurityMode.NoSecurity.
    """
    #  QCoapQUdpConnectionPrivate::QCoapQUdpConnectionPrivate(QtCoap::
    #      SecurityMode security)
    self._noteCreation(QCoapQUdpConnectionPrivate, lambda: Rituals.call(
        'ritual_ZN26QCoapQUdpConnectionPrivateC1EN6QtCoap12SecurityModeE',
        security.value,
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

  def bind(self) -> bool:
    """
    Calls Qt's 'bool QCoapQUdpConnectionPrivate::bind()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapqudpconnectionprivate.html#bind
    """
    #  bool QCoapQUdpConnectionPrivate::bind()
    ritual = 'ritual_ZN26QCoapQUdpConnectionPrivate4bindEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QCoapQUdpConnectionPrivate4bindEv'
    return self.uglySide.call(ritual)

  @overload(QByteArray, str, int)
  def writeToSocket(self, data: QByteArray, host: str, port: int) -> None:
    """
    Calls Qt's 'void QCoapQUdpConnectionPrivate::writeToSocket(const
    QByteArray &data, const QString &host, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapqudpconnectionprivate.html#writeToSocket

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
    #  void QCoapQUdpConnectionPrivate::writeToSocket(const QByteArray &data,
    #      const QString &host, quint16 port)
    self.uglySide.call(
        'ritual_ZN26QCoapQUdpConnectionPrivate13writeToSocketERK10QByteArra'
        'yRK7QStringt',
        self._valueOf(data), host, port,
    )

  def q_func(self) -> Optional[QCoapQUdpConnection]:
    """
    Calls Qt's 'QCoapQUdpConnection *QCoapQUdpConnectionPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapqudpconnectionprivate.html#q_func

    Returns
    -------

    Optional[QCoapQUdpConnection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapQUdpConnection *QCoapQUdpConnectionPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QCoapQUdpConnectionPrivate6q_funcEv',
    )
    from . import QCoapQUdpConnection
    return QCoapQUdpConnection._cuteAt(address)

  @staticmethod
  def bindSocket(*__, **_) -> Never:
    """
    Qt's 'void QCoapQUdpConnectionPrivate::bindSocket()': leans on
    'QCoapConnection::bound()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapQUdpConnectionPrivate.bindSocket' has no cute function yet. "
        "Qt's 'void QCoapQUdpConnectionPrivate::bindSocket()': leans on "
        "'QCoapConnection::bound()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def handleEncryptedDatagram(*__, **_) -> Never:
    """
    Qt's 'void QCoapQUdpConnectionPrivate::handleEncryptedDatagram()': leans
    on 'QCoapConnection::bound()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapQUdpConnectionPrivate.handleEncryptedDatagram' has no cute "
        "function yet. Qt's 'void "
        "QCoapQUdpConnectionPrivate::handleEncryptedDatagram()': leans on "
        "'QCoapConnection::bound()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def receiveDatagramDecrypted(*__, **_) -> Never:
    """
    Qt's 'std::optional<QNetworkDatagram>
    QCoapQUdpConnectionPrivate::receiveDatagramDecrypted() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCoapQUdpConnectionPrivate.receiveDatagramDecrypted' has no cute "
        "function yet. Qt's 'std::optional<QNetworkDatagram> "
        "QCoapQUdpConnectionPrivate::receiveDatagramDecrypted() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def socketReadyRead(*__, **_) -> Never:
    """
    Qt's 'void QCoapQUdpConnectionPrivate::socketReadyRead()': leans on
    'QCoapConnection::bound()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapQUdpConnectionPrivate.socketReadyRead' has no cute function "
        "yet. Qt's 'void QCoapQUdpConnectionPrivate::socketReadyRead()': "
        "leans on 'QCoapConnection::bound()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
