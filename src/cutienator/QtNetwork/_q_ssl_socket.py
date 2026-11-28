"""
QSslSocket binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qsslsocket.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QIODeviceBase, QList, QObject, QStringList
from . import QSsl, QAbstractSocket, QTcpSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
  from . import QOcspResponse, QSslCertificate, QSslCipher, QSslConfiguration
  from . import QSslError, QSslKey, QSslPreSharedKeyAuthenticator
  from . import QSslSocketPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSslCertificate = WAIT['QSslCertificate']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']
  QSslKey = WAIT['QSslKey']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSslSocket(QTcpSocket):
  """
  The cute side of Qt's QSslSocket: a plain Python object standing in front
  of one C++ QSslSocket.

  It is built on the cute 'QTcpSocket', as Qt's QSslSocket is built on Qt's
  QTcpSocket, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSslSocket that has a ritual and that Python can
  call so far, 74 names in all: 'metaObject', 'tr', 'resume',
  'connectToHostEncrypted', 'setSocketDescriptor', 'connectToHost',
  'disconnectFromHost', 'setSocketOption', 'socketOption', 'mode',
  'isEncrypted', 'protocol', 'setProtocol', 'peerVerifyMode',
  'setPeerVerifyMode', 'peerVerifyDepth', 'setPeerVerifyDepth',
  'peerVerifyName', 'setPeerVerifyName', 'bytesAvailable', 'bytesToWrite',
  'canReadLine', 'close', 'atEnd', 'setReadBufferSize',
  'encryptedBytesAvailable', 'encryptedBytesToWrite', 'sslConfiguration',
  'setSslConfiguration', 'setLocalCertificateChain', 'localCertificateChain',
  'setLocalCertificate', 'localCertificate', 'peerCertificate',
  'peerCertificateChain', 'sessionCipher', 'sessionProtocol',
  'ocspResponses', 'setPrivateKey', 'privateKey', 'waitForConnected',
  'waitForEncrypted', 'waitForReadyRead', 'waitForBytesWritten',
  'waitForDisconnected', 'sslHandshakeErrors', 'supportsSsl',
  'sslLibraryVersionNumber', 'sslLibraryVersionString',
  'sslLibraryBuildVersionNumber', 'sslLibraryBuildVersionString',
  'availableBackends', 'activeBackend', 'setActiveBackend',
  'isProtocolSupported', 'isClassImplemented', 'isFeatureSupported',
  'ignoreSslErrors', 'continueInterruptedHandshake', 'startClientEncryption',
  'startServerEncryption', 'encrypted', 'peerVerifyError', 'sslErrors',
  'modeChanged', 'encryptedBytesWritten',
  'preSharedKeyAuthenticationRequired', 'newSessionTicketReceived',
  'alertSent', 'alertReceived', 'handshakeInterruptedOnError', 'skipData',
  'writeData', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSslSocket::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSslSocket::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSslSocket::~QSslSocket()': the destructor: Python never removes a
    C++ QSslSocket.
  - Qt's 'QList<QSsl::SslProtocol> QSslSocket::supportedProtocols(const
    QString &backendName)': gives a type Python has no way to take yet.
  - Qt's 'QList<QSsl::ImplementedClass> QSslSocket::implementedClasses(const
    QString &backendName)': gives a type Python has no way to take yet.
  - Qt's 'QList<QSsl::SupportedFeature> QSslSocket::supportedFeatures(const
    QString &backendName)': gives a type Python has no way to take yet.
  - Qt's 'qint64 QSslSocket::readData(char *data, qint64 maxlen)': names
    'char', which has no cute class yet.
  - Qt's 'const QSslSocketPrivate *QSslSocket::d_func() const': takes in
    Python what 'QSslSocketPrivate *QSslSocket::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 93 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QSslSocket is created at the first use, not by 'QSslSocket(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSslSocket.
  - Qt tells when it has removed the C++ QSslSocket. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QSslSocket that has no cute function yet,
    'implementedClasses', 'supportedFeatures', 'supportedProtocols', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSslSocket, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PeerVerifyMode(CuteNum):
    """
    The enum 'QSslSocket::PeerVerifyMode' of Qt, with the 4 names Qt gives in
    it.
    """

    VerifyNone = Kee[int](0)
    QueryPeer = Kee[int](1)
    VerifyPeer = Kee[int](2)
    AutoVerifyPeer = Kee[int](3)

  class SslMode(CuteNum):
    """
    The enum 'QSslSocket::SslMode' of Qt, with the 3 names Qt gives in it.
    """

    UnencryptedMode = Kee[int](0)
    SslClientMode = Kee[int](1)
    SslServerMode = Kee[int](2)

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
    Calls Qt's 'QString QSslSocket::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#tr

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
    #  QString QSslSocket::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QSslSocket2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def supportsSsl() -> bool:
    """
    Calls Qt's 'bool QSslSocket::supportsSsl()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#supportsSsl
    """
    #  bool QSslSocket::supportsSsl()
    return Rituals.call('ritual_ZN10QSslSocket11supportsSslEv')

  @staticmethod
  def sslLibraryVersionNumber() -> int:
    """
    Calls Qt's 'long QSslSocket::sslLibraryVersionNumber()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#sslLibraryVersionNumber
    """
    #  long QSslSocket::sslLibraryVersionNumber()
    return Rituals.call('ritual_ZN10QSslSocket23sslLibraryVersionNumberEv')

  @staticmethod
  def sslLibraryVersionString() -> str:
    """
    Calls Qt's 'QString QSslSocket::sslLibraryVersionString()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#sslLibraryVersionString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslSocket::sslLibraryVersionString()
    return Rituals.call('ritual_ZN10QSslSocket23sslLibraryVersionStringEv')

  @staticmethod
  def sslLibraryBuildVersionNumber() -> int:
    """
    Calls Qt's 'long QSslSocket::sslLibraryBuildVersionNumber()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#sslLibraryBuildVersionNumber
    """
    #  long QSslSocket::sslLibraryBuildVersionNumber()
    return Rituals.call(
        'ritual_ZN10QSslSocket28sslLibraryBuildVersionNumberEv',
    )

  @staticmethod
  def sslLibraryBuildVersionString() -> str:
    """
    Calls Qt's 'QString QSslSocket::sslLibraryBuildVersionString()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#sslLibraryBuildVersionString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslSocket::sslLibraryBuildVersionString()
    return Rituals.call(
        'ritual_ZN10QSslSocket28sslLibraryBuildVersionStringEv',
    )

  @staticmethod
  def availableBackends() -> QStringList:
    """
    Calls Qt's 'QList<QString> QSslSocket::availableBackends()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#availableBackends

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QString> QSslSocket::availableBackends()
    address = Rituals.call('ritual_ZN10QSslSocket17availableBackendsEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  def activeBackend() -> str:
    """
    Calls Qt's 'QString QSslSocket::activeBackend()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#activeBackend

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslSocket::activeBackend()
    return Rituals.call('ritual_ZN10QSslSocket13activeBackendEv')

  @staticmethod
  @overload(str)
  def setActiveBackend(backendName: str) -> bool:
    """
    Calls Qt's 'bool QSslSocket::setActiveBackend(const QString
    &backendName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#setActiveBackend

    Parameters
    ----------

    backendName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSslSocket::setActiveBackend(const QString &backendName)
    return Rituals.call(
        'ritual_ZN10QSslSocket16setActiveBackendERK7QString', backendName,
    )

  @staticmethod
  @overload(QSsl.SslProtocol)
  @overload(QSsl.SslProtocol, str)
  def isProtocolSupported(
      protocol: QSsl.SslProtocol,
      backendName: str = '',
  ) -> bool:
    """
    Calls Qt's 'bool QSslSocket::isProtocolSupported(QSsl::SslProtocol
    protocol, const QString &backendName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#isProtocolSupported

    Parameters
    ----------

    protocol : QSsl.SslProtocol
      Passed on as its number.

    backendName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QSslSocket::isProtocolSupported(QSsl::SslProtocol protocol, const
    #      QString &backendName)
    return Rituals.call(
        'ritual_ZN10QSslSocket19isProtocolSupportedEN4QSsl11SslProtocolERK7'
        'QString',
        protocol.value, backendName,
    )

  @staticmethod
  @overload(QSsl.ImplementedClass)
  @overload(QSsl.ImplementedClass, str)
  def isClassImplemented(
      cl: QSsl.ImplementedClass,
      backendName: str = '',
  ) -> bool:
    """
    Calls Qt's 'bool QSslSocket::isClassImplemented(QSsl::ImplementedClass
    cl, const QString &backendName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#isClassImplemented

    Parameters
    ----------

    cl : QSsl.ImplementedClass
      Passed on as its number.

    backendName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QSslSocket::isClassImplemented(QSsl::ImplementedClass cl, const
    #      QString &backendName)
    return Rituals.call(
        'ritual_ZN10QSslSocket18isClassImplementedEN4QSsl16ImplementedClass'
        'ERK7QString',
        cl.value, backendName,
    )

  @staticmethod
  @overload(QSsl.SupportedFeature)
  @overload(QSsl.SupportedFeature, str)
  def isFeatureSupported(
      feat: QSsl.SupportedFeature,
      backendName: str = '',
  ) -> bool:
    """
    Calls Qt's 'bool QSslSocket::isFeatureSupported(QSsl::SupportedFeature
    feat, const QString &backendName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#isFeatureSupported

    Parameters
    ----------

    feat : QSsl.SupportedFeature
      Passed on as its number.

    backendName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QSslSocket::isFeatureSupported(QSsl::SupportedFeature feat, const
    #      QString &backendName)
    return Rituals.call(
        'ritual_ZN10QSslSocket18isFeatureSupportedEN4QSsl16SupportedFeature'
        'ERK7QString',
        feat.value, backendName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslSocket'

  #  A C++ QSslSocket Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSslSocket'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSslSocket::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSslSocket::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QSslSocket10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mode(self) -> SslMode:
    """
    Calls Qt's 'SslMode QSslSocket::mode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#mode

    Returns
    -------

    SslMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SslMode(number)' gives.
    """
    #  SslMode QSslSocket::mode() const
    return QSslSocket.SslMode(self.uglySide.call(
        'ritual_ZNK10QSslSocket4modeEv',
    ))

  def isEncrypted(self) -> bool:
    """
    Calls Qt's 'bool QSslSocket::isEncrypted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#isEncrypted
    """
    #  bool QSslSocket::isEncrypted() const
    return self.uglySide.call('ritual_ZNK10QSslSocket11isEncryptedEv')

  def protocol(self) -> QSsl.SslProtocol:
    """
    Calls Qt's 'QSsl::SslProtocol QSslSocket::protocol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#protocol

    Returns
    -------

    QSsl.SslProtocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.SslProtocol(number)'
      gives.
    """
    #  QSsl::SslProtocol QSslSocket::protocol() const
    return QSsl.SslProtocol(self.uglySide.call(
        'ritual_ZNK10QSslSocket8protocolEv',
    ))

  def peerVerifyMode(self) -> PeerVerifyMode:
    """
    Calls Qt's 'QSslSocket::PeerVerifyMode QSslSocket::peerVerifyMode()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#peerVerifyMode

    Returns
    -------

    PeerVerifyMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PeerVerifyMode(number)'
      gives.
    """
    #  QSslSocket::PeerVerifyMode QSslSocket::peerVerifyMode() const
    return QSslSocket.PeerVerifyMode(self.uglySide.call(
        'ritual_ZNK10QSslSocket14peerVerifyModeEv',
    ))

  def peerVerifyDepth(self) -> int:
    """
    Calls Qt's 'int QSslSocket::peerVerifyDepth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#peerVerifyDepth
    """
    #  int QSslSocket::peerVerifyDepth() const
    return self.uglySide.call('ritual_ZNK10QSslSocket15peerVerifyDepthEv')

  def peerVerifyName(self) -> str:
    """
    Calls Qt's 'QString QSslSocket::peerVerifyName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#peerVerifyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslSocket::peerVerifyName() const
    return self.uglySide.call('ritual_ZNK10QSslSocket14peerVerifyNameEv')

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QSslSocket::bytesAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#bytesAvailable
    """
    #  qint64 QSslSocket::bytesAvailable() const
    ritual = 'ritual_ZNK10QSslSocket14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSslSocket14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QSslSocket::bytesToWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#bytesToWrite
    """
    #  qint64 QSslSocket::bytesToWrite() const
    ritual = 'ritual_ZNK10QSslSocket12bytesToWriteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSslSocket12bytesToWriteEv'
    return self.uglySide.call(ritual)

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QSslSocket::canReadLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#canReadLine
    """
    #  bool QSslSocket::canReadLine() const
    ritual = 'ritual_ZNK10QSslSocket11canReadLineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSslSocket11canReadLineEv'
    return self.uglySide.call(ritual)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QSslSocket::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#atEnd
    """
    #  bool QSslSocket::atEnd() const
    ritual = 'ritual_ZNK10QSslSocket5atEndEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSslSocket5atEndEv'
    return self.uglySide.call(ritual)

  def encryptedBytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QSslSocket::encryptedBytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#encryptedBytesAvailable
    """
    #  qint64 QSslSocket::encryptedBytesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK10QSslSocket23encryptedBytesAvailableEv',
    )

  def encryptedBytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QSslSocket::encryptedBytesToWrite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#encryptedBytesToWrite
    """
    #  qint64 QSslSocket::encryptedBytesToWrite() const
    return self.uglySide.call(
        'ritual_ZNK10QSslSocket21encryptedBytesToWriteEv',
    )

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QSslSocket::sslConfiguration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QSslSocket::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK10QSslSocket16sslConfigurationEv',
    )
    from . import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  def localCertificateChain(self) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate> QSslSocket::localCertificateChain()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#localCertificateChain

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QSslSocket::localCertificateChain() const
    address = self.uglySide.call(
        'ritual_ZNK10QSslSocket21localCertificateChainEv',
    )
    from . import QSslCertificate
    return QList[QSslCertificate]._cuteOwning(address)

  def localCertificate(self) -> QSslCertificate:
    """
    Calls Qt's 'QSslCertificate QSslSocket::localCertificate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#localCertificate

    Returns
    -------

    QSslCertificate
      A new cute QSslCertificate around the copy Qt gave back. Python owns
      it.
    """
    #  QSslCertificate QSslSocket::localCertificate() const
    address = self.uglySide.call(
        'ritual_ZNK10QSslSocket16localCertificateEv',
    )
    from . import QSslCertificate
    return QSslCertificate._cuteOwning(address)

  def peerCertificate(self) -> QSslCertificate:
    """
    Calls Qt's 'QSslCertificate QSslSocket::peerCertificate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#peerCertificate

    Returns
    -------

    QSslCertificate
      A new cute QSslCertificate around the copy Qt gave back. Python owns
      it.
    """
    #  QSslCertificate QSslSocket::peerCertificate() const
    address = self.uglySide.call('ritual_ZNK10QSslSocket15peerCertificateEv')
    from . import QSslCertificate
    return QSslCertificate._cuteOwning(address)

  def peerCertificateChain(self) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate> QSslSocket::peerCertificateChain()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#peerCertificateChain

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QSslSocket::peerCertificateChain() const
    address = self.uglySide.call(
        'ritual_ZNK10QSslSocket20peerCertificateChainEv',
    )
    from . import QSslCertificate
    return QList[QSslCertificate]._cuteOwning(address)

  def sessionCipher(self) -> QSslCipher:
    """
    Calls Qt's 'QSslCipher QSslSocket::sessionCipher() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#sessionCipher

    Returns
    -------

    QSslCipher
      A new cute QSslCipher around the copy Qt gave back. Python owns it.
    """
    #  QSslCipher QSslSocket::sessionCipher() const
    address = self.uglySide.call('ritual_ZNK10QSslSocket13sessionCipherEv')
    from . import QSslCipher
    return QSslCipher._cuteOwning(address)

  def sessionProtocol(self) -> QSsl.SslProtocol:
    """
    Calls Qt's 'QSsl::SslProtocol QSslSocket::sessionProtocol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#sessionProtocol

    Returns
    -------

    QSsl.SslProtocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.SslProtocol(number)'
      gives.
    """
    #  QSsl::SslProtocol QSslSocket::sessionProtocol() const
    return QSsl.SslProtocol(self.uglySide.call(
        'ritual_ZNK10QSslSocket15sessionProtocolEv',
    ))

  def ocspResponses(self) -> QList[QOcspResponse]:
    """
    Calls Qt's 'QList<QOcspResponse> QSslSocket::ocspResponses() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#ocspResponses

    Returns
    -------

    QList[QOcspResponse]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOcspResponse> QSslSocket::ocspResponses() const
    address = self.uglySide.call('ritual_ZNK10QSslSocket13ocspResponsesEv')
    from . import QOcspResponse
    return QList[QOcspResponse]._cuteOwning(address)

  def privateKey(self) -> QSslKey:
    """
    Calls Qt's 'QSslKey QSslSocket::privateKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#privateKey

    Returns
    -------

    QSslKey
      A new cute QSslKey around the copy Qt gave back. Python owns it.
    """
    #  QSslKey QSslSocket::privateKey() const
    address = self.uglySide.call('ritual_ZNK10QSslSocket10privateKeyEv')
    from . import QSslKey
    return QSslKey._cuteOwning(address)

  def sslHandshakeErrors(self) -> QList[QSslError]:
    """
    Calls Qt's 'QList<QSslError> QSslSocket::sslHandshakeErrors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#sslHandshakeErrors

    Returns
    -------

    QList[QSslError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslError> QSslSocket::sslHandshakeErrors() const
    address = self.uglySide.call(
        'ritual_ZNK10QSslSocket18sslHandshakeErrorsEv',
    )
    from . import QSslError
    return QList[QSslError]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  @overload(int, QAbstractSocket.SocketState)
  @overload(int, QAbstractSocket.SocketState, QIODeviceBase.OpenMode)
  def setSocketDescriptor(
      self,
      socketDescriptor: int,
      state: QAbstractSocket.SocketState = (
          QAbstractSocket.SocketState.ConnectedState),
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> bool:
    """
    Calls Qt's 'bool QSslSocket::setSocketDescriptor(qintptr
    socketDescriptor, SocketState state, OpenMode openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#setSocketDescriptor

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.

    state : QAbstractSocket.SocketState
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractSocket.SocketState.ConnectedState.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  bool QSslSocket::setSocketDescriptor(qintptr socketDescriptor,
    #      SocketState state, OpenMode openMode)
    ritual = (
        'ritual_ZN10QSslSocket19setSocketDescriptorExN15QAbstractSocket11So'
        'cketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSslSocket19setSocketDescriptorExN15QAbstractSock'
          'et11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE')
    return self.uglySide.call(
        ritual, socketDescriptor, state.value, openMode.value,
    )

  @overload(QAbstractSocket.SocketOption, QVariant)
  def setSocketOption(
      self,
      option: QAbstractSocket.SocketOption,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QSslSocket::setSocketOption(QAbstractSocket::SocketOption option, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#setSocketOption

    Parameters
    ----------

    option : QAbstractSocket.SocketOption
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QSslSocket::setSocketOption(QAbstractSocket::SocketOption option,
    #      const QVariant &value)
    ritual = (
        'ritual_ZN10QSslSocket15setSocketOptionEN15QAbstractSocket12SocketO'
        'ptionERK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSslSocket15setSocketOptionEN15QAbstractSocket12S'
          'ocketOptionERK8QVariant')
    self.uglySide.call(ritual, option.value, self._valueOf(value))

  @overload(QSsl.SslProtocol)
  def setProtocol(self, protocol: QSsl.SslProtocol) -> None:
    """
    Calls Qt's 'void QSslSocket::setProtocol(QSsl::SslProtocol protocol)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#setProtocol

    Parameters
    ----------

    protocol : QSsl.SslProtocol
      Passed on as its number.
    """
    #  void QSslSocket::setProtocol(QSsl::SslProtocol protocol)
    self.uglySide.call(
        'ritual_ZN10QSslSocket11setProtocolEN4QSsl11SslProtocolE',
        protocol.value,
    )

  @overload(PeerVerifyMode)
  def setPeerVerifyMode(self, mode: PeerVerifyMode) -> None:
    """
    Calls Qt's 'void QSslSocket::setPeerVerifyMode(QSslSocket::PeerVerifyMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#setPeerVerifyMode

    Parameters
    ----------

    mode : PeerVerifyMode
      Passed on as its number.
    """
    #  void QSslSocket::setPeerVerifyMode(QSslSocket::PeerVerifyMode mode)
    self.uglySide.call(
        'ritual_ZN10QSslSocket17setPeerVerifyModeENS_14PeerVerifyModeE',
        mode.value,
    )

  @overload(int)
  def setPeerVerifyDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void QSslSocket::setPeerVerifyDepth(int depth)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#setPeerVerifyDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void QSslSocket::setPeerVerifyDepth(int depth)
    self.uglySide.call('ritual_ZN10QSslSocket18setPeerVerifyDepthEi', depth)

  @overload(str)
  def setPeerVerifyName(self, hostName: str) -> None:
    """
    Calls Qt's 'void QSslSocket::setPeerVerifyName(const QString &hostName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#setPeerVerifyName

    Parameters
    ----------

    hostName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSslSocket::setPeerVerifyName(const QString &hostName)
    self.uglySide.call(
        'ritual_ZN10QSslSocket17setPeerVerifyNameERK7QString', hostName,
    )

  @overload(int)
  def setReadBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QSslSocket::setReadBufferSize(qint64 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#setReadBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QSslSocket::setReadBufferSize(qint64 size)
    ritual = 'ritual_ZN10QSslSocket17setReadBufferSizeEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSslSocket17setReadBufferSizeEx'
    self.uglySide.call(ritual, size)

  @overload(QSslConfiguration)
  def setSslConfiguration(self, config: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QSslSocket::setSslConfiguration(const QSslConfiguration
    &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#setSslConfiguration

    Parameters
    ----------

    config : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QSslSocket::setSslConfiguration(const QSslConfiguration &config)
    self.uglySide.call(
        'ritual_ZN10QSslSocket19setSslConfigurationERK17QSslConfiguration',
        self._valueOf(config),
    )

  @overload(QList[QSslCertificate])
  def setLocalCertificateChain(
      self,
      localChain: QList[QSslCertificate],
  ) -> None:
    """
    Calls Qt's 'void QSslSocket::setLocalCertificateChain(const
    QList<QSslCertificate> &localChain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#setLocalCertificateChain

    Parameters
    ----------

    localChain : QList[QSslCertificate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslSocket::setLocalCertificateChain(const QList<QSslCertificate>
    #      &localChain)
    self.uglySide.call(
        'ritual_ZN10QSslSocket24setLocalCertificateChainERK5QListI15QSslCer'
        'tificateE',
        self._valueOf(localChain),
    )

  @overload(QSslCertificate)
  def setLocalCertificate(self, certificate: QSslCertificate) -> None:
    """
    Calls Qt's 'void QSslSocket::setLocalCertificate(const QSslCertificate
    &certificate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#setLocalCertificate

    Parameters
    ----------

    certificate : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  void QSslSocket::setLocalCertificate(const QSslCertificate
    #      &certificate)
    self.uglySide.call(
        'ritual_ZN10QSslSocket19setLocalCertificateERK15QSslCertificate',
        self._valueOf(certificate),
    )

  @overload(str)
  @overload(str, QSsl.EncodingFormat)
  def setLocalCertificate(
      self,
      fileName: str,
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
  ) -> None:
    """
    Calls Qt's 'void QSslSocket::setLocalCertificate(const QString &fileName,
    QSsl::EncodingFormat format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#setLocalCertificate

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.
    """
    #  void QSslSocket::setLocalCertificate(const QString &fileName,
    #      QSsl::EncodingFormat format)
    self.uglySide.call(
        'ritual_ZN10QSslSocket19setLocalCertificateERK7QStringN4QSsl14Encod'
        'ingFormatE',
        fileName, format.value,
    )

  @overload(QSslKey)
  def setPrivateKey(self, key: QSslKey) -> None:
    """
    Calls Qt's 'void QSslSocket::setPrivateKey(const QSslKey &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#setPrivateKey

    Parameters
    ----------

    key : QSslKey
      Passed on as a value: Qt reads the C++ QSslKey, which stays Python's
      own.
    """
    #  void QSslSocket::setPrivateKey(const QSslKey &key)
    self.uglySide.call(
        'ritual_ZN10QSslSocket13setPrivateKeyERK7QSslKey',
        self._valueOf(key),
    )

  @overload(str)
  @overload(str, QSsl.KeyAlgorithm)
  @overload(str, QSsl.KeyAlgorithm, QSsl.EncodingFormat)
  @overload(str, QSsl.KeyAlgorithm, QSsl.EncodingFormat, QByteArray)
  def setPrivateKey(
      self,
      fileName: str,
      algorithm: QSsl.KeyAlgorithm = QSsl.KeyAlgorithm.Rsa,
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
      passPhrase: Optional[QByteArray] = None,
  ) -> None:
    """
    Calls Qt's 'void QSslSocket::setPrivateKey(const QString &fileName,
    QSsl::KeyAlgorithm algorithm, QSsl::EncodingFormat format, const
    QByteArray &passPhrase)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#setPrivateKey

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    algorithm : QSsl.KeyAlgorithm
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.KeyAlgorithm.Rsa.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.

    passPhrase : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  void QSslSocket::setPrivateKey(const QString &fileName,
    #      QSsl::KeyAlgorithm algorithm, QSsl::EncodingFormat format, const
    #      QByteArray &passPhrase)
    if passPhrase is None:
      from ..QtCore import QByteArray
      passPhrase = QByteArray()
    self.uglySide.call(
        'ritual_ZN10QSslSocket13setPrivateKeyERK7QStringN4QSsl12KeyAlgorith'
        'mENS3_14EncodingFormatERK10QByteArray',
        fileName, algorithm.value, format.value, self._valueOf(passPhrase),
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
    Notes what was given, for Qt's 'QSslSocket::QSslSocket(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#QSslSocket

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSslSocket::QSslSocket(QObject *parent)
    self._noteCreation(QSslSocket, lambda: Rituals.call(
        'ritual_ZN10QSslSocketC1EP7QObject',
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

  def resume(self) -> None:
    """
    Calls Qt's 'void QSslSocket::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#resume
    """
    #  void QSslSocket::resume()
    ritual = 'ritual_ZN10QSslSocket6resumeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSslSocket6resumeEv'
    self.uglySide.call(ritual)

  @overload(str, int)
  @overload(str, int, QIODeviceBase.OpenMode)
  @overload(
      str, int, QIODeviceBase.OpenMode, QAbstractSocket.NetworkLayerProtocol,
  )
  def connectToHostEncrypted(
      self,
      hostName: str,
      port: int,
      mode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
      protocol: QAbstractSocket.NetworkLayerProtocol = (
          QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol),
  ) -> None:
    """
    Calls Qt's 'void QSslSocket::connectToHostEncrypted(const QString
    &hostName, quint16 port, OpenMode mode, NetworkLayerProtocol protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#connectToHostEncrypted

    Parameters
    ----------

    hostName : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.

    mode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.

    protocol : QAbstractSocket.NetworkLayerProtocol
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol.
    """
    #  void QSslSocket::connectToHostEncrypted(const QString &hostName,
    #      quint16 port, OpenMode mode, NetworkLayerProtocol protocol)
    self.uglySide.call(
        'ritual_ZN10QSslSocket22connectToHostEncryptedERK7QStringt6QFlagsIN'
        '13QIODeviceBase12OpenModeFlagEEN15QAbstractSocket20NetworkLayerPro'
        'tocolE',
        hostName, port, mode.value, protocol.value,
    )

  @overload(str, int, str)
  @overload(str, int, str, QIODeviceBase.OpenMode)
  @overload(
      str, int, str, QIODeviceBase.OpenMode,
      QAbstractSocket.NetworkLayerProtocol,
  )
  def connectToHostEncrypted(
      self,
      hostName: str,
      port: int,
      sslPeerName: str,
      mode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
      protocol: QAbstractSocket.NetworkLayerProtocol = (
          QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol),
  ) -> None:
    """
    Calls Qt's 'void QSslSocket::connectToHostEncrypted(const QString
    &hostName, quint16 port, const QString &sslPeerName, OpenMode mode,
    NetworkLayerProtocol protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#connectToHostEncrypted

    Parameters
    ----------

    hostName : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.

    sslPeerName : str
      Passed on as it is: a QString is made of it for the call.

    mode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.

    protocol : QAbstractSocket.NetworkLayerProtocol
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol.
    """
    #  void QSslSocket::connectToHostEncrypted(const QString &hostName,
    #      quint16 port, const QString &sslPeerName, OpenMode mode,
    #      NetworkLayerProtocol protocol)
    self.uglySide.call(
        'ritual_ZN10QSslSocket22connectToHostEncryptedERK7QStringtS2_6QFlag'
        'sIN13QIODeviceBase12OpenModeFlagEEN15QAbstractSocket20NetworkLayer'
        'ProtocolE',
        hostName, port, sslPeerName, mode.value, protocol.value,
    )

  @overload(str, int)
  @overload(str, int, QIODeviceBase.OpenMode)
  @overload(
      str, int, QIODeviceBase.OpenMode, QAbstractSocket.NetworkLayerProtocol,
  )
  def connectToHost(
      self,
      hostName: str,
      port: int,
      openMode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
      protocol: QAbstractSocket.NetworkLayerProtocol = (
          QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol),
  ) -> None:
    """
    Calls Qt's 'void QSslSocket::connectToHost(const QString &hostName,
    quint16 port, OpenMode openMode, NetworkLayerProtocol protocol)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#connectToHost

    Parameters
    ----------

    hostName : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.

    openMode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.

    protocol : QAbstractSocket.NetworkLayerProtocol
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractSocket.NetworkLayerProtocol.AnyIPProtocol.
    """
    #  void QSslSocket::connectToHost(const QString &hostName, quint16 port,
    #      OpenMode openMode, NetworkLayerProtocol protocol)
    ritual = (
        'ritual_ZN10QSslSocket13connectToHostERK7QStringt6QFlagsIN13QIODevi'
        'ceBase12OpenModeFlagEEN15QAbstractSocket20NetworkLayerProtocolE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSslSocket13connectToHostERK7QStringt6QFlagsIN13Q'
          'IODeviceBase12OpenModeFlagEEN15QAbstractSocket20NetworkLayerProt'
          'ocolE')
    self.uglySide.call(
        ritual, hostName, port, openMode.value, protocol.value,
    )

  def disconnectFromHost(self) -> None:
    """
    Calls Qt's 'void QSslSocket::disconnectFromHost()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#disconnectFromHost
    """
    #  void QSslSocket::disconnectFromHost()
    ritual = 'ritual_ZN10QSslSocket18disconnectFromHostEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSslSocket18disconnectFromHostEv'
    self.uglySide.call(ritual)

  @overload(QAbstractSocket.SocketOption)
  def socketOption(self, option: QAbstractSocket.SocketOption) -> QVariant:
    """
    Calls Qt's 'QVariant
    QSslSocket::socketOption(QAbstractSocket::SocketOption option)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#socketOption

    Parameters
    ----------

    option : QAbstractSocket.SocketOption
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSslSocket::socketOption(QAbstractSocket::SocketOption
    #      option)
    ritual = (
        'ritual_ZN10QSslSocket12socketOptionEN15QAbstractSocket12SocketOpti'
        'onE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSslSocket12socketOptionEN15QAbstractSocket12Sock'
          'etOptionE')
    address = self.uglySide.call(ritual, option.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def close(self) -> None:
    """
    Calls Qt's 'void QSslSocket::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#close
    """
    #  void QSslSocket::close()
    ritual = 'ritual_ZN10QSslSocket5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSslSocket5closeEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(int)
  def waitForConnected(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QSslSocket::waitForConnected(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#waitForConnected

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QSslSocket::waitForConnected(int msecs)
    ritual = 'ritual_ZN10QSslSocket16waitForConnectedEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSslSocket16waitForConnectedEi'
    return self.uglySide.call(ritual, msecs)

  @overload()
  @overload(int)
  def waitForEncrypted(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QSslSocket::waitForEncrypted(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#waitForEncrypted

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QSslSocket::waitForEncrypted(int msecs)
    return self.uglySide.call(
        'ritual_ZN10QSslSocket16waitForEncryptedEi', msecs,
    )

  @overload()
  @overload(int)
  def waitForReadyRead(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QSslSocket::waitForReadyRead(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#waitForReadyRead

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QSslSocket::waitForReadyRead(int msecs)
    ritual = 'ritual_ZN10QSslSocket16waitForReadyReadEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSslSocket16waitForReadyReadEi'
    return self.uglySide.call(ritual, msecs)

  @overload()
  @overload(int)
  def waitForBytesWritten(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QSslSocket::waitForBytesWritten(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#waitForBytesWritten

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QSslSocket::waitForBytesWritten(int msecs)
    ritual = 'ritual_ZN10QSslSocket19waitForBytesWrittenEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSslSocket19waitForBytesWrittenEi'
    return self.uglySide.call(ritual, msecs)

  @overload()
  @overload(int)
  def waitForDisconnected(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QSslSocket::waitForDisconnected(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#waitForDisconnected

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QSslSocket::waitForDisconnected(int msecs)
    ritual = 'ritual_ZN10QSslSocket19waitForDisconnectedEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSslSocket19waitForDisconnectedEi'
    return self.uglySide.call(ritual, msecs)

  @overload(QList[QSslError])
  def ignoreSslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QSslSocket::ignoreSslErrors(const QList<QSslError>
    &errors)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#ignoreSslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslSocket::ignoreSslErrors(const QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN10QSslSocket15ignoreSslErrorsERK5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  @overload()
  def ignoreSslErrors(self) -> None:
    """
    Calls Qt's 'void QSslSocket::ignoreSslErrors()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#ignoreSslErrors
    """
    #  void QSslSocket::ignoreSslErrors()
    self.uglySide.call('ritual_ZN10QSslSocket15ignoreSslErrorsEv')

  def continueInterruptedHandshake(self) -> None:
    """
    Calls Qt's 'void QSslSocket::continueInterruptedHandshake()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#continueInterruptedHandshake
    """
    #  void QSslSocket::continueInterruptedHandshake()
    self.uglySide.call(
        'ritual_ZN10QSslSocket28continueInterruptedHandshakeEv',
    )

  def startClientEncryption(self) -> None:
    """
    Calls Qt's 'void QSslSocket::startClientEncryption()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#startClientEncryption
    """
    #  void QSslSocket::startClientEncryption()
    self.uglySide.call('ritual_ZN10QSslSocket21startClientEncryptionEv')

  def startServerEncryption(self) -> None:
    """
    Calls Qt's 'void QSslSocket::startServerEncryption()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#startServerEncryption
    """
    #  void QSslSocket::startServerEncryption()
    self.uglySide.call('ritual_ZN10QSslSocket21startServerEncryptionEv')

  def encrypted(self) -> None:
    """
    Calls Qt's 'void QSslSocket::encrypted()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#encrypted
    """
    #  void QSslSocket::encrypted()
    self.uglySide.call('ritual_ZN10QSslSocket9encryptedEv')

  @overload(QSslError)
  def peerVerifyError(self, error: QSslError) -> None:
    """
    Calls Qt's 'void QSslSocket::peerVerifyError(const QSslError &error)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#peerVerifyError

    Parameters
    ----------

    error : QSslError
      Passed on as a value: Qt reads the C++ QSslError, which stays Python's
      own.
    """
    #  void QSslSocket::peerVerifyError(const QSslError &error)
    self.uglySide.call(
        'ritual_ZN10QSslSocket15peerVerifyErrorERK9QSslError',
        self._valueOf(error),
    )

  @overload(QList[QSslError])
  def sslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QSslSocket::sslErrors(const QList<QSslError> &errors)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#sslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslSocket::sslErrors(const QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN10QSslSocket9sslErrorsERK5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  @overload(SslMode)
  def modeChanged(self, newMode: SslMode) -> None:
    """
    Calls Qt's 'void QSslSocket::modeChanged(QSslSocket::SslMode newMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#modeChanged

    Parameters
    ----------

    newMode : SslMode
      Passed on as its number.
    """
    #  void QSslSocket::modeChanged(QSslSocket::SslMode newMode)
    self.uglySide.call(
        'ritual_ZN10QSslSocket11modeChangedENS_7SslModeE', newMode.value,
    )

  @overload(int)
  def encryptedBytesWritten(self, totalBytes: int) -> None:
    """
    Calls Qt's 'void QSslSocket::encryptedBytesWritten(qint64 totalBytes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#encryptedBytesWritten

    Parameters
    ----------

    totalBytes : int
      Passed on as it is.
    """
    #  void QSslSocket::encryptedBytesWritten(qint64 totalBytes)
    self.uglySide.call(
        'ritual_ZN10QSslSocket21encryptedBytesWrittenEx', totalBytes,
    )

  @overload(QSslPreSharedKeyAuthenticator)
  @overload(NoneType)
  def preSharedKeyAuthenticationRequired(
      self,
      authenticator: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QSslSocket::preSharedKeyAuthenticationRequired(
    QSslPreSharedKeyAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#preSharedKeyAuthenticationRequired

    Parameters
    ----------

    authenticator : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSslSocket::preSharedKeyAuthenticationRequired(
    #      QSslPreSharedKeyAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN10QSslSocket34preSharedKeyAuthenticationRequiredEP29QSslP'
        'reSharedKeyAuthenticator',
        self._addressOf(authenticator),
    )

  def newSessionTicketReceived(self) -> None:
    """
    Calls Qt's 'void QSslSocket::newSessionTicketReceived()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#newSessionTicketReceived
    """
    #  void QSslSocket::newSessionTicketReceived()
    self.uglySide.call('ritual_ZN10QSslSocket24newSessionTicketReceivedEv')

  @overload(QSsl.AlertLevel, QSsl.AlertType, str)
  def alertSent(
      self,
      level: QSsl.AlertLevel,
      type: QSsl.AlertType,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QSslSocket::alertSent(QSsl::AlertLevel level,
    QSsl::AlertType type, const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#alertSent

    Parameters
    ----------

    level : QSsl.AlertLevel
      Passed on as its number.

    type : QSsl.AlertType
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSslSocket::alertSent(QSsl::AlertLevel level, QSsl::AlertType
    #      type, const QString &description)
    self.uglySide.call(
        'ritual_ZN10QSslSocket9alertSentEN4QSsl10AlertLevelENS0_9AlertTypeE'
        'RK7QString',
        level.value, type.value, description,
    )

  @overload(QSsl.AlertLevel, QSsl.AlertType, str)
  def alertReceived(
      self,
      level: QSsl.AlertLevel,
      type: QSsl.AlertType,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QSslSocket::alertReceived(QSsl::AlertLevel level,
    QSsl::AlertType type, const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#alertReceived

    Parameters
    ----------

    level : QSsl.AlertLevel
      Passed on as its number.

    type : QSsl.AlertType
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSslSocket::alertReceived(QSsl::AlertLevel level, QSsl::AlertType
    #      type, const QString &description)
    self.uglySide.call(
        'ritual_ZN10QSslSocket13alertReceivedEN4QSsl10AlertLevelENS0_9Alert'
        'TypeERK7QString',
        level.value, type.value, description,
    )

  @overload(QSslError)
  def handshakeInterruptedOnError(self, error: QSslError) -> None:
    """
    Calls Qt's 'void QSslSocket::handshakeInterruptedOnError(const QSslError
    &error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocket.html#handshakeInterruptedOnError

    Parameters
    ----------

    error : QSslError
      Passed on as a value: Qt reads the C++ QSslError, which stays Python's
      own.
    """
    #  void QSslSocket::handshakeInterruptedOnError(const QSslError &error)
    self.uglySide.call(
        'ritual_ZN10QSslSocket27handshakeInterruptedOnErrorERK9QSslError',
        self._valueOf(error),
    )

  @overload(int)
  def skipData(self, maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QSslSocket::skipData(qint64 maxSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#skipData

    Parameters
    ----------

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QSslSocket::skipData(qint64 maxSize)
    ritual = 'ritual_ZN10QSslSocket8skipDataEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSslSocket8skipDataEx'
    return self.uglySide.call(ritual, maxSize)

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QSslSocket::writeData(const char *data, qint64 len)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QSslSocket::writeData(const char *data, qint64 len)
    return self.uglySide.call(
        'ritual_ZN10QSslSocket9writeDataEPKcx', self._bytesOf(data), len,
    )

  def d_func(self) -> Optional[QSslSocketPrivate]:
    """
    Calls Qt's 'QSslSocketPrivate *QSslSocket::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocket.html#d_func

    Returns
    -------

    Optional[QSslSocketPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSslSocketPrivate *QSslSocket::d_func()
    address = self.uglySide.call('ritual_ZN10QSslSocket6d_funcEv')
    from . import QSslSocketPrivate
    return QSslSocketPrivate._cuteAt(address)

  @staticmethod
  def implementedClasses(*__, **_) -> Never:
    """
    Qt's 'QList<QSsl::ImplementedClass> QSslSocket::implementedClasses(const
    QString &backendName)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSslSocket.implementedClasses' has no cute function yet. Qt's "
        "'QList<QSsl::ImplementedClass> "
        "QSslSocket::implementedClasses(const QString &backendName)': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def supportedFeatures(*__, **_) -> Never:
    """
    Qt's 'QList<QSsl::SupportedFeature> QSslSocket::supportedFeatures(const
    QString &backendName)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSslSocket.supportedFeatures' has no cute function yet. Qt's "
        "'QList<QSsl::SupportedFeature> QSslSocket::supportedFeatures(const "
        "QString &backendName)': gives a type Python has no way to take yet."
    )

  @staticmethod
  def supportedProtocols(*__, **_) -> Never:
    """
    Qt's 'QList<QSsl::SslProtocol> QSslSocket::supportedProtocols(const
    QString &backendName)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSslSocket.supportedProtocols' has no cute function yet. Qt's "
        "'QList<QSsl::SslProtocol> QSslSocket::supportedProtocols(const "
        "QString &backendName)': gives a type Python has no way to take yet."
    )
