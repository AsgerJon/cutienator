"""
QTlsBackend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTlsBackend to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QSsl, QSslConfiguration, QTlsPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QSslCertificate, QSslCipher, QSslKey
  from . import QSslPreSharedKeyAuthenticator, QSslSocketPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSslCertificate = WAIT['QSslCertificate']
  QSslCipher = WAIT['QSslCipher']
  QSslKey = WAIT['QSslKey']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']
  QSslSocketPrivate = WAIT['QSslSocketPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTlsBackend(QObject):
  """
  The cute side of Qt's QTlsBackend: a plain Python object standing in front
  of one C++ QTlsBackend.

  It is built on the cute 'QObject', as Qt's QTlsBackend is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTlsBackend that has a ritual and that Python can
  call so far, 47 names in all: 'metaObject', 'tr', 'isValid',
  'tlsLibraryVersionNumber', 'tlsLibraryVersionString',
  'tlsLibraryBuildVersionNumber', 'tlsLibraryBuildVersionString',
  'ensureInitialized', 'backendName', 'createKey', 'createCertificate',
  'systemCaCertificates', 'createTlsCryptograph', 'createDtlsCookieVerifier',
  'curveIdFromShortName', 'curveIdFromLongName', 'shortNameForId',
  'longNameForId', 'isTlsNamedCurve', 'dhParametersFromDer',
  'dhParametersFromPem', 'availableBackendNames', 'defaultBackendName',
  'findBackend', 'activeOrAnyBackend', 'setupClientPskAuth',
  'setupServerPskAuth', 'createCiphersuite', 'defaultCiphers',
  'defaultDtlsCiphers', 'setDefaultCiphers', 'setDefaultDtlsCiphers',
  'setDefaultSupportedCiphers', 'resetDefaultEllipticCurves',
  'setDefaultCaCertificates', 'rootLoadingOnDemandAllowed',
  'clearPeerCertificates', 'setPeerSessionShared', 'setSessionAsn1',
  'setSessionLifetimeHint', 'setAlpnStatus', 'setNegotiatedProtocol',
  'storePeerCertificate', 'storePeerCertificateChain', 'addTrustedRoot',
  'setEphemeralKey', 'forceAutotestSecurityLevel'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTlsBackend::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QTlsBackend::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QTlsBackend::~QTlsBackend()': the destructor: Python never removes
    a C++ QTlsBackend.
  - Qt's 'QList<QSsl::SslProtocol> QTlsBackend::supportedProtocols() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<QSsl::SupportedFeature> QTlsBackend::supportedFeatures()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<QSsl::ImplementedClass> QTlsBackend::implementedClasses()
    const': gives a type Python has no way to take yet.
  - Qt's 'QTlsPrivate::DtlsCryptograph
    *QTlsBackend::createDtlsCryptograph(class QDtls *qObject, int mode)
    const': names 'class QDtls', which has no cute class yet.
  - Qt's 'QTlsPrivate::X509ChainVerifyPtr QTlsBackend::X509Verifier() const':
    gives a type Python has no way to take yet.
  - Qt's 'QTlsPrivate::X509PemReaderPtr QTlsBackend::X509PemReader() const':
    gives a type Python has no way to take yet.
  - Qt's 'QTlsPrivate::X509DerReaderPtr QTlsBackend::X509DerReader() const':
    gives a type Python has no way to take yet.
  - Qt's 'QTlsPrivate::X509Pkcs12ReaderPtr QTlsBackend::X509Pkcs12Reader()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<int> QTlsBackend::ellipticCurvesIds() const': gives a type
    Python has no way to take yet.
  - Qt's 'QList<QSsl::SslProtocol> QTlsBackend::supportedProtocols(const
    QString &backendName)': gives a type Python has no way to take yet.
  - Qt's 'QList<QSsl::SupportedFeature> QTlsBackend::supportedFeatures(const
    QString &backendName)': gives a type Python has no way to take yet.
  - Qt's 'QList<QSsl::ImplementedClass> QTlsBackend::implementedClasses(const
    QString &backendName)': gives a type Python has no way to take yet.
  - Qt's 'void QTlsBackend::resetBackend(QSslKey &key, QTlsPrivate::TlsKey
    *keyBackend)': takes a type Python has no way to hand over yet.
  - Qt's 'void QTlsBackend::storePeerCertificate(QSslConfiguration
    &configuration, const QSslCertificate &peerCert)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QTlsBackend::storePeerCertificateChain(QSslConfiguration
    &configuration, const QList<QSslCertificate> &peerCertificateChain)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QTlsBackend::clearPeerCertificates(QSslConfiguration
    &configuration)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  8 of the 76 functions Qt declares: 4 forbidden; 2 not a gap; 1 the class is
  abstract, so C++ cannot make one, and the C++ class of ours does not fill
  in every function it leaves open; 1 a template.

  What to expect
  --------------

  - The C++ QTlsBackend is created at the first use, not by
    'QTlsBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTlsBackend.
  - Qt tells when it has removed the C++ QTlsBackend. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QTlsBackend that has no cute function yet,
    'X509DerReader', 'X509PemReader', 'X509Pkcs12Reader', 'X509Verifier',
    '__init__', 'backend', 'createDtlsCryptograph', 'ellipticCurvesIds',
    'implementedClasses', 'resetBackend', 'supportedFeatures',
    'supportedProtocols', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QTlsBackend::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#tr

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
    #  QString QTlsBackend::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QTlsBackend2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def availableBackendNames() -> QStringList:
    """
    Calls Qt's 'QList<QString> QTlsBackend::availableBackendNames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#availableBackendNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QString> QTlsBackend::availableBackendNames()
    address = Rituals.call('ritual_ZN11QTlsBackend21availableBackendNamesEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  def defaultBackendName() -> str:
    """
    Calls Qt's 'QString QTlsBackend::defaultBackendName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#defaultBackendName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTlsBackend::defaultBackendName()
    return Rituals.call('ritual_ZN11QTlsBackend18defaultBackendNameEv')

  @staticmethod
  @overload(str)
  def findBackend(backendName: str) -> Optional[QTlsBackend]:
    """
    Calls Qt's 'QTlsBackend *QTlsBackend::findBackend(const QString
    &backendName)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#findBackend

    Parameters
    ----------

    backendName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QTlsBackend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTlsBackend *QTlsBackend::findBackend(const QString &backendName)
    address = Rituals.call(
        'ritual_ZN11QTlsBackend11findBackendERK7QString', backendName,
    )
    return QTlsBackend._cuteAt(address)

  @staticmethod
  def activeOrAnyBackend() -> Optional[QTlsBackend]:
    """
    Calls Qt's 'QTlsBackend *QTlsBackend::activeOrAnyBackend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#activeOrAnyBackend

    Returns
    -------

    Optional[QTlsBackend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTlsBackend *QTlsBackend::activeOrAnyBackend()
    address = Rituals.call('ritual_ZN11QTlsBackend18activeOrAnyBackendEv')
    return QTlsBackend._cuteAt(address)

  @staticmethod
  @overload(QSslPreSharedKeyAuthenticator, str, int, int, int)
  @overload(QSslPreSharedKeyAuthenticator, NoneType, int, int, int)
  @overload(NoneType, str, int, int, int)
  @overload(NoneType, NoneType, int, int, int)
  def setupClientPskAuth(
      auth: Optional[QSslPreSharedKeyAuthenticator],
      hint: Optional[str],
      hintLength: int,
      maxIdentityLen: int,
      maxPskLen: int,
  ) -> None:
    """
    Calls Qt's 'void
    QTlsBackend::setupClientPskAuth(QSslPreSharedKeyAuthenticator *auth,
    const char *hint, int hintLength, unsigned int maxIdentityLen, unsigned
    int maxPskLen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#setupClientPskAuth

    Parameters
    ----------

    auth : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    hint : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    hintLength : int
      Passed on as it is.

    maxIdentityLen : int
      Passed on as it is.

    maxPskLen : int
      Passed on as it is.
    """
    #  void QTlsBackend::setupClientPskAuth(QSslPreSharedKeyAuthenticator
    #      *auth, const char *hint, int hintLength, unsigned int
    #      maxIdentityLen, unsigned int maxPskLen)
    Rituals.call(
        'ritual_ZN11QTlsBackend18setupClientPskAuthEP29QSslPreSharedKeyAuth'
        'enticatorPKcijj',
        CuteMixin._addressOf(auth), CuteMixin._bytesOf(hint), hintLength,
        maxIdentityLen, maxPskLen,
    )

  @staticmethod
  @overload(QSslPreSharedKeyAuthenticator, str, QByteArray, int)
  @overload(QSslPreSharedKeyAuthenticator, NoneType, QByteArray, int)
  @overload(NoneType, str, QByteArray, int)
  @overload(NoneType, NoneType, QByteArray, int)
  def setupServerPskAuth(
      auth: Optional[QSslPreSharedKeyAuthenticator],
      identity: Optional[str],
      identityHint: QByteArray,
      maxPskLen: int,
  ) -> None:
    """
    Calls Qt's 'void
    QTlsBackend::setupServerPskAuth(QSslPreSharedKeyAuthenticator *auth,
    const char *identity, const QByteArray &identityHint, unsigned int
    maxPskLen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#setupServerPskAuth

    Parameters
    ----------

    auth : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    identity : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    identityHint : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    maxPskLen : int
      Passed on as it is.
    """
    #  void QTlsBackend::setupServerPskAuth(QSslPreSharedKeyAuthenticator
    #      *auth, const char *identity, const QByteArray &identityHint,
    #      unsigned int maxPskLen)
    Rituals.call(
        'ritual_ZN11QTlsBackend18setupServerPskAuthEP29QSslPreSharedKeyAuth'
        'enticatorPKcRK10QByteArrayj',
        CuteMixin._addressOf(auth), CuteMixin._bytesOf(identity),
        CuteMixin._valueOf(identityHint), maxPskLen,
    )

  @staticmethod
  @overload(str, int, int)
  def createCiphersuite(
      description: str,
      bits: int,
      supportedBits: int,
  ) -> QSslCipher:
    """
    Calls Qt's 'QSslCipher QTlsBackend::createCiphersuite(const QString
    &description, int bits, int supportedBits)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#createCiphersuite

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.

    bits : int
      Passed on as it is.

    supportedBits : int
      Passed on as it is.

    Returns
    -------

    QSslCipher
      A new cute QSslCipher around the copy Qt gave back. Python owns it.
    """
    #  QSslCipher QTlsBackend::createCiphersuite(const QString &description,
    #      int bits, int supportedBits)
    address = Rituals.call(
        'ritual_ZN11QTlsBackend17createCiphersuiteERK7QStringii',
        description, bits, supportedBits,
    )
    from . import QSslCipher
    return QSslCipher._cuteOwning(address)

  @staticmethod
  @overload(str, QSsl.SslProtocol, str)
  def createCiphersuite(
      suiteName: str,
      protocol: QSsl.SslProtocol,
      protocolString: str,
  ) -> QSslCipher:
    """
    Calls Qt's 'QSslCipher QTlsBackend::createCiphersuite(const QString
    &suiteName, QSsl::SslProtocol protocol, const QString &protocolString)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#createCiphersuite

    Parameters
    ----------

    suiteName : str
      Passed on as it is: a QString is made of it for the call.

    protocol : QSsl.SslProtocol
      Passed on as its number.

    protocolString : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSslCipher
      A new cute QSslCipher around the copy Qt gave back. Python owns it.
    """
    #  QSslCipher QTlsBackend::createCiphersuite(const QString &suiteName,
    #      QSsl::SslProtocol protocol, const QString &protocolString)
    address = Rituals.call(
        'ritual_ZN11QTlsBackend17createCiphersuiteERK7QStringN4QSsl11SslPro'
        'tocolES2_',
        suiteName, protocol.value, protocolString,
    )
    from . import QSslCipher
    return QSslCipher._cuteOwning(address)

  @staticmethod
  @overload(str, str, str, str, int, QSsl.SslProtocol, str)
  def createCiphersuite(
      name: str,
      keyExchangeMethod: str,
      encryptionMethod: str,
      authenticationMethod: str,
      bits: int,
      protocol: QSsl.SslProtocol,
      protocolString: str,
  ) -> QSslCipher:
    """
    Calls Qt's 'QSslCipher QTlsBackend::createCiphersuite(const QString
    &name, const QString &keyExchangeMethod, const QString &encryptionMethod,
    const QString &authenticationMethod, int bits, QSsl::SslProtocol
    protocol, const QString &protocolString)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#createCiphersuite

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    keyExchangeMethod : str
      Passed on as it is: a QString is made of it for the call.

    encryptionMethod : str
      Passed on as it is: a QString is made of it for the call.

    authenticationMethod : str
      Passed on as it is: a QString is made of it for the call.

    bits : int
      Passed on as it is.

    protocol : QSsl.SslProtocol
      Passed on as its number.

    protocolString : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSslCipher
      A new cute QSslCipher around the copy Qt gave back. Python owns it.
    """
    #  QSslCipher QTlsBackend::createCiphersuite(const QString &name, const
    #      QString &keyExchangeMethod, const QString &encryptionMethod, const
    #      QString &authenticationMethod, int bits, QSsl::SslProtocol
    #      protocol, const QString &protocolString)
    address = Rituals.call(
        'ritual_ZN11QTlsBackend17createCiphersuiteERK7QStringS2_S2_S2_iN4QS'
        'sl11SslProtocolES2_',
        name, keyExchangeMethod, encryptionMethod, authenticationMethod,
        bits, protocol.value, protocolString,
    )
    from . import QSslCipher
    return QSslCipher._cuteOwning(address)

  @staticmethod
  def defaultCiphers() -> QList[QSslCipher]:
    """
    Calls Qt's 'QList<QSslCipher> QTlsBackend::defaultCiphers()'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#defaultCiphers

    Returns
    -------

    QList[QSslCipher]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCipher> QTlsBackend::defaultCiphers()
    address = Rituals.call('ritual_ZN11QTlsBackend14defaultCiphersEv')
    from . import QSslCipher
    return QList[QSslCipher]._cuteOwning(address)

  @staticmethod
  def defaultDtlsCiphers() -> QList[QSslCipher]:
    """
    Calls Qt's 'QList<QSslCipher> QTlsBackend::defaultDtlsCiphers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#defaultDtlsCiphers

    Returns
    -------

    QList[QSslCipher]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCipher> QTlsBackend::defaultDtlsCiphers()
    address = Rituals.call('ritual_ZN11QTlsBackend18defaultDtlsCiphersEv')
    from . import QSslCipher
    return QList[QSslCipher]._cuteOwning(address)

  @staticmethod
  @overload(QList[QSslCipher])
  def setDefaultCiphers(ciphers: QList[QSslCipher]) -> None:
    """
    Calls Qt's 'void QTlsBackend::setDefaultCiphers(const QList<QSslCipher>
    &ciphers)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#setDefaultCiphers

    Parameters
    ----------

    ciphers : QList[QSslCipher]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTlsBackend::setDefaultCiphers(const QList<QSslCipher> &ciphers)
    Rituals.call(
        'ritual_ZN11QTlsBackend17setDefaultCiphersERK5QListI10QSslCipherE',
        CuteMixin._valueOf(ciphers),
    )

  @staticmethod
  @overload(QList[QSslCipher])
  def setDefaultDtlsCiphers(ciphers: QList[QSslCipher]) -> None:
    """
    Calls Qt's 'void QTlsBackend::setDefaultDtlsCiphers(const
    QList<QSslCipher> &ciphers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#setDefaultDtlsCiphers

    Parameters
    ----------

    ciphers : QList[QSslCipher]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTlsBackend::setDefaultDtlsCiphers(const QList<QSslCipher>
    #      &ciphers)
    Rituals.call(
        'ritual_ZN11QTlsBackend21setDefaultDtlsCiphersERK5QListI10QSslCiphe'
        'rE',
        CuteMixin._valueOf(ciphers),
    )

  @staticmethod
  @overload(QList[QSslCipher])
  def setDefaultSupportedCiphers(ciphers: QList[QSslCipher]) -> None:
    """
    Calls Qt's 'void QTlsBackend::setDefaultSupportedCiphers(const
    QList<QSslCipher> &ciphers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#setDefaultSupportedCiphers

    Parameters
    ----------

    ciphers : QList[QSslCipher]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTlsBackend::setDefaultSupportedCiphers(const QList<QSslCipher>
    #      &ciphers)
    Rituals.call(
        'ritual_ZN11QTlsBackend26setDefaultSupportedCiphersERK5QListI10QSsl'
        'CipherE',
        CuteMixin._valueOf(ciphers),
    )

  @staticmethod
  def resetDefaultEllipticCurves() -> None:
    """
    Calls Qt's 'void QTlsBackend::resetDefaultEllipticCurves()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#resetDefaultEllipticCurves
    """
    #  void QTlsBackend::resetDefaultEllipticCurves()
    Rituals.call('ritual_ZN11QTlsBackend26resetDefaultEllipticCurvesEv')

  @staticmethod
  @overload(QList[QSslCertificate])
  def setDefaultCaCertificates(certs: QList[QSslCertificate]) -> None:
    """
    Calls Qt's 'void QTlsBackend::setDefaultCaCertificates(const
    QList<QSslCertificate> &certs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#setDefaultCaCertificates

    Parameters
    ----------

    certs : QList[QSslCertificate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTlsBackend::setDefaultCaCertificates(const
    #      QList<QSslCertificate> &certs)
    Rituals.call(
        'ritual_ZN11QTlsBackend24setDefaultCaCertificatesERK5QListI15QSslCe'
        'rtificateE',
        CuteMixin._valueOf(certs),
    )

  @staticmethod
  @overload(QSslConfiguration)
  def rootLoadingOnDemandAllowed(configuration: QSslConfiguration) -> bool:
    """
    Calls Qt's 'bool QTlsBackend::rootLoadingOnDemandAllowed(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#rootLoadingOnDemandAllowed

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  bool QTlsBackend::rootLoadingOnDemandAllowed(const QSslConfiguration
    #      &configuration)
    return Rituals.call(
        'ritual_ZN11QTlsBackend26rootLoadingOnDemandAllowedERK17QSslConfigu'
        'ration',
        CuteMixin._valueOf(configuration),
    )

  @staticmethod
  @overload(QSslSocketPrivate)
  @overload(NoneType)
  def clearPeerCertificates(d: Optional[QSslSocketPrivate]) -> None:
    """
    Calls Qt's 'void QTlsBackend::clearPeerCertificates(QSslSocketPrivate
    *d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#clearPeerCertificates

    Parameters
    ----------

    d : Optional[QSslSocketPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTlsBackend::clearPeerCertificates(QSslSocketPrivate *d)
    Rituals.call(
        'ritual_ZN11QTlsBackend21clearPeerCertificatesEP17QSslSocketPrivate',
        CuteMixin._addressOf(d),
    )

  @staticmethod
  @overload(QSslSocketPrivate, bool)
  @overload(NoneType, bool)
  def setPeerSessionShared(
      d: Optional[QSslSocketPrivate],
      shared: bool,
  ) -> None:
    """
    Calls Qt's 'void QTlsBackend::setPeerSessionShared(QSslSocketPrivate *d,
    bool shared)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#setPeerSessionShared

    Parameters
    ----------

    d : Optional[QSslSocketPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    shared : bool
      Passed on as it is.
    """
    #  void QTlsBackend::setPeerSessionShared(QSslSocketPrivate *d, bool
    #      shared)
    Rituals.call(
        'ritual_ZN11QTlsBackend20setPeerSessionSharedEP17QSslSocketPrivateb',
        CuteMixin._addressOf(d), shared,
    )

  @staticmethod
  @overload(QSslSocketPrivate, QByteArray)
  @overload(NoneType, QByteArray)
  def setSessionAsn1(
      d: Optional[QSslSocketPrivate],
      asn1: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QTlsBackend::setSessionAsn1(QSslSocketPrivate *d, const
    QByteArray &asn1)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#setSessionAsn1

    Parameters
    ----------

    d : Optional[QSslSocketPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    asn1 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QTlsBackend::setSessionAsn1(QSslSocketPrivate *d, const
    #      QByteArray &asn1)
    Rituals.call(
        'ritual_ZN11QTlsBackend14setSessionAsn1EP17QSslSocketPrivateRK10QBy'
        'teArray',
        CuteMixin._addressOf(d), CuteMixin._valueOf(asn1),
    )

  @staticmethod
  @overload(QSslSocketPrivate, int)
  @overload(NoneType, int)
  def setSessionLifetimeHint(
      d: Optional[QSslSocketPrivate],
      hint: int,
  ) -> None:
    """
    Calls Qt's 'void QTlsBackend::setSessionLifetimeHint(QSslSocketPrivate
    *d, int hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#setSessionLifetimeHint

    Parameters
    ----------

    d : Optional[QSslSocketPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    hint : int
      Passed on as it is.
    """
    #  void QTlsBackend::setSessionLifetimeHint(QSslSocketPrivate *d, int
    #      hint)
    Rituals.call(
        'ritual_ZN11QTlsBackend22setSessionLifetimeHintEP17QSslSocketPrivat'
        'ei',
        CuteMixin._addressOf(d), hint,
    )

  @staticmethod
  @overload(
      QSslSocketPrivate, QSslConfiguration.NextProtocolNegotiationStatus,
  )
  @overload(NoneType, QSslConfiguration.NextProtocolNegotiationStatus)
  def setAlpnStatus(
      d: Optional[QSslSocketPrivate],
      st: QSslConfiguration.NextProtocolNegotiationStatus,
  ) -> None:
    """
    Calls Qt's 'void QTlsBackend::setAlpnStatus(QSslSocketPrivate *d,
    AlpnNegotiationStatus st)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#setAlpnStatus

    Parameters
    ----------

    d : Optional[QSslSocketPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    st : QSslConfiguration.NextProtocolNegotiationStatus
      Passed on as its number.
    """
    #  void QTlsBackend::setAlpnStatus(QSslSocketPrivate *d,
    #      AlpnNegotiationStatus st)
    Rituals.call(
        'ritual_ZN11QTlsBackend13setAlpnStatusEP17QSslSocketPrivateN17QSslC'
        'onfiguration29NextProtocolNegotiationStatusE',
        CuteMixin._addressOf(d), st.value,
    )

  @staticmethod
  @overload(QSslSocketPrivate, QByteArray)
  @overload(NoneType, QByteArray)
  def setNegotiatedProtocol(
      d: Optional[QSslSocketPrivate],
      protocol: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QTlsBackend::setNegotiatedProtocol(QSslSocketPrivate *d,
    const QByteArray &protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#setNegotiatedProtocol

    Parameters
    ----------

    d : Optional[QSslSocketPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    protocol : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QTlsBackend::setNegotiatedProtocol(QSslSocketPrivate *d, const
    #      QByteArray &protocol)
    Rituals.call(
        'ritual_ZN11QTlsBackend21setNegotiatedProtocolEP17QSslSocketPrivate'
        'RK10QByteArray',
        CuteMixin._addressOf(d), CuteMixin._valueOf(protocol),
    )

  @staticmethod
  @overload(QSslSocketPrivate, QSslCertificate)
  @overload(NoneType, QSslCertificate)
  def storePeerCertificate(
      d: Optional[QSslSocketPrivate],
      peerCert: QSslCertificate,
  ) -> None:
    """
    Calls Qt's 'void QTlsBackend::storePeerCertificate(QSslSocketPrivate *d,
    const QSslCertificate &peerCert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#storePeerCertificate

    Parameters
    ----------

    d : Optional[QSslSocketPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    peerCert : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  void QTlsBackend::storePeerCertificate(QSslSocketPrivate *d, const
    #      QSslCertificate &peerCert)
    Rituals.call(
        'ritual_ZN11QTlsBackend20storePeerCertificateEP17QSslSocketPrivateR'
        'K15QSslCertificate',
        CuteMixin._addressOf(d), CuteMixin._valueOf(peerCert),
    )

  @staticmethod
  @overload(QSslSocketPrivate, QList[QSslCertificate])
  @overload(NoneType, QList[QSslCertificate])
  def storePeerCertificateChain(
      d: Optional[QSslSocketPrivate],
      peerChain: QList[QSslCertificate],
  ) -> None:
    """
    Calls Qt's 'void QTlsBackend::storePeerCertificateChain(QSslSocketPrivate
    *d, const QList<QSslCertificate> &peerChain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#storePeerCertificateChain

    Parameters
    ----------

    d : Optional[QSslSocketPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    peerChain : QList[QSslCertificate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTlsBackend::storePeerCertificateChain(QSslSocketPrivate *d,
    #      const QList<QSslCertificate> &peerChain)
    Rituals.call(
        'ritual_ZN11QTlsBackend25storePeerCertificateChainEP17QSslSocketPri'
        'vateRK5QListI15QSslCertificateE',
        CuteMixin._addressOf(d), CuteMixin._valueOf(peerChain),
    )

  @staticmethod
  @overload(QSslSocketPrivate, QSslCertificate)
  @overload(NoneType, QSslCertificate)
  def addTrustedRoot(
      d: Optional[QSslSocketPrivate],
      rootCert: QSslCertificate,
  ) -> None:
    """
    Calls Qt's 'void QTlsBackend::addTrustedRoot(QSslSocketPrivate *d, const
    QSslCertificate &rootCert)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#addTrustedRoot

    Parameters
    ----------

    d : Optional[QSslSocketPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rootCert : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  void QTlsBackend::addTrustedRoot(QSslSocketPrivate *d, const
    #      QSslCertificate &rootCert)
    Rituals.call(
        'ritual_ZN11QTlsBackend14addTrustedRootEP17QSslSocketPrivateRK15QSs'
        'lCertificate',
        CuteMixin._addressOf(d), CuteMixin._valueOf(rootCert),
    )

  @staticmethod
  @overload(QSslSocketPrivate, QSslKey)
  @overload(NoneType, QSslKey)
  def setEphemeralKey(d: Optional[QSslSocketPrivate], key: QSslKey) -> None:
    """
    Calls Qt's 'void QTlsBackend::setEphemeralKey(QSslSocketPrivate *d, const
    QSslKey &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#setEphemeralKey

    Parameters
    ----------

    d : Optional[QSslSocketPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    key : QSslKey
      Passed on as a value: Qt reads the C++ QSslKey, which stays Python's
      own.
    """
    #  void QTlsBackend::setEphemeralKey(QSslSocketPrivate *d, const QSslKey
    #      &key)
    Rituals.call(
        'ritual_ZN11QTlsBackend15setEphemeralKeyEP17QSslSocketPrivateRK7QSs'
        'lKey',
        CuteMixin._addressOf(d), CuteMixin._valueOf(key),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTlsBackend'

  #  A C++ QTlsBackend Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTlsBackend'

  #  The functions Qt calls itself that QTlsBackend is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'supportedProtocols': (
          'QList<QSsl::SslProtocol> QTlsBackend::supportedProtocols() const',
      ),
      'supportedFeatures': (
          'QList<QSsl::SupportedFeature> QTlsBackend::supportedFeatures() '
          'const',
      ),
      'implementedClasses': (
          'QList<QSsl::ImplementedClass> QTlsBackend::implementedClasses() '
          'const',
      ),
      'systemCaCertificates': (
          'QList<QSslCertificate> QTlsBackend::systemCaCertificates() const',
      ),
      'createDtlsCryptograph': (
          'QTlsPrivate::DtlsCryptograph '
          '*QTlsBackend::createDtlsCryptograph(class QDtls *, int) const',
      ),
      'X509Verifier': (
          'QTlsPrivate::X509ChainVerifyPtr QTlsBackend::X509Verifier() '
          'const',
      ),
      'X509PemReader': (
          'QTlsPrivate::X509PemReaderPtr QTlsBackend::X509PemReader() const',
      ),
      'X509DerReader': (
          'QTlsPrivate::X509DerReaderPtr QTlsBackend::X509DerReader() const',
      ),
      'X509Pkcs12Reader': (
          'QTlsPrivate::X509Pkcs12ReaderPtr '
          'QTlsBackend::X509Pkcs12Reader() const',
      ),
      'ellipticCurvesIds': (
          'QList<int> QTlsBackend::ellipticCurvesIds() const',
      ),
  }

  #  The functions Qt calls itself that QTlsBackend is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'isValid': (
          ('_ZNK11QTlsBackend7isValidEv',
           ('bool', 'number', ''),
           ()),
      ),
      'tlsLibraryVersionNumber': (
          ('_ZNK11QTlsBackend23tlsLibraryVersionNumberEv',
           ('long', 'number', ''),
           ()),
      ),
      'tlsLibraryVersionString': (
          ('_ZNK11QTlsBackend23tlsLibraryVersionStringEv',
           ('address', 'text', ''),
           ()),
      ),
      'tlsLibraryBuildVersionNumber': (
          ('_ZNK11QTlsBackend28tlsLibraryBuildVersionNumberEv',
           ('long', 'number', ''),
           ()),
      ),
      'tlsLibraryBuildVersionString': (
          ('_ZNK11QTlsBackend28tlsLibraryBuildVersionStringEv',
           ('address', 'text', ''),
           ()),
      ),
      'ensureInitialized': (
          ('_ZNK11QTlsBackend17ensureInitializedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'backendName': (
          ('_ZNK11QTlsBackend11backendNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'createKey': (
          ('_ZNK11QTlsBackend9createKeyEv',
           ('address', 'address', 'QtNetwork:QTlsPrivate.TlsKey'),
           ()),
      ),
      'createCertificate': (
          ('_ZNK11QTlsBackend17createCertificateEv',
           ('address', 'address', 'QtNetwork:QTlsPrivate.X509Certificate'),
           ()),
      ),
      'createTlsCryptograph': (
          ('_ZNK11QTlsBackend20createTlsCryptographEv',
           ('address', 'address', 'QtNetwork:QTlsPrivate.TlsCryptograph'),
           ()),
      ),
      'createDtlsCookieVerifier': (
          ('_ZNK11QTlsBackend24createDtlsCookieVerifierEv',
           ('address', 'address',
            'QtNetwork:QTlsPrivate.DtlsCookieVerifier'),
           ()),
      ),
      'curveIdFromShortName': (
          ('_ZNK11QTlsBackend20curveIdFromShortNameERK7QString',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'curveIdFromLongName': (
          ('_ZNK11QTlsBackend19curveIdFromLongNameERK7QString',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'shortNameForId': (
          ('_ZNK11QTlsBackend14shortNameForIdEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'longNameForId': (
          ('_ZNK11QTlsBackend13longNameForIdEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'isTlsNamedCurve': (
          ('_ZNK11QTlsBackend15isTlsNamedCurveEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'dhParametersFromDer': (
          ('_ZNK11QTlsBackend19dhParametersFromDerERK10QByteArrayPS0_',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'address', 'QtCore:QByteArray'),
           )),
      ),
      'dhParametersFromPem': (
          ('_ZNK11QTlsBackend19dhParametersFromPemERK10QByteArrayPS0_',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'address', 'QtCore:QByteArray'),
           )),
      ),
      'forceAutotestSecurityLevel': (
          ('_ZN11QTlsBackend26forceAutotestSecurityLevelEv',
           ('nothing', 'nothing', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTlsBackend::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTlsBackend::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QTlsBackend10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTlsBackend::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#isValid
    """
    #  bool QTlsBackend::isValid() const
    ritual = 'ritual_ZNK11QTlsBackend7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend7isValidEv'
    return self.uglySide.call(ritual)

  def tlsLibraryVersionNumber(self) -> int:
    """
    Calls Qt's 'long QTlsBackend::tlsLibraryVersionNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#tlsLibraryVersionNumber
    """
    #  long QTlsBackend::tlsLibraryVersionNumber() const
    ritual = 'ritual_ZNK11QTlsBackend23tlsLibraryVersionNumberEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend23tlsLibraryVersionNumberEv'
    return self.uglySide.call(ritual)

  def tlsLibraryVersionString(self) -> str:
    """
    Calls Qt's 'QString QTlsBackend::tlsLibraryVersionString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#tlsLibraryVersionString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTlsBackend::tlsLibraryVersionString() const
    ritual = 'ritual_ZNK11QTlsBackend23tlsLibraryVersionStringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend23tlsLibraryVersionStringEv'
    return self.uglySide.call(ritual)

  def tlsLibraryBuildVersionNumber(self) -> int:
    """
    Calls Qt's 'long QTlsBackend::tlsLibraryBuildVersionNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#tlsLibraryBuildVersionNumber
    """
    #  long QTlsBackend::tlsLibraryBuildVersionNumber() const
    ritual = 'ritual_ZNK11QTlsBackend28tlsLibraryBuildVersionNumberEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend28tlsLibraryBuildVersionNumberEv'
    return self.uglySide.call(ritual)

  def tlsLibraryBuildVersionString(self) -> str:
    """
    Calls Qt's 'QString QTlsBackend::tlsLibraryBuildVersionString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#tlsLibraryBuildVersionString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTlsBackend::tlsLibraryBuildVersionString() const
    ritual = 'ritual_ZNK11QTlsBackend28tlsLibraryBuildVersionStringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend28tlsLibraryBuildVersionStringEv'
    return self.uglySide.call(ritual)

  def backendName(self) -> str:
    """
    Calls Qt's 'QString QTlsBackend::backendName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#backendName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTlsBackend::backendName() const
    return self.uglySide.call('ritual_ZNK11QTlsBackend11backendNameEv')

  def createKey(self) -> Optional[QTlsPrivate.TlsKey]:
    """
    Calls Qt's 'QTlsPrivate::TlsKey *QTlsBackend::createKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#createKey

    Returns
    -------

    Optional[QTlsPrivate.TlsKey]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTlsPrivate::TlsKey *QTlsBackend::createKey() const
    ritual = 'ritual_ZNK11QTlsBackend9createKeyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend9createKeyEv'
    address = self.uglySide.call(ritual)
    return QTlsPrivate.TlsKey._cuteAt(address)

  def createCertificate(self) -> Optional[QTlsPrivate.X509Certificate]:
    """
    Calls Qt's 'QTlsPrivate::X509Certificate
    *QTlsBackend::createCertificate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#createCertificate

    Returns
    -------

    Optional[QTlsPrivate.X509Certificate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTlsPrivate::X509Certificate *QTlsBackend::createCertificate() const
    ritual = 'ritual_ZNK11QTlsBackend17createCertificateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend17createCertificateEv'
    address = self.uglySide.call(ritual)
    return QTlsPrivate.X509Certificate._cuteAt(address)

  def systemCaCertificates(self) -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate> QTlsBackend::systemCaCertificates()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#systemCaCertificates

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QTlsBackend::systemCaCertificates() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsBackend20systemCaCertificatesEv',
    )
    from . import QSslCertificate
    return QList[QSslCertificate]._cuteOwning(address)

  def createTlsCryptograph(self) -> Optional[QTlsPrivate.TlsCryptograph]:
    """
    Calls Qt's 'QTlsPrivate::TlsCryptograph
    *QTlsBackend::createTlsCryptograph() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#createTlsCryptograph

    Returns
    -------

    Optional[QTlsPrivate.TlsCryptograph]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTlsPrivate::TlsCryptograph *QTlsBackend::createTlsCryptograph() const
    ritual = 'ritual_ZNK11QTlsBackend20createTlsCryptographEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend20createTlsCryptographEv'
    address = self.uglySide.call(ritual)
    return QTlsPrivate.TlsCryptograph._cuteAt(address)

  def createDtlsCookieVerifier(
      self,
  ) -> Optional[QTlsPrivate.DtlsCookieVerifier]:
    """
    Calls Qt's 'QTlsPrivate::DtlsCookieVerifier
    *QTlsBackend::createDtlsCookieVerifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#createDtlsCookieVerifier

    Returns
    -------

    Optional[QTlsPrivate.DtlsCookieVerifier]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTlsPrivate::DtlsCookieVerifier
    #      *QTlsBackend::createDtlsCookieVerifier() const
    ritual = 'ritual_ZNK11QTlsBackend24createDtlsCookieVerifierEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend24createDtlsCookieVerifierEv'
    address = self.uglySide.call(ritual)
    return QTlsPrivate.DtlsCookieVerifier._cuteAt(address)

  @overload(str)
  def curveIdFromShortName(self, name: str) -> int:
    """
    Calls Qt's 'int QTlsBackend::curveIdFromShortName(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#curveIdFromShortName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QTlsBackend::curveIdFromShortName(const QString &name) const
    ritual = 'ritual_ZNK11QTlsBackend20curveIdFromShortNameERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend20curveIdFromShortNameERK7QString'
    return self.uglySide.call(ritual, name)

  @overload(str)
  def curveIdFromLongName(self, name: str) -> int:
    """
    Calls Qt's 'int QTlsBackend::curveIdFromLongName(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#curveIdFromLongName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QTlsBackend::curveIdFromLongName(const QString &name) const
    ritual = 'ritual_ZNK11QTlsBackend19curveIdFromLongNameERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend19curveIdFromLongNameERK7QString'
    return self.uglySide.call(ritual, name)

  @overload(int)
  def shortNameForId(self, cid: int) -> str:
    """
    Calls Qt's 'QString QTlsBackend::shortNameForId(int cid) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#shortNameForId

    Parameters
    ----------

    cid : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTlsBackend::shortNameForId(int cid) const
    ritual = 'ritual_ZNK11QTlsBackend14shortNameForIdEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend14shortNameForIdEi'
    return self.uglySide.call(ritual, cid)

  @overload(int)
  def longNameForId(self, cid: int) -> str:
    """
    Calls Qt's 'QString QTlsBackend::longNameForId(int cid) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#longNameForId

    Parameters
    ----------

    cid : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTlsBackend::longNameForId(int cid) const
    ritual = 'ritual_ZNK11QTlsBackend13longNameForIdEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend13longNameForIdEi'
    return self.uglySide.call(ritual, cid)

  @overload(int)
  def isTlsNamedCurve(self, cid: int) -> bool:
    """
    Calls Qt's 'bool QTlsBackend::isTlsNamedCurve(int cid) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#isTlsNamedCurve

    Parameters
    ----------

    cid : int
      Passed on as it is.
    """
    #  bool QTlsBackend::isTlsNamedCurve(int cid) const
    ritual = 'ritual_ZNK11QTlsBackend15isTlsNamedCurveEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend15isTlsNamedCurveEi'
    return self.uglySide.call(ritual, cid)

  @overload(QByteArray, QByteArray)
  @overload(QByteArray, NoneType)
  def dhParametersFromDer(
      self,
      derData: QByteArray,
      data: Optional[QByteArray],
  ) -> int:
    """
    Calls Qt's 'int QTlsBackend::dhParametersFromDer(const QByteArray
    &derData, QByteArray *data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#dhParametersFromDer

    Parameters
    ----------

    derData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QTlsBackend::dhParametersFromDer(const QByteArray &derData,
    #      QByteArray *data) const
    ritual = (
        'ritual_ZNK11QTlsBackend19dhParametersFromDerERK10QByteArrayPS0_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QTlsBackend19dhParametersFromDerERK10QByteArrayP'
          'S0_')
    return self.uglySide.call(
        ritual, self._valueOf(derData), self._addressOf(data),
    )

  @overload(QByteArray, QByteArray)
  @overload(QByteArray, NoneType)
  def dhParametersFromPem(
      self,
      pemData: QByteArray,
      data: Optional[QByteArray],
  ) -> int:
    """
    Calls Qt's 'int QTlsBackend::dhParametersFromPem(const QByteArray
    &pemData, QByteArray *data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#dhParametersFromPem

    Parameters
    ----------

    pemData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QTlsBackend::dhParametersFromPem(const QByteArray &pemData,
    #      QByteArray *data) const
    ritual = (
        'ritual_ZNK11QTlsBackend19dhParametersFromPemERK10QByteArrayPS0_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QTlsBackend19dhParametersFromPemERK10QByteArrayP'
          'S0_')
    return self.uglySide.call(
        ritual, self._valueOf(pemData), self._addressOf(data),
    )

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
    Qt's 'QTlsBackend::QTlsBackend()': the class is abstract, so C++ cannot
    make one, and the C++ class of ours does not fill in every function it
    leaves open.
    """
    raise NotImplementedError(
        "'QTlsBackend.__init__' has no cute function yet. Qt's "
        "'QTlsBackend::QTlsBackend()': the class is abstract, so C++ cannot "
        "make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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

  def ensureInitialized(self) -> None:
    """
    Calls Qt's 'void QTlsBackend::ensureInitialized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtlsbackend.html#ensureInitialized
    """
    #  void QTlsBackend::ensureInitialized() const
    ritual = 'ritual_ZNK11QTlsBackend17ensureInitializedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTlsBackend17ensureInitializedEv'
    self.uglySide.call(ritual)

  def forceAutotestSecurityLevel(self) -> None:
    """
    Calls Qt's 'void QTlsBackend::forceAutotestSecurityLevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsbackend.html#forceAutotestSecurityLevel
    """
    #  void QTlsBackend::forceAutotestSecurityLevel()
    ritual = 'ritual_ZN11QTlsBackend26forceAutotestSecurityLevelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QTlsBackend26forceAutotestSecurityLevelEv'
    self.uglySide.call(ritual)

  @staticmethod
  def X509DerReader(*__, **_) -> Never:
    """
    Qt's 'QTlsPrivate::X509DerReaderPtr QTlsBackend::X509DerReader() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTlsBackend.X509DerReader' has no cute function yet. Qt's "
        "'QTlsPrivate::X509DerReaderPtr QTlsBackend::X509DerReader() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def X509PemReader(*__, **_) -> Never:
    """
    Qt's 'QTlsPrivate::X509PemReaderPtr QTlsBackend::X509PemReader() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTlsBackend.X509PemReader' has no cute function yet. Qt's "
        "'QTlsPrivate::X509PemReaderPtr QTlsBackend::X509PemReader() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def X509Pkcs12Reader(*__, **_) -> Never:
    """
    Qt's 'QTlsPrivate::X509Pkcs12ReaderPtr QTlsBackend::X509Pkcs12Reader()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTlsBackend.X509Pkcs12Reader' has no cute function yet. Qt's "
        "'QTlsPrivate::X509Pkcs12ReaderPtr QTlsBackend::X509Pkcs12Reader() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def X509Verifier(*__, **_) -> Never:
    """
    Qt's 'QTlsPrivate::X509ChainVerifyPtr QTlsBackend::X509Verifier() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTlsBackend.X509Verifier' has no cute function yet. Qt's "
        "'QTlsPrivate::X509ChainVerifyPtr QTlsBackend::X509Verifier() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def backend(*__, **_) -> Never:
    """
    Qt's 'QTlsBackend::backend': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QTlsBackend.backend' has no cute function yet. Qt's "
        "'QTlsBackend::backend': a template: a pattern and no single "
        "function.")

  @staticmethod
  def createDtlsCryptograph(*__, **_) -> Never:
    """
    Qt's 'QTlsPrivate::DtlsCryptograph
    *QTlsBackend::createDtlsCryptograph(class QDtls *qObject, int mode)
    const': names 'class QDtls', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTlsBackend.createDtlsCryptograph' has no cute function yet. Qt's "
        "'QTlsPrivate::DtlsCryptograph "
        "*QTlsBackend::createDtlsCryptograph(class QDtls *qObject, int "
        "mode) const': names 'class QDtls', which has no cute class yet.")

  @staticmethod
  def ellipticCurvesIds(*__, **_) -> Never:
    """
    Qt's 'QList<int> QTlsBackend::ellipticCurvesIds() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTlsBackend.ellipticCurvesIds' has no cute function yet. Qt's "
        "'QList<int> QTlsBackend::ellipticCurvesIds() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def implementedClasses(*__, **_) -> Never:
    """
    - Qt's 'QList<QSsl::ImplementedClass> QTlsBackend::implementedClasses()
      const': gives a type Python has no way to take yet.
    - Qt's 'QList<QSsl::ImplementedClass>
      QTlsBackend::implementedClasses(const QString &backendName)': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTlsBackend.implementedClasses' has no cute function yet. Qt's "
        "'QList<QSsl::ImplementedClass> QTlsBackend::implementedClasses() "
        "const': gives a type Python has no way to take yet. Qt's "
        "'QList<QSsl::ImplementedClass> "
        "QTlsBackend::implementedClasses(const QString &backendName)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def resetBackend(*__, **_) -> Never:
    """
    Qt's 'void QTlsBackend::resetBackend(QSslKey &key, QTlsPrivate::TlsKey
    *keyBackend)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTlsBackend.resetBackend' has no cute function yet. Qt's 'void "
        "QTlsBackend::resetBackend(QSslKey &key, QTlsPrivate::TlsKey "
        "*keyBackend)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def supportedFeatures(*__, **_) -> Never:
    """
    - Qt's 'QList<QSsl::SupportedFeature> QTlsBackend::supportedFeatures()
      const': gives a type Python has no way to take yet.
    - Qt's 'QList<QSsl::SupportedFeature>
      QTlsBackend::supportedFeatures(const QString &backendName)': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTlsBackend.supportedFeatures' has no cute function yet. Qt's "
        "'QList<QSsl::SupportedFeature> QTlsBackend::supportedFeatures() "
        "const': gives a type Python has no way to take yet. Qt's "
        "'QList<QSsl::SupportedFeature> "
        "QTlsBackend::supportedFeatures(const QString &backendName)': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def supportedProtocols(*__, **_) -> Never:
    """
    - Qt's 'QList<QSsl::SslProtocol> QTlsBackend::supportedProtocols()
      const': gives a type Python has no way to take yet.
    - Qt's 'QList<QSsl::SslProtocol> QTlsBackend::supportedProtocols(const
      QString &backendName)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTlsBackend.supportedProtocols' has no cute function yet. Qt's "
        "'QList<QSsl::SslProtocol> QTlsBackend::supportedProtocols() "
        "const': gives a type Python has no way to take yet. Qt's "
        "'QList<QSsl::SslProtocol> QTlsBackend::supportedProtocols(const "
        "QString &backendName)': gives a type Python has no way to take yet."
    )
