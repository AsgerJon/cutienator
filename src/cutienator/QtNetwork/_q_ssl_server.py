"""
QSslServer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qsslserver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QSsl, QAbstractSocket, QTcpServer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QSslConfiguration, QSslError, QSslPreSharedKeyAuthenticator
  from . import QSslServerPrivate, QSslSocket
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']
  QSslSocket = WAIT['QSslSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSslServer(QTcpServer):
  """
  The cute side of Qt's QSslServer: a plain Python object standing in front
  of one C++ QSslServer.

  It is built on the cute 'QTcpServer', as Qt's QSslServer is built on Qt's
  QTcpServer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSslServer that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'setSslConfiguration',
  'sslConfiguration', 'setHandshakeTimeout', 'handshakeTimeout', 'sslErrors',
  'peerVerifyError', 'errorOccurred', 'preSharedKeyAuthenticationRequired',
  'alertSent', 'alertReceived', 'handshakeInterruptedOnError',
  'startedEncryptionHandshake', 'incomingConnection', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSslServer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSslServer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSslServer::~QSslServer()': the destructor: Python never removes a
    C++ QSslServer.
  - Qt's 'const QSslServerPrivate *QSslServer::d_func() const': takes in
    Python what 'QSslServerPrivate *QSslServer::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 27 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QSslServer is created at the first use, not by 'QSslServer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSslServer.
  - Qt tells when it has removed the C++ QSslServer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QSslServer::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslserver.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslServer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QSslServer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslServer'

  #  A C++ QSslServer Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSslServer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSslServer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslserver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSslServer::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QSslServer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QSslServer::sslConfiguration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslserver.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QSslServer::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK10QSslServer16sslConfigurationEv',
    )
    from . import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  def handshakeTimeout(self) -> int:
    """
    Calls Qt's 'int QSslServer::handshakeTimeout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslserver.html#handshakeTimeout
    """
    #  int QSslServer::handshakeTimeout() const
    return self.uglySide.call('ritual_ZNK10QSslServer16handshakeTimeoutEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSslConfiguration)
  def setSslConfiguration(self, sslConfiguration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QSslServer::setSslConfiguration(const QSslConfiguration
    &sslConfiguration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslserver.html#setSslConfiguration

    Parameters
    ----------

    sslConfiguration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QSslServer::setSslConfiguration(const QSslConfiguration
    #      &sslConfiguration)
    self.uglySide.call(
        'ritual_ZN10QSslServer19setSslConfigurationERK17QSslConfiguration',
        self._valueOf(sslConfiguration),
    )

  @overload(int)
  def setHandshakeTimeout(self, timeout: int) -> None:
    """
    Calls Qt's 'void QSslServer::setHandshakeTimeout(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslserver.html#setHandshakeTimeout

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void QSslServer::setHandshakeTimeout(int timeout)
    self.uglySide.call(
        'ritual_ZN10QSslServer19setHandshakeTimeoutEi', timeout,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSslServer::QSslServer(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslserver.html#QSslServer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSslServer::QSslServer(QObject *parent)
    self._noteCreation(QSslServer, lambda: Rituals.call(
        'ritual_ZN10QSslServerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QSslSocket, QList[QSslError])
  @overload(NoneType, QList[QSslError])
  def sslErrors(
      self,
      socket: Optional[QSslSocket],
      errors: QList[QSslError],
  ) -> None:
    """
    Calls Qt's 'void QSslServer::sslErrors(QSslSocket *socket, const
    QList<QSslError> &errors)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslserver.html#sslErrors

    Parameters
    ----------

    socket : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslServer::sslErrors(QSslSocket *socket, const QList<QSslError>
    #      &errors)
    self.uglySide.call(
        'ritual_ZN10QSslServer9sslErrorsEP10QSslSocketRK5QListI9QSslErrorE',
        self._addressOf(socket), self._valueOf(errors),
    )

  @overload(QSslSocket, QSslError)
  @overload(NoneType, QSslError)
  def peerVerifyError(
      self,
      socket: Optional[QSslSocket],
      error: QSslError,
  ) -> None:
    """
    Calls Qt's 'void QSslServer::peerVerifyError(QSslSocket *socket, const
    QSslError &error)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslserver.html#peerVerifyError

    Parameters
    ----------

    socket : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    error : QSslError
      Passed on as a value: Qt reads the C++ QSslError, which stays Python's
      own.
    """
    #  void QSslServer::peerVerifyError(QSslSocket *socket, const QSslError
    #      &error)
    self.uglySide.call(
        'ritual_ZN10QSslServer15peerVerifyErrorEP10QSslSocketRK9QSslError',
        self._addressOf(socket), self._valueOf(error),
    )

  @overload(QSslSocket, QAbstractSocket.SocketError)
  @overload(NoneType, QAbstractSocket.SocketError)
  def errorOccurred(
      self,
      socket: Optional[QSslSocket],
      error: QAbstractSocket.SocketError,
  ) -> None:
    """
    Calls Qt's 'void QSslServer::errorOccurred(QSslSocket *socket,
    QAbstractSocket::SocketError error)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslserver.html#errorOccurred

    Parameters
    ----------

    socket : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    error : QAbstractSocket.SocketError
      Passed on as its number.
    """
    #  void QSslServer::errorOccurred(QSslSocket *socket,
    #      QAbstractSocket::SocketError error)
    self.uglySide.call(
        'ritual_ZN10QSslServer13errorOccurredEP10QSslSocketN15QAbstractSock'
        'et11SocketErrorE',
        self._addressOf(socket), error.value,
    )

  @overload(QSslSocket, QSslPreSharedKeyAuthenticator)
  @overload(QSslSocket, NoneType)
  @overload(NoneType, QSslPreSharedKeyAuthenticator)
  @overload(NoneType, NoneType)
  def preSharedKeyAuthenticationRequired(
      self,
      socket: Optional[QSslSocket],
      authenticator: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void
    QSslServer::preSharedKeyAuthenticationRequired(QSslSocket *socket,
    QSslPreSharedKeyAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslserver.html#preSharedKeyAuthenticationRequired

    Parameters
    ----------

    socket : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    authenticator : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSslServer::preSharedKeyAuthenticationRequired(QSslSocket
    #      *socket, QSslPreSharedKeyAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN10QSslServer34preSharedKeyAuthenticationRequiredEP10QSslS'
        'ocketP29QSslPreSharedKeyAuthenticator',
        self._addressOf(socket), self._addressOf(authenticator),
    )

  @overload(QSslSocket, QSsl.AlertLevel, QSsl.AlertType, str)
  @overload(NoneType, QSsl.AlertLevel, QSsl.AlertType, str)
  def alertSent(
      self,
      socket: Optional[QSslSocket],
      level: QSsl.AlertLevel,
      type: QSsl.AlertType,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QSslServer::alertSent(QSslSocket *socket,
    QSsl::AlertLevel level, QSsl::AlertType type, const QString
    &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslserver.html#alertSent

    Parameters
    ----------

    socket : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    level : QSsl.AlertLevel
      Passed on as its number.

    type : QSsl.AlertType
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSslServer::alertSent(QSslSocket *socket, QSsl::AlertLevel level,
    #      QSsl::AlertType type, const QString &description)
    self.uglySide.call(
        'ritual_ZN10QSslServer9alertSentEP10QSslSocketN4QSsl10AlertLevelENS'
        '2_9AlertTypeERK7QString',
        self._addressOf(socket), level.value, type.value, description,
    )

  @overload(QSslSocket, QSsl.AlertLevel, QSsl.AlertType, str)
  @overload(NoneType, QSsl.AlertLevel, QSsl.AlertType, str)
  def alertReceived(
      self,
      socket: Optional[QSslSocket],
      level: QSsl.AlertLevel,
      type: QSsl.AlertType,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QSslServer::alertReceived(QSslSocket *socket,
    QSsl::AlertLevel level, QSsl::AlertType type, const QString
    &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslserver.html#alertReceived

    Parameters
    ----------

    socket : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    level : QSsl.AlertLevel
      Passed on as its number.

    type : QSsl.AlertType
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSslServer::alertReceived(QSslSocket *socket, QSsl::AlertLevel
    #      level, QSsl::AlertType type, const QString &description)
    self.uglySide.call(
        'ritual_ZN10QSslServer13alertReceivedEP10QSslSocketN4QSsl10AlertLev'
        'elENS2_9AlertTypeERK7QString',
        self._addressOf(socket), level.value, type.value, description,
    )

  @overload(QSslSocket, QSslError)
  @overload(NoneType, QSslError)
  def handshakeInterruptedOnError(
      self,
      socket: Optional[QSslSocket],
      error: QSslError,
  ) -> None:
    """
    Calls Qt's 'void QSslServer::handshakeInterruptedOnError(QSslSocket
    *socket, const QSslError &error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslserver.html#handshakeInterruptedOnError

    Parameters
    ----------

    socket : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    error : QSslError
      Passed on as a value: Qt reads the C++ QSslError, which stays Python's
      own.
    """
    #  void QSslServer::handshakeInterruptedOnError(QSslSocket *socket, const
    #      QSslError &error)
    self.uglySide.call(
        'ritual_ZN10QSslServer27handshakeInterruptedOnErrorEP10QSslSocketRK'
        '9QSslError',
        self._addressOf(socket), self._valueOf(error),
    )

  @overload(QSslSocket)
  @overload(NoneType)
  def startedEncryptionHandshake(self, socket: Optional[QSslSocket]) -> None:
    """
    Calls Qt's 'void QSslServer::startedEncryptionHandshake(QSslSocket
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslserver.html#startedEncryptionHandshake

    Parameters
    ----------

    socket : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSslServer::startedEncryptionHandshake(QSslSocket *socket)
    self.uglySide.call(
        'ritual_ZN10QSslServer26startedEncryptionHandshakeEP10QSslSocket',
        self._addressOf(socket),
    )

  @overload(int)
  def incomingConnection(self, socket: int) -> None:
    """
    Calls Qt's 'void QSslServer::incomingConnection(qintptr socket)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslserver.html#incomingConnection

    Parameters
    ----------

    socket : int
      Passed on as it is.
    """
    #  void QSslServer::incomingConnection(qintptr socket)
    ritual = 'ritual_ZN10QSslServer18incomingConnectionEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSslServer18incomingConnectionEx'
    self.uglySide.call(ritual, socket)

  def d_func(self) -> Optional[QSslServerPrivate]:
    """
    Calls Qt's 'QSslServerPrivate *QSslServer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslserver.html#d_func

    Returns
    -------

    Optional[QSslServerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSslServerPrivate *QSslServer::d_func()
    address = self.uglySide.call('ritual_ZN10QSslServer6d_funcEv')
    from . import QSslServerPrivate
    return QSslServerPrivate._cuteAt(address)
