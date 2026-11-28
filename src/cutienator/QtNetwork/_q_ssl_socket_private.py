"""
QSslSocketPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qsslsocket_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSslSocketPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QIODeviceBase, QList
from . import QSsl, QAbstractSocket, QSslSocket, QTcpSocketPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QHostAddress, QNetworkInterface, QSslCertificate, QSslCipher
  from . import QSslEllipticCurve, QTcpSocket, QTlsBackend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']
  QNetworkInterface = WAIT['QNetworkInterface']
  QSslCertificate = WAIT['QSslCertificate']
  QSslCipher = WAIT['QSslCipher']
  QSslEllipticCurve = WAIT['QSslEllipticCurve']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSslSocketPrivate(QTcpSocketPrivate):
  """
  The cute side of Qt's QSslSocketPrivate: a plain Python object standing in
  front of one C++ QSslSocketPrivate.

  It is built on the cute 'QTcpSocketPrivate', as Qt's QSslSocketPrivate is
  built on Qt's QTcpSocketPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSslSocketPrivate that has a ritual and that Python
  can call so far, 66 names in all: 'q_func', 'init',
  'verifyProtocolSupported', 'supportsSsl', 'ensureInitialized',
  'defaultCiphers', 'defaultDtlsCiphers', 'supportedCiphers',
  'setDefaultCiphers', 'setDefaultDtlsCiphers', 'setDefaultSupportedCiphers',
  'supportedEllipticCurves', 'setDefaultSupportedEllipticCurves',
  'resetDefaultEllipticCurves', 'defaultCaCertificates',
  'systemCaCertificates', 'setDefaultCaCertificates',
  'addDefaultCaCertificate', 'addDefaultCaCertificates',
  'isMatchingHostname', 'createPlainSocket', 'pauseSocketNotifiers',
  'resumeSocketNotifiers', 'isPaused', 'setPaused', 'bind',
  '_q_connectedSlot', '_q_hostFoundSlot', '_q_disconnectedSlot',
  '_q_stateChangedSlot', '_q_errorSlot', '_q_readyReadSlot',
  '_q_channelReadyReadSlot', '_q_bytesWrittenSlot',
  '_q_channelBytesWrittenSlot', '_q_readChannelFinishedSlot',
  '_q_flushWriteBuffer', '_q_flushReadBuffer', '_q_resumeImplementation',
  'unixRootCertDirectories', 'peek', 'flush', 'startClientEncryption',
  'startServerEncryption', 'transmit', 'disconnectFromHost', 'disconnected',
  'sessionCipher', 'sessionProtocol', 'continueHandshake',
  'rootCertOnDemandLoadingSupported', 'setRootCertOnDemandLoadingSupported',
  'tlsBackendInUse', 'tlsMode', 'isRootsOnDemandAllowed', 'verificationName',
  'tlsHostName', 'plainTcpSocket', 'verifyErrorsHaveBeenIgnored',
  'isAutoStartingHandshake', 'isPendingClose', 'setPendingClose',
  'maxReadBufferSize', 'setMaxReadBufferSize', 'setEncrypted',
  'hasUndecryptedData'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSslSocket *QSslSocketPrivate::q_func() const': takes in
    Python what 'QSslSocket *QSslSocketPrivate::q_func()' takes.
  - Qt's 'QSslSocketPrivate::~QSslSocketPrivate()': the destructor: Python
    never removes a C++ QSslSocketPrivate.
  - Qt's 'void QSslSocketPrivate::checkSettingSslContext(QSslSocket *a0,
    std::shared_ptr<QSslContext> a1)': takes a type Python has no way to hand
    over yet.
  - Qt's 'std::shared_ptr<QSslContext>
    QSslSocketPrivate::sslContext(QSslSocket *socket)': gives a type Python
    has no way to take yet.
  - Qt's 'qint64 QSslSocketPrivate::peek(char *data, qint64 maxSize)': names
    'char', which has no cute class yet.
  - Qt's 'QRingBufferRef &QSslSocketPrivate::tlsWriteBuffer()': gives a type
    Python has no way to take yet.
  - Qt's 'QRingBufferRef &QSslSocketPrivate::tlsBuffer()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 77 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QSslSocketPrivate is created at the first use, not by
    'QSslSocketPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSslSocketPrivate.
  - Each name of Qt's QSslSocketPrivate that has no cute function yet,
    'checkSettingSslContext', 'readyReadPointer', 'sslContext', 'tlsBuffer',
    'tlsEmittedBytesWritten', 'tlsWriteBuffer', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def supportsSsl() -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::supportsSsl()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocketprivate.html#supportsSsl
    """
    #  bool QSslSocketPrivate::supportsSsl()
    return Rituals.call('ritual_ZN17QSslSocketPrivate11supportsSslEv')

  @staticmethod
  def ensureInitialized() -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::ensureInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#ensureInitialized
    """
    #  void QSslSocketPrivate::ensureInitialized()
    Rituals.call('ritual_ZN17QSslSocketPrivate17ensureInitializedEv')

  @staticmethod
  def defaultCiphers() -> QList[QSslCipher]:
    """
    Calls Qt's 'QList<QSslCipher> QSslSocketPrivate::defaultCiphers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#defaultCiphers

    Returns
    -------

    QList[QSslCipher]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCipher> QSslSocketPrivate::defaultCiphers()
    address = Rituals.call('ritual_ZN17QSslSocketPrivate14defaultCiphersEv')
    from . import QSslCipher
    return QList[QSslCipher]._cuteOwning(address)

  @staticmethod
  def defaultDtlsCiphers() -> QList[QSslCipher]:
    """
    Calls Qt's 'QList<QSslCipher> QSslSocketPrivate::defaultDtlsCiphers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#defaultDtlsCiphers

    Returns
    -------

    QList[QSslCipher]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCipher> QSslSocketPrivate::defaultDtlsCiphers()
    address = Rituals.call(
        'ritual_ZN17QSslSocketPrivate18defaultDtlsCiphersEv',
    )
    from . import QSslCipher
    return QList[QSslCipher]._cuteOwning(address)

  @staticmethod
  def supportedCiphers() -> QList[QSslCipher]:
    """
    Calls Qt's 'QList<QSslCipher> QSslSocketPrivate::supportedCiphers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#supportedCiphers

    Returns
    -------

    QList[QSslCipher]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCipher> QSslSocketPrivate::supportedCiphers()
    address = Rituals.call(
        'ritual_ZN17QSslSocketPrivate16supportedCiphersEv',
    )
    from . import QSslCipher
    return QList[QSslCipher]._cuteOwning(address)

  @staticmethod
  @overload(QList[QSslCipher])
  def setDefaultCiphers(ciphers: QList[QSslCipher]) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::setDefaultCiphers(const
    QList<QSslCipher> &ciphers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#setDefaultCiphers

    Parameters
    ----------

    ciphers : QList[QSslCipher]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslSocketPrivate::setDefaultCiphers(const QList<QSslCipher>
    #      &ciphers)
    Rituals.call(
        'ritual_ZN17QSslSocketPrivate17setDefaultCiphersERK5QListI10QSslCip'
        'herE',
        CuteMixin._valueOf(ciphers),
    )

  @staticmethod
  @overload(QList[QSslCipher])
  def setDefaultDtlsCiphers(ciphers: QList[QSslCipher]) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::setDefaultDtlsCiphers(const
    QList<QSslCipher> &ciphers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#setDefaultDtlsCiphers

    Parameters
    ----------

    ciphers : QList[QSslCipher]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslSocketPrivate::setDefaultDtlsCiphers(const QList<QSslCipher>
    #      &ciphers)
    Rituals.call(
        'ritual_ZN17QSslSocketPrivate21setDefaultDtlsCiphersERK5QListI10QSs'
        'lCipherE',
        CuteMixin._valueOf(ciphers),
    )

  @staticmethod
  @overload(QList[QSslCipher])
  def setDefaultSupportedCiphers(ciphers: QList[QSslCipher]) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::setDefaultSupportedCiphers(const
    QList<QSslCipher> &ciphers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#setDefaultSupportedCiphers

    Parameters
    ----------

    ciphers : QList[QSslCipher]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslSocketPrivate::setDefaultSupportedCiphers(const
    #      QList<QSslCipher> &ciphers)
    Rituals.call(
        'ritual_ZN17QSslSocketPrivate26setDefaultSupportedCiphersERK5QListI'
        '10QSslCipherE',
        CuteMixin._valueOf(ciphers),
    )

  @staticmethod
  def supportedEllipticCurves() -> QList[QSslEllipticCurve]:
    """
    Calls Qt's 'QList<QSslEllipticCurve>
    QSslSocketPrivate::supportedEllipticCurves()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#supportedEllipticCurves

    Returns
    -------

    QList[QSslEllipticCurve]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslEllipticCurve> QSslSocketPrivate::supportedEllipticCurves()
    address = Rituals.call(
        'ritual_ZN17QSslSocketPrivate23supportedEllipticCurvesEv',
    )
    from . import QSslEllipticCurve
    return QList[QSslEllipticCurve]._cuteOwning(address)

  @staticmethod
  @overload(QList[QSslEllipticCurve])
  def setDefaultSupportedEllipticCurves(
      curves: QList[QSslEllipticCurve],
  ) -> None:
    """
    Calls Qt's 'void
    QSslSocketPrivate::setDefaultSupportedEllipticCurves(const
    QList<QSslEllipticCurve> &curves)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html

    Parameters
    ----------

    curves : QList[QSslEllipticCurve]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslSocketPrivate::setDefaultSupportedEllipticCurves(const
    #      QList<QSslEllipticCurve> &curves)
    Rituals.call(
        'ritual_ZN17QSslSocketPrivate33setDefaultSupportedEllipticCurvesERK'
        '5QListI17QSslEllipticCurveE',
        CuteMixin._valueOf(curves),
    )

  @staticmethod
  def resetDefaultEllipticCurves() -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::resetDefaultEllipticCurves()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#resetDefaultEllipticCurves
    """
    #  void QSslSocketPrivate::resetDefaultEllipticCurves()
    Rituals.call(
        'ritual_ZN17QSslSocketPrivate26resetDefaultEllipticCurvesEv',
    )

  @staticmethod
  def defaultCaCertificates() -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate>
    QSslSocketPrivate::defaultCaCertificates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#defaultCaCertificates

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QSslSocketPrivate::defaultCaCertificates()
    address = Rituals.call(
        'ritual_ZN17QSslSocketPrivate21defaultCaCertificatesEv',
    )
    from . import QSslCertificate
    return QList[QSslCertificate]._cuteOwning(address)

  @staticmethod
  def systemCaCertificates() -> QList[QSslCertificate]:
    """
    Calls Qt's 'QList<QSslCertificate>
    QSslSocketPrivate::systemCaCertificates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#systemCaCertificates

    Returns
    -------

    QList[QSslCertificate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslCertificate> QSslSocketPrivate::systemCaCertificates()
    address = Rituals.call(
        'ritual_ZN17QSslSocketPrivate20systemCaCertificatesEv',
    )
    from . import QSslCertificate
    return QList[QSslCertificate]._cuteOwning(address)

  @staticmethod
  @overload(QList[QSslCertificate])
  def setDefaultCaCertificates(certs: QList[QSslCertificate]) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::setDefaultCaCertificates(const
    QList<QSslCertificate> &certs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#setDefaultCaCertificates

    Parameters
    ----------

    certs : QList[QSslCertificate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslSocketPrivate::setDefaultCaCertificates(const
    #      QList<QSslCertificate> &certs)
    Rituals.call(
        'ritual_ZN17QSslSocketPrivate24setDefaultCaCertificatesERK5QListI15'
        'QSslCertificateE',
        CuteMixin._valueOf(certs),
    )

  @staticmethod
  @overload(QSslCertificate)
  def addDefaultCaCertificate(cert: QSslCertificate) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::addDefaultCaCertificate(const
    QSslCertificate &cert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#addDefaultCaCertificate

    Parameters
    ----------

    cert : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.
    """
    #  void QSslSocketPrivate::addDefaultCaCertificate(const QSslCertificate
    #      &cert)
    Rituals.call(
        'ritual_ZN17QSslSocketPrivate23addDefaultCaCertificateERK15QSslCert'
        'ificate',
        CuteMixin._valueOf(cert),
    )

  @staticmethod
  @overload(QList[QSslCertificate])
  def addDefaultCaCertificates(certs: QList[QSslCertificate]) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::addDefaultCaCertificates(const
    QList<QSslCertificate> &certs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#addDefaultCaCertificates

    Parameters
    ----------

    certs : QList[QSslCertificate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSslSocketPrivate::addDefaultCaCertificates(const
    #      QList<QSslCertificate> &certs)
    Rituals.call(
        'ritual_ZN17QSslSocketPrivate24addDefaultCaCertificatesERK5QListI15'
        'QSslCertificateE',
        CuteMixin._valueOf(certs),
    )

  @staticmethod
  @overload(QSslCertificate, str)
  def isMatchingHostname(cert: QSslCertificate, peerName: str) -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::isMatchingHostname(const
    QSslCertificate &cert, const QString &peerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#isMatchingHostname

    Parameters
    ----------

    cert : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.

    peerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSslSocketPrivate::isMatchingHostname(const QSslCertificate
    #      &cert, const QString &peerName)
    return Rituals.call(
        'ritual_ZN17QSslSocketPrivate18isMatchingHostnameERK15QSslCertifica'
        'teRK7QString',
        CuteMixin._valueOf(cert), peerName,
    )

  @staticmethod
  @overload(str, str)
  def isMatchingHostname(cn: str, hostname: str) -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::isMatchingHostname(const QString &cn,
    const QString &hostname)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#isMatchingHostname

    Parameters
    ----------

    cn : str
      Passed on as it is: a QString is made of it for the call.

    hostname : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSslSocketPrivate::isMatchingHostname(const QString &cn, const
    #      QString &hostname)
    return Rituals.call(
        'ritual_ZN17QSslSocketPrivate18isMatchingHostnameERK7QStringS2_',
        cn, hostname,
    )

  @staticmethod
  @overload(QSslSocket)
  @overload(NoneType)
  def pauseSocketNotifiers(a0: Optional[QSslSocket]) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::pauseSocketNotifiers(QSslSocket
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#pauseSocketNotifiers

    Parameters
    ----------

    a0 : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSslSocketPrivate::pauseSocketNotifiers(QSslSocket *a0)
    Rituals.call(
        'ritual_ZN17QSslSocketPrivate20pauseSocketNotifiersEP10QSslSocket',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(QSslSocket)
  @overload(NoneType)
  def resumeSocketNotifiers(a0: Optional[QSslSocket]) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::resumeSocketNotifiers(QSslSocket
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#resumeSocketNotifiers

    Parameters
    ----------

    a0 : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSslSocketPrivate::resumeSocketNotifiers(QSslSocket *a0)
    Rituals.call(
        'ritual_ZN17QSslSocketPrivate21resumeSocketNotifiersEP10QSslSocket',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  def unixRootCertDirectories() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray>
    QSslSocketPrivate::unixRootCertDirectories()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#unixRootCertDirectories

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QSslSocketPrivate::unixRootCertDirectories()
    address = Rituals.call(
        'ritual_ZN17QSslSocketPrivate23unixRootCertDirectoriesEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @staticmethod
  def rootCertOnDemandLoadingSupported() -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::rootCertOnDemandLoadingSupported()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html
    """
    #  bool QSslSocketPrivate::rootCertOnDemandLoadingSupported()
    return Rituals.call(
        'ritual_ZN17QSslSocketPrivate32rootCertOnDemandLoadingSupportedEv',
    )

  @staticmethod
  @overload(bool)
  def setRootCertOnDemandLoadingSupported(supported: bool) -> None:
    """
    Calls Qt's 'void
    QSslSocketPrivate::setRootCertOnDemandLoadingSupported(bool supported)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html

    Parameters
    ----------

    supported : bool
      Passed on as it is.
    """
    #  void QSslSocketPrivate::setRootCertOnDemandLoadingSupported(bool
    #      supported)
    Rituals.call(
        'ritual_ZN17QSslSocketPrivate35setRootCertOnDemandLoadingSupportedE'
        'b',
        supported,
    )

  @staticmethod
  def tlsBackendInUse() -> Optional[QTlsBackend]:
    """
    Calls Qt's 'QTlsBackend *QSslSocketPrivate::tlsBackendInUse()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#tlsBackendInUse

    Returns
    -------

    Optional[QTlsBackend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTlsBackend *QSslSocketPrivate::tlsBackendInUse()
    address = Rituals.call('ritual_ZN17QSslSocketPrivate15tlsBackendInUseEv')
    from . import QTlsBackend
    return QTlsBackend._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslSocketPrivate'

  #  A C++ QSslSocketPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSslSocketPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::isPaused() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocketprivate.html#isPaused
    """
    #  bool QSslSocketPrivate::isPaused() const
    return self.uglySide.call('ritual_ZNK17QSslSocketPrivate8isPausedEv')

  def sessionCipher(self) -> QSslCipher:
    """
    Calls Qt's 'QSslCipher QSslSocketPrivate::sessionCipher() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#sessionCipher

    Returns
    -------

    QSslCipher
      A new cute QSslCipher around the copy Qt gave back. Python owns it.
    """
    #  QSslCipher QSslSocketPrivate::sessionCipher() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslSocketPrivate13sessionCipherEv',
    )
    from . import QSslCipher
    return QSslCipher._cuteOwning(address)

  def sessionProtocol(self) -> QSsl.SslProtocol:
    """
    Calls Qt's 'QSsl::SslProtocol QSslSocketPrivate::sessionProtocol()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#sessionProtocol

    Returns
    -------

    QSsl.SslProtocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.SslProtocol(number)'
      gives.
    """
    #  QSsl::SslProtocol QSslSocketPrivate::sessionProtocol() const
    return QSsl.SslProtocol(self.uglySide.call(
        'ritual_ZNK17QSslSocketPrivate15sessionProtocolEv',
    ))

  def tlsMode(self) -> QSslSocket.SslMode:
    """
    Calls Qt's 'QSslSocket::SslMode QSslSocketPrivate::tlsMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocketprivate.html#tlsMode

    Returns
    -------

    QSslSocket.SslMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSslSocket.SslMode(number)' gives.
    """
    #  QSslSocket::SslMode QSslSocketPrivate::tlsMode() const
    return QSslSocket.SslMode(self.uglySide.call(
        'ritual_ZNK17QSslSocketPrivate7tlsModeEv',
    ))

  def isRootsOnDemandAllowed(self) -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::isRootsOnDemandAllowed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#isRootsOnDemandAllowed
    """
    #  bool QSslSocketPrivate::isRootsOnDemandAllowed() const
    return self.uglySide.call(
        'ritual_ZNK17QSslSocketPrivate22isRootsOnDemandAllowedEv',
    )

  def verificationName(self) -> str:
    """
    Calls Qt's 'QString QSslSocketPrivate::verificationName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#verificationName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslSocketPrivate::verificationName() const
    return self.uglySide.call(
        'ritual_ZNK17QSslSocketPrivate16verificationNameEv',
    )

  def tlsHostName(self) -> str:
    """
    Calls Qt's 'QString QSslSocketPrivate::tlsHostName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocketprivate.html#tlsHostName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSslSocketPrivate::tlsHostName() const
    return self.uglySide.call('ritual_ZNK17QSslSocketPrivate11tlsHostNameEv')

  def plainTcpSocket(self) -> Optional[QTcpSocket]:
    """
    Calls Qt's 'QTcpSocket *QSslSocketPrivate::plainTcpSocket() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#plainTcpSocket

    Returns
    -------

    Optional[QTcpSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTcpSocket *QSslSocketPrivate::plainTcpSocket() const
    address = self.uglySide.call(
        'ritual_ZNK17QSslSocketPrivate14plainTcpSocketEv',
    )
    from . import QTcpSocket
    return QTcpSocket._cuteAt(address)

  def isAutoStartingHandshake(self) -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::isAutoStartingHandshake() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#isAutoStartingHandshake
    """
    #  bool QSslSocketPrivate::isAutoStartingHandshake() const
    return self.uglySide.call(
        'ritual_ZNK17QSslSocketPrivate23isAutoStartingHandshakeEv',
    )

  def isPendingClose(self) -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::isPendingClose() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#isPendingClose
    """
    #  bool QSslSocketPrivate::isPendingClose() const
    return self.uglySide.call(
        'ritual_ZNK17QSslSocketPrivate14isPendingCloseEv',
    )

  def maxReadBufferSize(self) -> int:
    """
    Calls Qt's 'qint64 QSslSocketPrivate::maxReadBufferSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#maxReadBufferSize
    """
    #  qint64 QSslSocketPrivate::maxReadBufferSize() const
    return self.uglySide.call(
        'ritual_ZNK17QSslSocketPrivate17maxReadBufferSizeEv',
    )

  def hasUndecryptedData(self) -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::hasUndecryptedData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#hasUndecryptedData
    """
    #  bool QSslSocketPrivate::hasUndecryptedData() const
    return self.uglySide.call(
        'ritual_ZNK17QSslSocketPrivate18hasUndecryptedDataEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setPaused(self, p: bool) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::setPaused(bool p)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocketprivate.html#setPaused

    Parameters
    ----------

    p : bool
      Passed on as it is.
    """
    #  void QSslSocketPrivate::setPaused(bool p)
    self.uglySide.call('ritual_ZN17QSslSocketPrivate9setPausedEb', p)

  @overload(bool)
  def setPendingClose(self, pc: bool) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::setPendingClose(bool pc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#setPendingClose

    Parameters
    ----------

    pc : bool
      Passed on as it is.
    """
    #  void QSslSocketPrivate::setPendingClose(bool pc)
    self.uglySide.call('ritual_ZN17QSslSocketPrivate15setPendingCloseEb', pc)

  @overload(int)
  def setMaxReadBufferSize(self, maxSize: int) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::setMaxReadBufferSize(qint64
    maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#setMaxReadBufferSize

    Parameters
    ----------

    maxSize : int
      Passed on as it is.
    """
    #  void QSslSocketPrivate::setMaxReadBufferSize(qint64 maxSize)
    self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate20setMaxReadBufferSizeEx', maxSize,
    )

  @overload(bool)
  def setEncrypted(self, enc: bool) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::setEncrypted(bool enc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#setEncrypted

    Parameters
    ----------

    enc : bool
      Passed on as it is.
    """
    #  void QSslSocketPrivate::setEncrypted(bool enc)
    self.uglySide.call('ritual_ZN17QSslSocketPrivate12setEncryptedEb', enc)

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
    Notes what was given, for Qt's 'QSslSocketPrivate::QSslSocketPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#QSslSocketPrivate
    """
    #  QSslSocketPrivate::QSslSocketPrivate()
    self._noteCreation(QSslSocketPrivate, lambda: Rituals.call(
        'ritual_ZN17QSslSocketPrivateC1Ev',
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

  def q_func(self) -> Optional[QSslSocket]:
    """
    Calls Qt's 'QSslSocket *QSslSocketPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocketprivate.html#q_func

    Returns
    -------

    Optional[QSslSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSslSocket *QSslSocketPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QSslSocketPrivate6q_funcEv')
    return QSslSocket._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocketprivate.html#init
    """
    #  void QSslSocketPrivate::init()
    self.uglySide.call('ritual_ZN17QSslSocketPrivate4initEv')

  @overload(str)
  @overload(NoneType)
  def verifyProtocolSupported(self, where: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::verifyProtocolSupported(const char
    *where)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#verifyProtocolSupported

    Parameters
    ----------

    where : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QSslSocketPrivate::verifyProtocolSupported(const char *where)
    return self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate23verifyProtocolSupportedEPKc',
        self._bytesOf(where),
    )

  @overload(QIODeviceBase.OpenMode)
  def createPlainSocket(self, openMode: QIODeviceBase.OpenMode) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::createPlainSocket(QIODevice::OpenMode
    openMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#createPlainSocket

    Parameters
    ----------

    openMode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  void QSslSocketPrivate::createPlainSocket(QIODevice::OpenMode
    #      openMode)
    self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate17createPlainSocketE6QFlagsIN13QIODevi'
        'ceBase12OpenModeFlagEE',
        openMode.value,
    )

  @overload(QHostAddress, int, QAbstractSocket.BindMode)
  @overload(QHostAddress, int, QAbstractSocket.BindMode, QNetworkInterface)
  @overload(QHostAddress, int, QAbstractSocket.BindMode, NoneType)
  def bind(
      self,
      address: QHostAddress,
      a1: int,
      a2: QAbstractSocket.BindMode,
      iface: Optional[QNetworkInterface] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::bind(const QHostAddress &address,
    quint16 a1, QAbstractSocket::BindMode a2, const QNetworkInterface
    *iface)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocketprivate.html#bind

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : QAbstractSocket.BindMode
      Passed on as its number.

    iface : Optional[QNetworkInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QSslSocketPrivate::bind(const QHostAddress &address, quint16 a1,
    #      QAbstractSocket::BindMode a2, const QNetworkInterface *iface)
    ritual = (
        'ritual_ZN17QSslSocketPrivate4bindERK12QHostAddresst6QFlagsIN15QAbs'
        'tractSocket8BindFlagEEPK17QNetworkInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSslSocketPrivate4bindERK12QHostAddresst6QFlagsIN'
          '15QAbstractSocket8BindFlagEEPK17QNetworkInterface')
    return self.uglySide.call(
        ritual, self._valueOf(address), a1, a2.value, self._addressOf(iface),
    )

  def _q_connectedSlot(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::_q_connectedSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_connectedSlot
    """
    #  void QSslSocketPrivate::_q_connectedSlot()
    self.uglySide.call('ritual_ZN17QSslSocketPrivate16_q_connectedSlotEv')

  def _q_hostFoundSlot(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::_q_hostFoundSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_hostFoundSlot
    """
    #  void QSslSocketPrivate::_q_hostFoundSlot()
    self.uglySide.call('ritual_ZN17QSslSocketPrivate16_q_hostFoundSlotEv')

  def _q_disconnectedSlot(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::_q_disconnectedSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_disconnectedSlot
    """
    #  void QSslSocketPrivate::_q_disconnectedSlot()
    self.uglySide.call('ritual_ZN17QSslSocketPrivate19_q_disconnectedSlotEv')

  @overload(QAbstractSocket.SocketState)
  def _q_stateChangedSlot(self, a0: QAbstractSocket.SocketState) -> None:
    """
    Calls Qt's 'void
    QSslSocketPrivate::_q_stateChangedSlot(QAbstractSocket::SocketState a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_stateChangedSlot

    Parameters
    ----------

    a0 : QAbstractSocket.SocketState
      Passed on as its number.
    """
    #  void QSslSocketPrivate::_q_stateChangedSlot(QAbstractSocket::
    #      SocketState a0)
    self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate19_q_stateChangedSlotEN15QAbstractSock'
        'et11SocketStateE',
        a0.value,
    )

  @overload(QAbstractSocket.SocketError)
  def _q_errorSlot(self, a0: QAbstractSocket.SocketError) -> None:
    """
    Calls Qt's 'void
    QSslSocketPrivate::_q_errorSlot(QAbstractSocket::SocketError a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_errorSlot

    Parameters
    ----------

    a0 : QAbstractSocket.SocketError
      Passed on as its number.
    """
    #  void QSslSocketPrivate::_q_errorSlot(QAbstractSocket::SocketError a0)
    self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate12_q_errorSlotEN15QAbstractSocket11Soc'
        'ketErrorE',
        a0.value,
    )

  def _q_readyReadSlot(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::_q_readyReadSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_readyReadSlot
    """
    #  void QSslSocketPrivate::_q_readyReadSlot()
    self.uglySide.call('ritual_ZN17QSslSocketPrivate16_q_readyReadSlotEv')

  @overload(int)
  def _q_channelReadyReadSlot(self, a0: int) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::_q_channelReadyReadSlot(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_channelReadyReadSlot

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSslSocketPrivate::_q_channelReadyReadSlot(int a0)
    self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate23_q_channelReadyReadSlotEi', a0,
    )

  @overload(int)
  def _q_bytesWrittenSlot(self, a0: int) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::_q_bytesWrittenSlot(qint64 a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_bytesWrittenSlot

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSslSocketPrivate::_q_bytesWrittenSlot(qint64 a0)
    self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate19_q_bytesWrittenSlotEx', a0,
    )

  @overload(int, int)
  def _q_channelBytesWrittenSlot(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::_q_channelBytesWrittenSlot(int a0,
    qint64 a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_channelBytesWrittenSlot

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QSslSocketPrivate::_q_channelBytesWrittenSlot(int a0, qint64 a1)
    self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate26_q_channelBytesWrittenSlotEix',
        a0, a1,
    )

  def _q_readChannelFinishedSlot(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::_q_readChannelFinishedSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_readChannelFinishedSlot
    """
    #  void QSslSocketPrivate::_q_readChannelFinishedSlot()
    self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate26_q_readChannelFinishedSlotEv',
    )

  def _q_flushWriteBuffer(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::_q_flushWriteBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_flushWriteBuffer
    """
    #  void QSslSocketPrivate::_q_flushWriteBuffer()
    self.uglySide.call('ritual_ZN17QSslSocketPrivate19_q_flushWriteBufferEv')

  def _q_flushReadBuffer(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::_q_flushReadBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_flushReadBuffer
    """
    #  void QSslSocketPrivate::_q_flushReadBuffer()
    self.uglySide.call('ritual_ZN17QSslSocketPrivate18_q_flushReadBufferEv')

  def _q_resumeImplementation(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::_q_resumeImplementation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#_q_resumeImplementation
    """
    #  void QSslSocketPrivate::_q_resumeImplementation()
    self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate23_q_resumeImplementationEv',
    )

  @overload(int)
  def peek(self, maxSize: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslSocketPrivate::peek(qint64 maxSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocketprivate.html#peek

    Parameters
    ----------

    maxSize : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslSocketPrivate::peek(qint64 maxSize)
    ritual = 'ritual_ZN17QSslSocketPrivate4peekEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSslSocketPrivate4peekEx'
    address = self.uglySide.call(ritual, maxSize)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def flush(self) -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocketprivate.html#flush
    """
    #  bool QSslSocketPrivate::flush()
    ritual = 'ritual_ZN17QSslSocketPrivate5flushEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSslSocketPrivate5flushEv'
    return self.uglySide.call(ritual)

  def startClientEncryption(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::startClientEncryption()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#startClientEncryption
    """
    #  void QSslSocketPrivate::startClientEncryption()
    self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate21startClientEncryptionEv',
    )

  def startServerEncryption(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::startServerEncryption()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#startServerEncryption
    """
    #  void QSslSocketPrivate::startServerEncryption()
    self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate21startServerEncryptionEv',
    )

  def transmit(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::transmit()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslsocketprivate.html#transmit
    """
    #  void QSslSocketPrivate::transmit()
    self.uglySide.call('ritual_ZN17QSslSocketPrivate8transmitEv')

  def disconnectFromHost(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::disconnectFromHost()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#disconnectFromHost
    """
    #  void QSslSocketPrivate::disconnectFromHost()
    self.uglySide.call('ritual_ZN17QSslSocketPrivate18disconnectFromHostEv')

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::disconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#disconnected
    """
    #  void QSslSocketPrivate::disconnected()
    self.uglySide.call('ritual_ZN17QSslSocketPrivate12disconnectedEv')

  def continueHandshake(self) -> None:
    """
    Calls Qt's 'void QSslSocketPrivate::continueHandshake()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#continueHandshake
    """
    #  void QSslSocketPrivate::continueHandshake()
    self.uglySide.call('ritual_ZN17QSslSocketPrivate17continueHandshakeEv')

  def verifyErrorsHaveBeenIgnored(self) -> bool:
    """
    Calls Qt's 'bool QSslSocketPrivate::verifyErrorsHaveBeenIgnored()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslsocketprivate.html#verifyErrorsHaveBeenIgnored
    """
    #  bool QSslSocketPrivate::verifyErrorsHaveBeenIgnored()
    return self.uglySide.call(
        'ritual_ZN17QSslSocketPrivate27verifyErrorsHaveBeenIgnoredEv',
    )

  @staticmethod
  def checkSettingSslContext(*__, **_) -> Never:
    """
    Qt's 'void QSslSocketPrivate::checkSettingSslContext(QSslSocket *a0,
    std::shared_ptr<QSslContext> a1)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSslSocketPrivate.checkSettingSslContext' has no cute function "
        "yet. Qt's 'void "
        "QSslSocketPrivate::checkSettingSslContext(QSslSocket *a0, "
        "std::shared_ptr<QSslContext> a1)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def readyReadPointer(*__, **_) -> Never:
    """
    Qt's 'bool *QSslSocketPrivate::readyReadPointer()': takes or gives a type
    that cannot be passed yet: bool *.
    """
    raise NotImplementedError(
        "'QSslSocketPrivate.readyReadPointer' has no cute function yet. "
        "Qt's 'bool *QSslSocketPrivate::readyReadPointer()': takes or gives "
        "a type that cannot be passed yet: bool *.")

  @staticmethod
  def sslContext(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<QSslContext>
    QSslSocketPrivate::sslContext(QSslSocket *socket)': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSslSocketPrivate.sslContext' has no cute function yet. Qt's "
        "'std::shared_ptr<QSslContext> "
        "QSslSocketPrivate::sslContext(QSslSocket *socket)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def tlsBuffer(*__, **_) -> Never:
    """
    Qt's 'QRingBufferRef &QSslSocketPrivate::tlsBuffer()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSslSocketPrivate.tlsBuffer' has no cute function yet. Qt's "
        "'QRingBufferRef &QSslSocketPrivate::tlsBuffer()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def tlsEmittedBytesWritten(*__, **_) -> Never:
    """
    Qt's 'bool &QSslSocketPrivate::tlsEmittedBytesWritten()': takes or gives
    a type that cannot be passed yet: bool &.
    """
    raise NotImplementedError(
        "'QSslSocketPrivate.tlsEmittedBytesWritten' has no cute function "
        "yet. Qt's 'bool &QSslSocketPrivate::tlsEmittedBytesWritten()': "
        "takes or gives a type that cannot be passed yet: bool &.")

  @staticmethod
  def tlsWriteBuffer(*__, **_) -> Never:
    """
    Qt's 'QRingBufferRef &QSslSocketPrivate::tlsWriteBuffer()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSslSocketPrivate.tlsWriteBuffer' has no cute function yet. Qt's "
        "'QRingBufferRef &QSslSocketPrivate::tlsWriteBuffer()': gives a "
        "type Python has no way to take yet.")
