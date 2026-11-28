"""
QDtls binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qdtls.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QSsl, QDtlsClientVerifier, QSslSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QDtlsPrivate, QHostAddress, QSslCipher, QSslConfiguration
  from . import QSslError, QSslPreSharedKeyAuthenticator, QUdpSocket
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHostAddress = WAIT['QHostAddress']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']
  QUdpSocket = WAIT['QUdpSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDtls(QObject):
  """
  The cute side of Qt's QDtls: a plain Python object standing in front of one
  C++ QDtls.

  It is built on the cute 'QObject', as Qt's QDtls is built on Qt's QObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDtls that has a ritual and that Python can call so
  far, 33 names in all: 'metaObject', 'tr', 'setPeer',
  'setPeerVerificationName', 'peerAddress', 'peerPort',
  'peerVerificationName', 'sslMode', 'setMtuHint', 'mtuHint',
  'setCookieGeneratorParameters', 'cookieGeneratorParameters',
  'setDtlsConfiguration', 'dtlsConfiguration', 'handshakeState',
  'doHandshake', 'handleTimeout', 'resumeHandshake', 'abortHandshake',
  'shutdown', 'isConnectionEncrypted', 'sessionCipher', 'sessionProtocol',
  'writeDatagramEncrypted', 'decryptDatagram', 'dtlsErrorString',
  'peerVerificationErrors', 'ignoreVerificationErrors', 'pskRequired',
  'handshakeTimeout', 'startHandshake', 'continueHandshake', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDtls::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QDtls::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QDtls::~QDtls()': the destructor: Python never removes a C++ QDtls.
  - Qt's 'QDtlsError QDtls::dtlsError() const': gives the enum 'QDtlsError',
    whose class cannot be named here.
  - Qt's 'const QDtlsPrivate *QDtls::d_func() const': takes in Python what
    'QDtlsPrivate *QDtls::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 45 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QDtls is created at the first use, not by 'QDtls(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDtls.
  - Qt tells when it has removed the C++ QDtls. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QDtls that has no cute function yet, 'dtlsError', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDtls, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class HandshakeState(CuteNum):
    """
    The enum 'QDtls::HandshakeState' of Qt, with the 4 names Qt gives in it.
    """

    HandshakeNotStarted = Kee[int](0)
    HandshakeInProgress = Kee[int](1)
    PeerVerificationFailed = Kee[int](2)
    HandshakeComplete = Kee[int](3)

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
    Calls Qt's 'QString QDtls::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#tr

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
    #  QString QDtls::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN5QDtls2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDtls'

  #  A C++ QDtls Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDtls'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDtls::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDtls::metaObject() const
    address = self.uglySide.call('ritual_ZNK5QDtls10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def peerAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QDtls::peerAddress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#peerAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QDtls::peerAddress() const
    address = self.uglySide.call('ritual_ZNK5QDtls11peerAddressEv')
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def peerPort(self) -> int:
    """
    Calls Qt's 'quint16 QDtls::peerPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#peerPort
    """
    #  quint16 QDtls::peerPort() const
    return self.uglySide.call('ritual_ZNK5QDtls8peerPortEv')

  def peerVerificationName(self) -> str:
    """
    Calls Qt's 'QString QDtls::peerVerificationName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#peerVerificationName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDtls::peerVerificationName() const
    return self.uglySide.call('ritual_ZNK5QDtls20peerVerificationNameEv')

  def sslMode(self) -> QSslSocket.SslMode:
    """
    Calls Qt's 'QSslSocket::SslMode QDtls::sslMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#sslMode

    Returns
    -------

    QSslSocket.SslMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSslSocket.SslMode(number)' gives.
    """
    #  QSslSocket::SslMode QDtls::sslMode() const
    return QSslSocket.SslMode(self.uglySide.call(
        'ritual_ZNK5QDtls7sslModeEv',
    ))

  def mtuHint(self) -> int:
    """
    Calls Qt's 'quint16 QDtls::mtuHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#mtuHint
    """
    #  quint16 QDtls::mtuHint() const
    return self.uglySide.call('ritual_ZNK5QDtls7mtuHintEv')

  def cookieGeneratorParameters(
      self,
  ) -> QDtlsClientVerifier.GeneratorParameters:
    """
    Calls Qt's 'GeneratorParameters QDtls::cookieGeneratorParameters()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdtls.html#cookieGeneratorParameters

    Returns
    -------

    QDtlsClientVerifier.GeneratorParameters
      A new cute QDtlsClientVerifier::GeneratorParameters around the copy Qt
      gave back. Python owns it.
    """
    #  GeneratorParameters QDtls::cookieGeneratorParameters() const
    address = self.uglySide.call(
        'ritual_ZNK5QDtls25cookieGeneratorParametersEv',
    )
    return QDtlsClientVerifier.GeneratorParameters._cuteOwning(address)

  def dtlsConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QDtls::dtlsConfiguration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#dtlsConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QDtls::dtlsConfiguration() const
    address = self.uglySide.call('ritual_ZNK5QDtls17dtlsConfigurationEv')
    from . import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  def handshakeState(self) -> HandshakeState:
    """
    Calls Qt's 'HandshakeState QDtls::handshakeState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#handshakeState

    Returns
    -------

    HandshakeState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HandshakeState(number)'
      gives.
    """
    #  HandshakeState QDtls::handshakeState() const
    return QDtls.HandshakeState(self.uglySide.call(
        'ritual_ZNK5QDtls14handshakeStateEv',
    ))

  def isConnectionEncrypted(self) -> bool:
    """
    Calls Qt's 'bool QDtls::isConnectionEncrypted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#isConnectionEncrypted
    """
    #  bool QDtls::isConnectionEncrypted() const
    return self.uglySide.call('ritual_ZNK5QDtls21isConnectionEncryptedEv')

  def sessionCipher(self) -> QSslCipher:
    """
    Calls Qt's 'QSslCipher QDtls::sessionCipher() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#sessionCipher

    Returns
    -------

    QSslCipher
      A new cute QSslCipher around the copy Qt gave back. Python owns it.
    """
    #  QSslCipher QDtls::sessionCipher() const
    address = self.uglySide.call('ritual_ZNK5QDtls13sessionCipherEv')
    from . import QSslCipher
    return QSslCipher._cuteOwning(address)

  def sessionProtocol(self) -> QSsl.SslProtocol:
    """
    Calls Qt's 'QSsl::SslProtocol QDtls::sessionProtocol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#sessionProtocol

    Returns
    -------

    QSsl.SslProtocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.SslProtocol(number)'
      gives.
    """
    #  QSsl::SslProtocol QDtls::sessionProtocol() const
    return QSsl.SslProtocol(self.uglySide.call(
        'ritual_ZNK5QDtls15sessionProtocolEv',
    ))

  def dtlsErrorString(self) -> str:
    """
    Calls Qt's 'QString QDtls::dtlsErrorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#dtlsErrorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDtls::dtlsErrorString() const
    return self.uglySide.call('ritual_ZNK5QDtls15dtlsErrorStringEv')

  def peerVerificationErrors(self) -> QList[QSslError]:
    """
    Calls Qt's 'QList<QSslError> QDtls::peerVerificationErrors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#peerVerificationErrors

    Returns
    -------

    QList[QSslError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslError> QDtls::peerVerificationErrors() const
    address = self.uglySide.call(
        'ritual_ZNK5QDtls22peerVerificationErrorsEv',
    )
    from . import QSslError
    return QList[QSslError]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHostAddress, int)
  @overload(QHostAddress, int, str)
  def setPeer(
      self,
      address: QHostAddress,
      port: int,
      verificationName: str = '',
  ) -> bool:
    """
    Calls Qt's 'bool QDtls::setPeer(const QHostAddress &address, quint16
    port, const QString &verificationName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#setPeer

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.

    verificationName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QDtls::setPeer(const QHostAddress &address, quint16 port, const
    #      QString &verificationName)
    return self.uglySide.call(
        'ritual_ZN5QDtls7setPeerERK12QHostAddresstRK7QString',
        self._valueOf(address), port, verificationName,
    )

  @overload(str)
  def setPeerVerificationName(self, name: str) -> bool:
    """
    Calls Qt's 'bool QDtls::setPeerVerificationName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#setPeerVerificationName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDtls::setPeerVerificationName(const QString &name)
    return self.uglySide.call(
        'ritual_ZN5QDtls23setPeerVerificationNameERK7QString', name,
    )

  @overload(int)
  def setMtuHint(self, mtuHint: int) -> None:
    """
    Calls Qt's 'void QDtls::setMtuHint(quint16 mtuHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#setMtuHint

    Parameters
    ----------

    mtuHint : int
      Passed on as it is.
    """
    #  void QDtls::setMtuHint(quint16 mtuHint)
    self.uglySide.call('ritual_ZN5QDtls10setMtuHintEt', mtuHint)

  @overload(QDtlsClientVerifier.GeneratorParameters)
  def setCookieGeneratorParameters(
      self,
      params: QDtlsClientVerifier.GeneratorParameters,
  ) -> bool:
    """
    Calls Qt's 'bool QDtls::setCookieGeneratorParameters(const
    GeneratorParameters &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdtls.html#setCookieGeneratorParameters

    Parameters
    ----------

    params : QDtlsClientVerifier.GeneratorParameters
      Passed on as a value: Qt reads the C++
      QDtlsClientVerifier::GeneratorParameters, which stays Python's own.
    """
    #  bool QDtls::setCookieGeneratorParameters(const GeneratorParameters
    #      &params)
    return self.uglySide.call(
        'ritual_ZN5QDtls28setCookieGeneratorParametersERKN19QDtlsClientVeri'
        'fier19GeneratorParametersE',
        self._valueOf(params),
    )

  @overload(QSslConfiguration)
  def setDtlsConfiguration(self, configuration: QSslConfiguration) -> bool:
    """
    Calls Qt's 'bool QDtls::setDtlsConfiguration(const QSslConfiguration
    &configuration)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#setDtlsConfiguration

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  bool QDtls::setDtlsConfiguration(const QSslConfiguration
    #      &configuration)
    return self.uglySide.call(
        'ritual_ZN5QDtls20setDtlsConfigurationERK17QSslConfiguration',
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

  @overload(QSslSocket.SslMode)
  @overload(QSslSocket.SslMode, QObject)
  @overload(QSslSocket.SslMode, NoneType)
  def __init__(
      self,
      mode: QSslSocket.SslMode,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDtls::QDtls(QSslSocket::SslMode mode,
    QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#QDtls

    Parameters
    ----------

    mode : QSslSocket.SslMode
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDtls::QDtls(QSslSocket::SslMode mode, QObject *parent)
    self._noteCreation(QDtls, lambda: Rituals.call(
        'ritual_ZN5QDtlsC1EN10QSslSocket7SslModeEP7QObject',
        mode.value, self._addressOf(parent, 'QObject'),
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

  @overload(QUdpSocket)
  @overload(NoneType)
  @overload(QUdpSocket, QByteArray)
  @overload(NoneType, QByteArray)
  def doHandshake(
      self,
      socket: Optional[QUdpSocket],
      dgram: Optional[QByteArray] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QDtls::doHandshake(QUdpSocket *socket, const QByteArray
    &dgram)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#doHandshake

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dgram : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  bool QDtls::doHandshake(QUdpSocket *socket, const QByteArray &dgram)
    if dgram is None:
      from ..QtCore import QByteArray
      dgram = QByteArray()
    return self.uglySide.call(
        'ritual_ZN5QDtls11doHandshakeEP10QUdpSocketRK10QByteArray',
        self._addressOf(socket), self._valueOf(dgram),
    )

  @overload(QUdpSocket)
  @overload(NoneType)
  def handleTimeout(self, socket: Optional[QUdpSocket]) -> bool:
    """
    Calls Qt's 'bool QDtls::handleTimeout(QUdpSocket *socket)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#handleTimeout

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDtls::handleTimeout(QUdpSocket *socket)
    return self.uglySide.call(
        'ritual_ZN5QDtls13handleTimeoutEP10QUdpSocket',
        self._addressOf(socket),
    )

  @overload(QUdpSocket)
  @overload(NoneType)
  def resumeHandshake(self, socket: Optional[QUdpSocket]) -> bool:
    """
    Calls Qt's 'bool QDtls::resumeHandshake(QUdpSocket *socket)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#resumeHandshake

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDtls::resumeHandshake(QUdpSocket *socket)
    return self.uglySide.call(
        'ritual_ZN5QDtls15resumeHandshakeEP10QUdpSocket',
        self._addressOf(socket),
    )

  @overload(QUdpSocket)
  @overload(NoneType)
  def abortHandshake(self, socket: Optional[QUdpSocket]) -> bool:
    """
    Calls Qt's 'bool QDtls::abortHandshake(QUdpSocket *socket)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#abortHandshake

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDtls::abortHandshake(QUdpSocket *socket)
    return self.uglySide.call(
        'ritual_ZN5QDtls14abortHandshakeEP10QUdpSocket',
        self._addressOf(socket),
    )

  @overload(QUdpSocket)
  @overload(NoneType)
  def shutdown(self, socket: Optional[QUdpSocket]) -> bool:
    """
    Calls Qt's 'bool QDtls::shutdown(QUdpSocket *socket)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#shutdown

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDtls::shutdown(QUdpSocket *socket)
    return self.uglySide.call(
        'ritual_ZN5QDtls8shutdownEP10QUdpSocket', self._addressOf(socket),
    )

  @overload(QUdpSocket, QByteArray)
  @overload(NoneType, QByteArray)
  def writeDatagramEncrypted(
      self,
      socket: Optional[QUdpSocket],
      dgram: QByteArray,
  ) -> int:
    """
    Calls Qt's 'qint64 QDtls::writeDatagramEncrypted(QUdpSocket *socket,
    const QByteArray &dgram)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#writeDatagramEncrypted

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dgram : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  qint64 QDtls::writeDatagramEncrypted(QUdpSocket *socket, const
    #      QByteArray &dgram)
    return self.uglySide.call(
        'ritual_ZN5QDtls22writeDatagramEncryptedEP10QUdpSocketRK10QByteArra'
        'y',
        self._addressOf(socket), self._valueOf(dgram),
    )

  @overload(QUdpSocket, QByteArray)
  @overload(NoneType, QByteArray)
  def decryptDatagram(
      self,
      socket: Optional[QUdpSocket],
      dgram: QByteArray,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QDtls::decryptDatagram(QUdpSocket *socket, const
    QByteArray &dgram)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#decryptDatagram

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dgram : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QDtls::decryptDatagram(QUdpSocket *socket, const QByteArray
    #      &dgram)
    address = self.uglySide.call(
        'ritual_ZN5QDtls15decryptDatagramEP10QUdpSocketRK10QByteArray',
        self._addressOf(socket), self._valueOf(dgram),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QList[QSslError])
  def ignoreVerificationErrors(
      self,
      errorsToIgnore: QList[QSslError],
  ) -> None:
    """
    Calls Qt's 'void QDtls::ignoreVerificationErrors(const QList<QSslError>
    &errorsToIgnore)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdtls.html#ignoreVerificationErrors

    Parameters
    ----------

    errorsToIgnore : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDtls::ignoreVerificationErrors(const QList<QSslError>
    #      &errorsToIgnore)
    self.uglySide.call(
        'ritual_ZN5QDtls24ignoreVerificationErrorsERK5QListI9QSslErrorE',
        self._valueOf(errorsToIgnore),
    )

  @overload(QSslPreSharedKeyAuthenticator)
  @overload(NoneType)
  def pskRequired(
      self,
      authenticator: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QDtls::pskRequired(QSslPreSharedKeyAuthenticator
    *authenticator)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#pskRequired

    Parameters
    ----------

    authenticator : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDtls::pskRequired(QSslPreSharedKeyAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN5QDtls11pskRequiredEP29QSslPreSharedKeyAuthenticator',
        self._addressOf(authenticator),
    )

  def handshakeTimeout(self) -> None:
    """
    Calls Qt's 'void QDtls::handshakeTimeout()'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#handshakeTimeout
    """
    #  void QDtls::handshakeTimeout()
    self.uglySide.call('ritual_ZN5QDtls16handshakeTimeoutEv')

  @overload(QUdpSocket, QByteArray)
  @overload(NoneType, QByteArray)
  def startHandshake(
      self,
      socket: Optional[QUdpSocket],
      dgram: QByteArray,
  ) -> bool:
    """
    Calls Qt's 'bool QDtls::startHandshake(QUdpSocket *socket, const
    QByteArray &dgram)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#startHandshake

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dgram : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QDtls::startHandshake(QUdpSocket *socket, const QByteArray
    #      &dgram)
    return self.uglySide.call(
        'ritual_ZN5QDtls14startHandshakeEP10QUdpSocketRK10QByteArray',
        self._addressOf(socket), self._valueOf(dgram),
    )

  @overload(QUdpSocket, QByteArray)
  @overload(NoneType, QByteArray)
  def continueHandshake(
      self,
      socket: Optional[QUdpSocket],
      dgram: QByteArray,
  ) -> bool:
    """
    Calls Qt's 'bool QDtls::continueHandshake(QUdpSocket *socket, const
    QByteArray &dgram)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#continueHandshake

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dgram : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QDtls::continueHandshake(QUdpSocket *socket, const QByteArray
    #      &dgram)
    return self.uglySide.call(
        'ritual_ZN5QDtls17continueHandshakeEP10QUdpSocketRK10QByteArray',
        self._addressOf(socket), self._valueOf(dgram),
    )

  def d_func(self) -> Optional[QDtlsPrivate]:
    """
    Calls Qt's 'QDtlsPrivate *QDtls::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdtls.html#d_func

    Returns
    -------

    Optional[QDtlsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDtlsPrivate *QDtls::d_func()
    address = self.uglySide.call('ritual_ZN5QDtls6d_funcEv')
    from . import QDtlsPrivate
    return QDtlsPrivate._cuteAt(address)

  @staticmethod
  def dtlsError(*__, **_) -> Never:
    """
    Qt's 'QDtlsError QDtls::dtlsError() const': gives the enum 'QDtlsError',
    whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QDtls.dtlsError' has no cute function yet. Qt's 'QDtlsError "
        "QDtls::dtlsError() const': gives the enum 'QDtlsError', whose "
        "class cannot be named here.")
