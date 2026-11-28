"""
QSslConfiguration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qsslconfiguration.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QSsl, QSslCertificate, QSslSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QVariant
  from . import QSslCipher, QSslConfigurationPrivate
  from . import QSslDiffieHellmanParameters, QSslEllipticCurve, QSslKey
  from . import QSslKeyingMaterial
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSslCipher = WAIT['QSslCipher']
  QSslConfigurationPrivate = WAIT['QSslConfigurationPrivate']
  QSslDiffieHellmanParameters = WAIT['QSslDiffieHellmanParameters']
  QSslEllipticCurve = WAIT['QSslEllipticCurve']
  QSslKey = WAIT['QSslKey']
  QSslKeyingMaterial = WAIT['QSslKeyingMaterial']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSslConfiguration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSslConfiguration: a plain Python object standing in
  front of one C++ QSslConfiguration.

  C++ hands a QSslConfiguration around as a copy, so every C++
  QSslConfiguration behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSslConfiguration that has a ritual and that Python
  can call so far, 59 names in all: '__eq__', '__ne__', 'isNull', 'protocol',
  'setProtocol', 'peerVerifyMode', 'setPeerVerifyMode', 'peerVerifyDepth',
  'setPeerVerifyDepth', 'localCertificateChain', 'setLocalCertificateChain',
  'localCertificate', 'setLocalCertificate', 'peerCertificate',
  'peerCertificateChain', 'sessionCipher', 'sessionProtocol', 'privateKey',
  'setPrivateKey', 'ciphers', 'setCiphers', 'supportedCiphers',
  'caCertificates', 'setCaCertificates', 'addCaCertificates',
  'addCaCertificate', 'systemCaCertificates', 'setSslOption',
  'testSslOption', 'sessionTicket', 'setSessionTicket',
  'sessionTicketLifeTimeHint', 'ephemeralServerKey', 'ellipticCurves',
  'setEllipticCurves', 'supportedEllipticCurves', 'preSharedKeyIdentityHint',
  'setPreSharedKeyIdentityHint', 'diffieHellmanParameters',
  'setDiffieHellmanParameters', 'setBackendConfigurationOption',
  'defaultConfiguration', 'setDefaultConfiguration',
  'dtlsCookieVerificationEnabled', 'setDtlsCookieVerificationEnabled',
  'defaultDtlsConfiguration', 'setDefaultDtlsConfiguration',
  'handshakeMustInterruptOnError', 'setHandshakeMustInterruptOnError',
  'missingCertificateIsFatal', 'setMissingCertificateIsFatal',
  'setOcspStaplingEnabled', 'ocspStaplingEnabled', 'setAllowedNextProtocols',
  'allowedNextProtocols', 'nextNegotiatedProtocol',
  'nextProtocolNegotiationStatus', 'takeKeyingMaterial', 'setKeyingMaterial'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSslConfiguration::~QSslConfiguration()': the destructor: Python
    removes its C++ QSslConfiguration by it, and has no other use for it.
  - Qt's 'QSslConfiguration &QSslConfiguration::operator=(QSslConfiguration
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QSslConfiguration &QSslConfiguration::operator=(const
    QSslConfiguration &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'void QSslConfiguration::swap(QSslConfiguration &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QMap<QByteArray, QVariant>
    QSslConfiguration::backendConfiguration() const': gives a type Python has
    no way to take yet.
  - Qt's 'void QSslConfiguration::setBackendConfiguration(const
    QMap<QByteArray, QVariant> &backendConfiguration)': takes a type Python
    has no way to hand over yet.
  - Qt's 'std::optional<QSslKeyingMaterial>
    QSslConfiguration::takeKeyingMaterial(const QSslKeyingMaterial
    &material)': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QSslConfiguration is created at the first use, not by
    'QSslConfiguration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSslConfiguration back gives a copy the ritual made
    for Python, in a new cute QSslConfiguration.
  - Each name of Qt's QSslConfiguration that has no cute function yet,
    'backendConfiguration', 'setBackendConfiguration', 'swap', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSslConfiguration, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class NextProtocolNegotiationStatus(CuteNum):
    """
    The enum 'QSslConfiguration::NextProtocolNegotiationStatus' of Qt, with
    the 3 names Qt gives in it.
    """

    NextProtocolNegotiationNone = Kee[int](0)
    NextProtocolNegotiationNegotiated = Kee[int](1)
    NextProtocolNegotiationUnsupported = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def supportedCiphers() -> QList[QSslCipher]:
    """
    Calls Qt's 'QList<QSslCipher> QSslConfiguration::supportedCiphers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#supportedCiphers

    Returns
    -------

    QList[QSslCipher]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCipher> QSslConfiguration::supportedCiphers()
    address = Rituals.call(
        'ritual_ZN17QSslConfiguration16supportedCiphersEv',
    )
    from . import QSslCipher
    return QList[QSslCipher]._cuteOwning(address)

  @staticmethod
  def systemCaCertificates() -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate>
    QSslConfiguration::systemCaCertificates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#systemCaCertificates

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QSslConfiguration::systemCaCertificates()
    address = Rituals.call(
        'ritual_ZN17QSslConfiguration20systemCaCertificatesEv',
    )
    return QList[QSslCertificate]._cuteOwning(address)

  @staticmethod
  def supportedEllipticCurves() -> QList[QSslEllipticCurve]:
    """
    Calls Qt's 'QList<QSslEllipticCurve>
    QSslConfiguration::supportedEllipticCurves()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#supportedEllipticCurves

    Returns
    -------

    QList[QSslEllipticCurve]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslEllipticCurve> QSslConfiguration::supportedEllipticCurves()
    address = Rituals.call(
        'ritual_ZN17QSslConfiguration23supportedEllipticCurvesEv',
    )
    from . import QSslEllipticCurve
    return QList[QSslEllipticCurve]._cuteOwning(address)

  @staticmethod
  def defaultConfiguration() -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QSslConfiguration::defaultConfiguration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#defaultConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QSslConfiguration::defaultConfiguration()
    address = Rituals.call(
        'ritual_ZN17QSslConfiguration20defaultConfigurationEv',
    )
    return QSslConfiguration._cuteOwning(address)

  @staticmethod
  @overload(THIS)
  def setDefaultConfiguration(configuration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setDefaultConfiguration(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setDefaultConfiguration

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QSslConfiguration::setDefaultConfiguration(const
    #      QSslConfiguration &configuration)
    Rituals.call(
        'ritual_ZN17QSslConfiguration23setDefaultConfigurationERKS_',
        CuteMixin._valueOf(configuration),
    )

  @staticmethod
  def defaultDtlsConfiguration() -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration
    QSslConfiguration::defaultDtlsConfiguration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#defaultDtlsConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QSslConfiguration::defaultDtlsConfiguration()
    address = Rituals.call(
        'ritual_ZN17QSslConfiguration24defaultDtlsConfigurationEv',
    )
    return QSslConfiguration._cuteOwning(address)

  @staticmethod
  @overload(THIS)
  def setDefaultDtlsConfiguration(configuration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setDefaultDtlsConfiguration(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setDefaultDtlsConfiguration

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QSslConfiguration::setDefaultDtlsConfiguration(const
    #      QSslConfiguration &configuration)
    Rituals.call(
        'ritual_ZN17QSslConfiguration27setDefaultDtlsConfigurationERKS_',
        CuteMixin._valueOf(configuration),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslConfiguration'

  #  Qt's '~QSslConfiguration()'. Naming it makes this a value class: Python
  #  owns every C++ QSslConfiguration behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QSslConfigurationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSslConfiguration::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslconfiguration.html#isNull
    """
    #  bool QSslConfiguration::isNull() const
    return self.uglySide.call('ritual_ZNK17QSslConfiguration6isNullEv')

  def protocol(self) -> QSsl.SslProtocol:
    """
    Calls Qt's 'QSsl::SslProtocol QSslConfiguration::protocol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslconfiguration.html#protocol

    Returns
    -------

    QSsl.SslProtocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.SslProtocol(number)'
      gives.
    """
    #  QSsl::SslProtocol QSslConfiguration::protocol() const
    return QSsl.SslProtocol(self.uglySide.call(
        'ritual_ZNK17QSslConfiguration8protocolEv',
    ))

  def peerVerifyMode(self) -> QSslSocket.PeerVerifyMode:
    """
    Calls Qt's 'QSslSocket::PeerVerifyMode
    QSslConfiguration::peerVerifyMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#peerVerifyMode

    Returns
    -------

    QSslSocket.PeerVerifyMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSslSocket.PeerVerifyMode(number)' gives.
    """
    #  QSslSocket::PeerVerifyMode QSslConfiguration::peerVerifyMode() const
    return QSslSocket.PeerVerifyMode(self.uglySide.call(
        'ritual_ZNK17QSslConfiguration14peerVerifyModeEv',
    ))

  def peerVerifyDepth(self) -> int:
    """
    Calls Qt's 'int QSslConfiguration::peerVerifyDepth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#peerVerifyDepth
    """
    #  int QSslConfiguration::peerVerifyDepth() const
    return self.uglySide.call(
        'ritual_ZNK17QSslConfiguration15peerVerifyDepthEv',
    )

  def localCertificateChain(self) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate>
    QSslConfiguration::localCertificateChain() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#localCertificateChain

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QSslConfiguration::localCertificateChain()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration21localCertificateChainEv',
    )
    return QList[QSslCertificate]._cuteOwning(address)

  def localCertificate(self) -> QSslCertificate:
    """
    Calls Qt's 'QSslCertificate QSslConfiguration::localCertificate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#localCertificate

    Returns
    -------

    QSslCertificate
      A new cute QSslCertificate around the copy Qt gave back. Python owns
      it.
    """
    #  QSslCertificate QSslConfiguration::localCertificate() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration16localCertificateEv',
    )
    return QSslCertificate._cuteOwning(address)

  def peerCertificate(self) -> QSslCertificate:
    """
    Calls Qt's 'QSslCertificate QSslConfiguration::peerCertificate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#peerCertificate

    Returns
    -------

    QSslCertificate
      A new cute QSslCertificate around the copy Qt gave back. Python owns
      it.
    """
    #  QSslCertificate QSslConfiguration::peerCertificate() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration15peerCertificateEv',
    )
    return QSslCertificate._cuteOwning(address)

  def peerCertificateChain(self) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate>
    QSslConfiguration::peerCertificateChain() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#peerCertificateChain

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QSslConfiguration::peerCertificateChain() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration20peerCertificateChainEv',
    )
    return QList[QSslCertificate]._cuteOwning(address)

  def sessionCipher(self) -> QSslCipher:
    """
    Calls Qt's 'QSslCipher QSslConfiguration::sessionCipher() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#sessionCipher

    Returns
    -------

    QSslCipher
      A new cute QSslCipher around the copy Qt gave back. Python owns it.
    """
    #  QSslCipher QSslConfiguration::sessionCipher() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration13sessionCipherEv',
    )
    from . import QSslCipher
    return QSslCipher._cuteOwning(address)

  def sessionProtocol(self) -> QSsl.SslProtocol:
    """
    Calls Qt's 'QSsl::SslProtocol QSslConfiguration::sessionProtocol()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#sessionProtocol

    Returns
    -------

    QSsl.SslProtocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.SslProtocol(number)'
      gives.
    """
    #  QSsl::SslProtocol QSslConfiguration::sessionProtocol() const
    return QSsl.SslProtocol(self.uglySide.call(
        'ritual_ZNK17QSslConfiguration15sessionProtocolEv',
    ))

  def privateKey(self) -> QSslKey:
    """
    Calls Qt's 'QSslKey QSslConfiguration::privateKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslconfiguration.html#privateKey

    Returns
    -------

    QSslKey
      A new cute QSslKey around the copy Qt gave back. Python owns it.
    """
    #  QSslKey QSslConfiguration::privateKey() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration10privateKeyEv',
    )
    from . import QSslKey
    return QSslKey._cuteOwning(address)

  def ciphers(self) -> QList[QSslCipher]:
    """
    Calls Qt's 'QList<QSslCipher> QSslConfiguration::ciphers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslconfiguration.html#ciphers

    Returns
    -------

    QList[QSslCipher]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCipher> QSslConfiguration::ciphers() const
    address = self.uglySide.call('ritual_ZNK17QSslConfiguration7ciphersEv')
    from . import QSslCipher
    return QList[QSslCipher]._cuteOwning(address)

  def caCertificates(self) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate> QSslConfiguration::caCertificates()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#caCertificates

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QSslConfiguration::caCertificates() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration14caCertificatesEv',
    )
    return QList[QSslCertificate]._cuteOwning(address)

  @overload(QSsl.SslOption)
  def testSslOption(self, option: QSsl.SslOption) -> bool:
    """
    Calls Qt's 'bool QSslConfiguration::testSslOption(QSsl::SslOption option)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#testSslOption

    Parameters
    ----------

    option : QSsl.SslOption
      Passed on as its number.
    """
    #  bool QSslConfiguration::testSslOption(QSsl::SslOption option) const
    return self.uglySide.call(
        'ritual_ZNK17QSslConfiguration13testSslOptionEN4QSsl9SslOptionE',
        option.value,
    )

  def sessionTicket(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslConfiguration::sessionTicket() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#sessionTicket

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslConfiguration::sessionTicket() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration13sessionTicketEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def sessionTicketLifeTimeHint(self) -> int:
    """
    Calls Qt's 'int QSslConfiguration::sessionTicketLifeTimeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#sessionTicketLifeTimeHint
    """
    #  int QSslConfiguration::sessionTicketLifeTimeHint() const
    return self.uglySide.call(
        'ritual_ZNK17QSslConfiguration25sessionTicketLifeTimeHintEv',
    )

  def ephemeralServerKey(self) -> QSslKey:
    """
    Calls Qt's 'QSslKey QSslConfiguration::ephemeralServerKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#ephemeralServerKey

    Returns
    -------

    QSslKey
      A new cute QSslKey around the copy Qt gave back. Python owns it.
    """
    #  QSslKey QSslConfiguration::ephemeralServerKey() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration18ephemeralServerKeyEv',
    )
    from . import QSslKey
    return QSslKey._cuteOwning(address)

  def ellipticCurves(self) -> QList[QSslEllipticCurve]:
    """
    Calls Qt's 'QList<QSslEllipticCurve> QSslConfiguration::ellipticCurves()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#ellipticCurves

    Returns
    -------

    QList[QSslEllipticCurve]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslEllipticCurve> QSslConfiguration::ellipticCurves() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration14ellipticCurvesEv',
    )
    from . import QSslEllipticCurve
    return QList[QSslEllipticCurve]._cuteOwning(address)

  def preSharedKeyIdentityHint(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslConfiguration::preSharedKeyIdentityHint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#preSharedKeyIdentityHint

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslConfiguration::preSharedKeyIdentityHint() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration24preSharedKeyIdentityHintEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def diffieHellmanParameters(self) -> QSslDiffieHellmanParameters:
    """
    Calls Qt's 'QSslDiffieHellmanParameters
    QSslConfiguration::diffieHellmanParameters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#diffieHellmanParameters

    Returns
    -------

    QSslDiffieHellmanParameters
      A new cute QSslDiffieHellmanParameters around the copy Qt gave back.
      Python owns it.
    """
    #  QSslDiffieHellmanParameters
    #      QSslConfiguration::diffieHellmanParameters() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration23diffieHellmanParametersEv',
    )
    from . import QSslDiffieHellmanParameters
    return QSslDiffieHellmanParameters._cuteOwning(address)

  def dtlsCookieVerificationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSslConfiguration::dtlsCookieVerificationEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html
    """
    #  bool QSslConfiguration::dtlsCookieVerificationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QSslConfiguration29dtlsCookieVerificationEnabledEv',
    )

  def handshakeMustInterruptOnError(self) -> bool:
    """
    Calls Qt's 'bool QSslConfiguration::handshakeMustInterruptOnError()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html
    """
    #  bool QSslConfiguration::handshakeMustInterruptOnError() const
    return self.uglySide.call(
        'ritual_ZNK17QSslConfiguration29handshakeMustInterruptOnErrorEv',
    )

  def missingCertificateIsFatal(self) -> bool:
    """
    Calls Qt's 'bool QSslConfiguration::missingCertificateIsFatal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#missingCertificateIsFatal
    """
    #  bool QSslConfiguration::missingCertificateIsFatal() const
    return self.uglySide.call(
        'ritual_ZNK17QSslConfiguration25missingCertificateIsFatalEv',
    )

  def ocspStaplingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSslConfiguration::ocspStaplingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#ocspStaplingEnabled
    """
    #  bool QSslConfiguration::ocspStaplingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QSslConfiguration19ocspStaplingEnabledEv',
    )

  def allowedNextProtocols(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QSslConfiguration::allowedNextProtocols()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#allowedNextProtocols

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QSslConfiguration::allowedNextProtocols() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration20allowedNextProtocolsEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def nextNegotiatedProtocol(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslConfiguration::nextNegotiatedProtocol()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#nextNegotiatedProtocol

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslConfiguration::nextNegotiatedProtocol() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslConfiguration22nextNegotiatedProtocolEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def nextProtocolNegotiationStatus(self) -> NextProtocolNegotiationStatus:
    """
    Calls Qt's 'NextProtocolNegotiationStatus
    QSslConfiguration::nextProtocolNegotiationStatus() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html

    Returns
    -------

    NextProtocolNegotiationStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'NextProtocolNegotiationStatus(number)' gives.
    """
    #  NextProtocolNegotiationStatus
    #      QSslConfiguration::nextProtocolNegotiationStatus() const
    return QSslConfiguration.NextProtocolNegotiationStatus(
        self.uglySide.call(
            'ritual_ZNK17QSslConfiguration29nextProtocolNegotiationStatusEv',
        ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSsl.SslProtocol)
  def setProtocol(self, protocol: QSsl.SslProtocol) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setProtocol(QSsl::SslProtocol
    protocol)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslconfiguration.html#setProtocol

    Parameters
    ----------

    protocol : QSsl.SslProtocol
      Passed on as its number.
    """
    #  void QSslConfiguration::setProtocol(QSsl::SslProtocol protocol)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration11setProtocolEN4QSsl11SslProtocolE',
        protocol.value,
    )

  @overload(QSslSocket.PeerVerifyMode)
  def setPeerVerifyMode(self, mode: QSslSocket.PeerVerifyMode) -> None:
    """
    Calls Qt's 'void
    QSslConfiguration::setPeerVerifyMode(QSslSocket::PeerVerifyMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setPeerVerifyMode

    Parameters
    ----------

    mode : QSslSocket.PeerVerifyMode
      Passed on as its number.
    """
    #  void QSslConfiguration::setPeerVerifyMode(QSslSocket::PeerVerifyMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration17setPeerVerifyModeEN10QSslSocket14Pee'
        'rVerifyModeE',
        mode.value,
    )

  @overload(int)
  def setPeerVerifyDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setPeerVerifyDepth(int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setPeerVerifyDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void QSslConfiguration::setPeerVerifyDepth(int depth)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration18setPeerVerifyDepthEi', depth,
    )

  @overload(QList[QSslCertificate])
  def setLocalCertificateChain(
      self,
      localChain: QList[QSslCertificate],
  ) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setLocalCertificateChain(const
    QList<QSslCertificate> &localChain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setLocalCertificateChain

    Parameters
    ----------

    localChain : QList[QSslCertificate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslConfiguration::setLocalCertificateChain(const
    #      QList<QSslCertificate> &localChain)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration24setLocalCertificateChainERK5QListI15'
        'QSslCertificateE',
        self._valueOf(localChain),
    )

  @overload(QSslCertificate)
  def setLocalCertificate(self, certificate: QSslCertificate) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setLocalCertificate(const
    QSslCertificate &certificate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setLocalCertificate

    Parameters
    ----------

    certificate : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  void QSslConfiguration::setLocalCertificate(const QSslCertificate
    #      &certificate)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration19setLocalCertificateERK15QSslCertific'
        'ate',
        self._valueOf(certificate),
    )

  @overload(QSslKey)
  def setPrivateKey(self, key: QSslKey) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setPrivateKey(const QSslKey &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setPrivateKey

    Parameters
    ----------

    key : QSslKey
      Passed on as a value: Qt reads the C++ QSslKey, which stays Python's
      own.
    """
    #  void QSslConfiguration::setPrivateKey(const QSslKey &key)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration13setPrivateKeyERK7QSslKey',
        self._valueOf(key),
    )

  @overload(QList[QSslCipher])
  def setCiphers(self, ciphers: QList[QSslCipher]) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setCiphers(const QList<QSslCipher>
    &ciphers)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslconfiguration.html#setCiphers

    Parameters
    ----------

    ciphers : QList[QSslCipher]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslConfiguration::setCiphers(const QList<QSslCipher> &ciphers)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration10setCiphersERK5QListI10QSslCipherE',
        self._valueOf(ciphers),
    )

  @overload(str)
  def setCiphers(self, ciphers: str) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setCiphers(const QString &ciphers)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslconfiguration.html#setCiphers

    Parameters
    ----------

    ciphers : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSslConfiguration::setCiphers(const QString &ciphers)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration10setCiphersERK7QString', ciphers,
    )

  @overload(QList[QSslCertificate])
  def setCaCertificates(self, certificates: QList[QSslCertificate]) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setCaCertificates(const
    QList<QSslCertificate> &certificates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setCaCertificates

    Parameters
    ----------

    certificates : QList[QSslCertificate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslConfiguration::setCaCertificates(const QList<QSslCertificate>
    #      &certificates)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration17setCaCertificatesERK5QListI15QSslCer'
        'tificateE',
        self._valueOf(certificates),
    )

  @overload(QSsl.SslOption, bool)
  def setSslOption(self, option: QSsl.SslOption, on: bool) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setSslOption(QSsl::SslOption option,
    bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setSslOption

    Parameters
    ----------

    option : QSsl.SslOption
      Passed on as its number.

    on : bool
      Passed on as it is.
    """
    #  void QSslConfiguration::setSslOption(QSsl::SslOption option, bool on)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration12setSslOptionEN4QSsl9SslOptionEb',
        option.value, on,
    )

  @overload(QByteArray)
  def setSessionTicket(self, sessionTicket: QByteArray) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setSessionTicket(const QByteArray
    &sessionTicket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setSessionTicket

    Parameters
    ----------

    sessionTicket : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSslConfiguration::setSessionTicket(const QByteArray
    #      &sessionTicket)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration16setSessionTicketERK10QByteArray',
        self._valueOf(sessionTicket),
    )

  @overload(QList[QSslEllipticCurve])
  def setEllipticCurves(self, curves: QList[QSslEllipticCurve]) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setEllipticCurves(const
    QList<QSslEllipticCurve> &curves)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setEllipticCurves

    Parameters
    ----------

    curves : QList[QSslEllipticCurve]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslConfiguration::setEllipticCurves(const
    #      QList<QSslEllipticCurve> &curves)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration17setEllipticCurvesERK5QListI17QSslEll'
        'ipticCurveE',
        self._valueOf(curves),
    )

  @overload(QByteArray)
  def setPreSharedKeyIdentityHint(self, hint: QByteArray) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setPreSharedKeyIdentityHint(const
    QByteArray &hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setPreSharedKeyIdentityHint

    Parameters
    ----------

    hint : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSslConfiguration::setPreSharedKeyIdentityHint(const QByteArray
    #      &hint)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration27setPreSharedKeyIdentityHintERK10QByt'
        'eArray',
        self._valueOf(hint),
    )

  @overload(QSslDiffieHellmanParameters)
  def setDiffieHellmanParameters(
      self,
      dhparams: QSslDiffieHellmanParameters,
  ) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setDiffieHellmanParameters(const
    QSslDiffieHellmanParameters &dhparams)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setDiffieHellmanParameters

    Parameters
    ----------

    dhparams : QSslDiffieHellmanParameters
      Passed on as a value: Qt reads the C++ QSslDiffieHellmanParameters,
      which stays Python's own.
    """
    #  void QSslConfiguration::setDiffieHellmanParameters(const
    #      QSslDiffieHellmanParameters &dhparams)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration26setDiffieHellmanParametersERK27QSslD'
        'iffieHellmanParameters',
        self._valueOf(dhparams),
    )

  @overload(QByteArray, QVariant)
  def setBackendConfigurationOption(
      self,
      name: QByteArray,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setBackendConfigurationOption(const
    QByteArray &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QSslConfiguration::setBackendConfigurationOption(const QByteArray
    #      &name, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration29setBackendConfigurationOptionERK10QB'
        'yteArrayRK8QVariant',
        self._valueOf(name), self._valueOf(value),
    )

  @overload(bool)
  def setDtlsCookieVerificationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setDtlsCookieVerificationEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSslConfiguration::setDtlsCookieVerificationEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration32setDtlsCookieVerificationEnabledEb',
        enable,
    )

  @overload(bool)
  def setHandshakeMustInterruptOnError(self, interrupt: bool) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setHandshakeMustInterruptOnError(bool
    interrupt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html

    Parameters
    ----------

    interrupt : bool
      Passed on as it is.
    """
    #  void QSslConfiguration::setHandshakeMustInterruptOnError(bool
    #      interrupt)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration32setHandshakeMustInterruptOnErrorEb',
        interrupt,
    )

  @overload(bool)
  def setMissingCertificateIsFatal(self, cannotRecover: bool) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setMissingCertificateIsFatal(bool
    cannotRecover)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html

    Parameters
    ----------

    cannotRecover : bool
      Passed on as it is.
    """
    #  void QSslConfiguration::setMissingCertificateIsFatal(bool
    #      cannotRecover)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration28setMissingCertificateIsFatalEb',
        cannotRecover,
    )

  @overload(bool)
  def setOcspStaplingEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setOcspStaplingEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setOcspStaplingEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSslConfiguration::setOcspStaplingEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration22setOcspStaplingEnabledEb', enable,
    )

  @overload(QList[QByteArray])
  def setAllowedNextProtocols(self, protocols: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setAllowedNextProtocols(const
    QList<QByteArray> &protocols)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setAllowedNextProtocols

    Parameters
    ----------

    protocols : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslConfiguration::setAllowedNextProtocols(const
    #      QList<QByteArray> &protocols)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration23setAllowedNextProtocolsERK5QListI10Q'
        'ByteArrayE',
        self._valueOf(protocols),
    )

  @overload(QList[QSslKeyingMaterial])
  def setKeyingMaterial(
      self,
      keyMaterial: QList[QSslKeyingMaterial],
  ) -> None:
    """
    Calls Qt's 'void QSslConfiguration::setKeyingMaterial(const
    QList<QSslKeyingMaterial> &keyMaterial)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#setKeyingMaterial

    Parameters
    ----------

    keyMaterial : QList[QSslKeyingMaterial]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslConfiguration::setKeyingMaterial(const
    #      QList<QSslKeyingMaterial> &keyMaterial)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration17setKeyingMaterialERK5QListI18QSslKey'
        'ingMaterialE',
        self._valueOf(keyMaterial),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QSslConfiguration) -> bool:
    """
    Calls Qt's 'bool QSslConfiguration::operator==(const QSslConfiguration
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslconfiguration.html#operator==

    Parameters
    ----------

    other : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  bool QSslConfiguration::operator==(const QSslConfiguration &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QSslConfigurationeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QSslConfiguration) -> bool:
    """
    Calls Qt's 'bool QSslConfiguration::operator!=(const QSslConfiguration
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslconfiguration.html#operator!=

    Parameters
    ----------

    other : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  bool QSslConfiguration::operator!=(const QSslConfiguration &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QSslConfigurationneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSslConfiguration::QSslConfiguration()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#QSslConfiguration
    """
    #  QSslConfiguration::QSslConfiguration()
    self._noteCreation(QSslConfiguration, lambda: Rituals.call(
        'ritual_ZN17QSslConfigurationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QSslConfiguration) -> None:
    """
    Notes what was given, for Qt's
    'QSslConfiguration::QSslConfiguration(const QSslConfiguration &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#QSslConfiguration

    Parameters
    ----------

    other : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  QSslConfiguration::QSslConfiguration(const QSslConfiguration &other)
    self._noteCreation(QSslConfiguration, lambda: Rituals.call(
        'ritual_ZN17QSslConfigurationC1ERKS_', self._valueOf(other),
    ))

  @overload(QSslConfigurationPrivate)
  @overload(NoneType)
  def __init__(self, dd: Optional[QSslConfigurationPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QSslConfiguration::QSslConfiguration(QSslConfigurationPrivate *dd)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#QSslConfiguration

    Parameters
    ----------

    dd : Optional[QSslConfigurationPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSslConfiguration::QSslConfiguration(QSslConfigurationPrivate *dd)
    self._noteCreation(QSslConfiguration, lambda: Rituals.call(
        'ritual_ZN17QSslConfigurationC1EP24QSslConfigurationPrivate',
        self._addressOf(dd),
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

  @overload(str)
  @overload(str, QSsl.EncodingFormat)
  @overload(str, QSsl.EncodingFormat, QSslCertificate.PatternSyntax)
  def addCaCertificates(
      self,
      path: str,
      format: QSsl.EncodingFormat = QSsl.EncodingFormat.Pem,
      syntax: QSslCertificate.PatternSyntax = (
          QSslCertificate.PatternSyntax.FixedString),
  ) -> bool:
    """
    Calls Qt's 'bool QSslConfiguration::addCaCertificates(const QString
    &path, QSsl::EncodingFormat format, QSslCertificate::PatternSyntax
    syntax)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#addCaCertificates

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    format : QSsl.EncodingFormat
      Passed on as its number. May be left out, as in Qt: it is then
      QSsl.EncodingFormat.Pem.

    syntax : QSslCertificate.PatternSyntax
      Passed on as its number. May be left out, as in Qt: it is then
      QSslCertificate.PatternSyntax.FixedString.
    """
    #  bool QSslConfiguration::addCaCertificates(const QString &path,
    #      QSsl::EncodingFormat format, QSslCertificate::PatternSyntax
    #      syntax)
    return self.uglySide.call(
        'ritual_ZN17QSslConfiguration17addCaCertificatesERK7QStringN4QSsl14'
        'EncodingFormatEN15QSslCertificate13PatternSyntaxE',
        path, format.value, syntax.value,
    )

  @overload(QList[QSslCertificate])
  def addCaCertificates(self, certificates: QList[QSslCertificate]) -> None:
    """
    Calls Qt's 'void QSslConfiguration::addCaCertificates(const
    QList<QSslCertificate> &certificates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#addCaCertificates

    Parameters
    ----------

    certificates : QList[QSslCertificate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslConfiguration::addCaCertificates(const QList<QSslCertificate>
    #      &certificates)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration17addCaCertificatesERK5QListI15QSslCer'
        'tificateE',
        self._valueOf(certificates),
    )

  @overload(QSslCertificate)
  def addCaCertificate(self, certificate: QSslCertificate) -> None:
    """
    Calls Qt's 'void QSslConfiguration::addCaCertificate(const
    QSslCertificate &certificate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#addCaCertificate

    Parameters
    ----------

    certificate : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  void QSslConfiguration::addCaCertificate(const QSslCertificate
    #      &certificate)
    self.uglySide.call(
        'ritual_ZN17QSslConfiguration16addCaCertificateERK15QSslCertificate',
        self._valueOf(certificate),
    )

  def takeKeyingMaterial(self) -> QList[QSslKeyingMaterial]:
    """
    Calls Qt's 'QList<QSslKeyingMaterial>
    QSslConfiguration::takeKeyingMaterial()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslconfiguration.html#takeKeyingMaterial

    Returns
    -------

    QList[QSslKeyingMaterial]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslKeyingMaterial> QSslConfiguration::takeKeyingMaterial()
    address = self.uglySide.call(
        'ritual_ZN17QSslConfiguration18takeKeyingMaterialEv',
    )
    from . import QSslKeyingMaterial
    return QList[QSslKeyingMaterial]._cuteOwning(address)

  @staticmethod
  def backendConfiguration(*__, **_) -> Never:
    """
    Qt's 'QMap<QByteArray, QVariant>
    QSslConfiguration::backendConfiguration() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QSslConfiguration.backendConfiguration' has no cute function yet. "
        "Qt's 'QMap<QByteArray, QVariant> "
        "QSslConfiguration::backendConfiguration() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setBackendConfiguration(*__, **_) -> Never:
    """
    Qt's 'void QSslConfiguration::setBackendConfiguration(const
    QMap<QByteArray, QVariant> &backendConfiguration)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSslConfiguration.setBackendConfiguration' has no cute function "
        "yet. Qt's 'void QSslConfiguration::setBackendConfiguration(const "
        "QMap<QByteArray, QVariant> &backendConfiguration)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSslConfiguration::swap(QSslConfiguration &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSslConfiguration.swap' has no cute function yet. Qt's 'void "
        "QSslConfiguration::swap(QSslConfiguration &other)': takes a type "
        "Python has no way to hand over yet.")
