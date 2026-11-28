"""
QTlsPrivate::TlsCryptograph binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTlsPrivate::TlsCryptograph to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QSsl, QAbstractSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QOcspResponse, QSslCertificate, QSslCipher, QSslError
  from . import QSslSocket, QSslSocketPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSslCertificate = WAIT['QSslCertificate']
  QSslSocket = WAIT['QSslSocket']
  QSslSocketPrivate = WAIT['QSslSocketPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class TlsCryptograph(QObject):
  """
  The cute side of Qt's QTlsPrivate::TlsCryptograph: a plain Python object
  standing in front of one C++ QTlsPrivate::TlsCryptograph.

  It is built on the cute 'QObject', as Qt's QTlsPrivate::TlsCryptograph is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTlsPrivate::TlsCryptograph that has a ritual and
  that Python can call so far, 16 names in all: 'init', 'tlsErrors',
  'startClientEncryption', 'startServerEncryption', 'continueHandshake',
  'enableHandshakeContinuation', 'disconnectFromHost', 'disconnected',
  'cancelCAFetch', 'sessionCipher', 'sessionProtocol', 'transmit',
  'hasUndecryptedData', 'ocsps', 'isMatchingHostname', 'setErrorAndEmit'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTlsPrivate::TlsCryptograph::~TlsCryptograph()': the destructor:
    Python never removes a C++ QTlsPrivate::TlsCryptograph.
  - Qt's 'void QTlsPrivate::TlsCryptograph::checkSettingSslContext(std::
    shared_ptr<QSslContext> tlsContext)': takes a type Python has no way to
    hand over yet.
  - Qt's 'std::shared_ptr<QSslContext>
    QTlsPrivate::TlsCryptograph::sslContext() const': gives a type Python has
    no way to take yet.

  What to expect
  --------------

  - The C++ QTlsPrivate::TlsCryptograph is created at the first use, not by
    'QTlsPrivate::TlsCryptograph(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTlsPrivate::TlsCryptograph.
  - Qt tells when it has removed the C++ QTlsPrivate::TlsCryptograph. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QTlsPrivate::TlsCryptograph that has no cute function
    yet, 'checkSettingSslContext', 'sslContext', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSslCertificate, str)
  def isMatchingHostname(cert: QSslCertificate, peerName: str) -> bool:
    """
    Calls Qt's 'bool QTlsPrivate::TlsCryptograph::isMatchingHostname(const
    QSslCertificate &cert, const QString &peerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#isMatchingHostname

    Parameters
    ----------

    cert : QSslCertificate
      Passed on as a value: Qt reads the C++ QSslCertificate, which stays
      Python's own.

    peerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QTlsPrivate::TlsCryptograph::isMatchingHostname(const
    #      QSslCertificate &cert, const QString &peerName)
    return Rituals.call(
        'ritual_ZN11QTlsPrivate14TlsCryptograph18isMatchingHostnameERK15QSs'
        'lCertificateRK7QString',
        CuteMixin._valueOf(cert), peerName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTlsPrivate::TlsCryptograph'

  #  A C++ QTlsPrivate::TlsCryptograph Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTlsPrivate_TlsCryptograph'

  #  The functions Qt calls itself that QTlsPrivate::TlsCryptograph is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'checkSettingSslContext': (
          'void '
          'QTlsPrivate::TlsCryptograph::checkSettingSslContext(std::shared_'
          'ptr<QSslContext>)',
      ),
      'sslContext': (
          'std::shared_ptr<QSslContext> '
          'QTlsPrivate::TlsCryptograph::sslContext() const',
      ),
      'tlsErrors': (
          'QList<QSslError> QTlsPrivate::TlsCryptograph::tlsErrors() const',
      ),
      'ocsps': (
          'QList<QOcspResponse> QTlsPrivate::TlsCryptograph::ocsps() const',
      ),
  }

  #  The functions Qt calls itself that QTlsPrivate::TlsCryptograph is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'init': (
          ('_ZN11QTlsPrivate14TlsCryptograph4initEP10QSslSocketP17QSslSocke'
           'tPrivate',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtNetwork:QSslSocket'),
               ('address', 'address', 'QtNetwork:QSslSocketPrivate'),
           )),
      ),
      'startClientEncryption': (
          ('_ZN11QTlsPrivate14TlsCryptograph21startClientEncryptionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'startServerEncryption': (
          ('_ZN11QTlsPrivate14TlsCryptograph21startServerEncryptionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'continueHandshake': (
          ('_ZN11QTlsPrivate14TlsCryptograph17continueHandshakeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'enableHandshakeContinuation': (
          ('_ZN11QTlsPrivate14TlsCryptograph27enableHandshakeContinuationEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'disconnectFromHost': (
          ('_ZN11QTlsPrivate14TlsCryptograph18disconnectFromHostEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'disconnected': (
          ('_ZN11QTlsPrivate14TlsCryptograph12disconnectedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'cancelCAFetch': (
          ('_ZN11QTlsPrivate14TlsCryptograph13cancelCAFetchEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'sessionCipher': (
          ('_ZNK11QTlsPrivate14TlsCryptograph13sessionCipherEv',
           ('address', 'value', 'QtNetwork:QSslCipher'),
           ()),
      ),
      'sessionProtocol': (
          ('_ZNK11QTlsPrivate14TlsCryptograph15sessionProtocolEv',
           ('int', 'enum', 'QtNetwork:QSsl.SslProtocol'),
           ()),
      ),
      'transmit': (
          ('_ZN11QTlsPrivate14TlsCryptograph8transmitEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'hasUndecryptedData': (
          ('_ZNK11QTlsPrivate14TlsCryptograph18hasUndecryptedDataEv',
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

  def tlsErrors(self) -> QList[QSslError]:
    """
    Calls Qt's 'QList<QSslError> QTlsPrivate::TlsCryptograph::tlsErrors()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#tlsErrors

    Returns
    -------

    QList[QSslError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslError> QTlsPrivate::TlsCryptograph::tlsErrors() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate14TlsCryptograph9tlsErrorsEv',
    )
    from . import QSslError
    return QList[QSslError]._cuteOwning(address)

  def sessionCipher(self) -> QSslCipher:
    """
    Calls Qt's 'QSslCipher QTlsPrivate::TlsCryptograph::sessionCipher()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#sessionCipher

    Returns
    -------

    QSslCipher
      A new cute QSslCipher around the copy Qt gave back. Python owns it.
    """
    #  QSslCipher QTlsPrivate::TlsCryptograph::sessionCipher() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate14TlsCryptograph13sessionCipherEv',
    )
    from . import QSslCipher
    return QSslCipher._cuteOwning(address)

  def sessionProtocol(self) -> QSsl.SslProtocol:
    """
    Calls Qt's 'QSsl::SslProtocol
    QTlsPrivate::TlsCryptograph::sessionProtocol() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#sessionProtocol

    Returns
    -------

    QSsl.SslProtocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.SslProtocol(number)'
      gives.
    """
    #  QSsl::SslProtocol QTlsPrivate::TlsCryptograph::sessionProtocol() const
    return QSsl.SslProtocol(self.uglySide.call(
        'ritual_ZNK11QTlsPrivate14TlsCryptograph15sessionProtocolEv',
    ))

  def hasUndecryptedData(self) -> bool:
    """
    Calls Qt's 'bool QTlsPrivate::TlsCryptograph::hasUndecryptedData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#hasUndecryptedData
    """
    #  bool QTlsPrivate::TlsCryptograph::hasUndecryptedData() const
    ritual = 'ritual_ZNK11QTlsPrivate14TlsCryptograph18hasUndecryptedDataEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QTlsPrivate14TlsCryptograph18hasUndecryptedDataE'
          'v')
    return self.uglySide.call(ritual)

  def ocsps(self) -> QList[QOcspResponse]:
    """
    Calls Qt's 'QList<QOcspResponse> QTlsPrivate::TlsCryptograph::ocsps()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#ocsps

    Returns
    -------

    QList[QOcspResponse]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOcspResponse> QTlsPrivate::TlsCryptograph::ocsps() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate14TlsCryptograph5ocspsEv',
    )
    from . import QOcspResponse
    return QList[QOcspResponse]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSslSocketPrivate, QAbstractSocket.SocketError, str)
  @overload(NoneType, QAbstractSocket.SocketError, str)
  def setErrorAndEmit(
      self,
      d: Optional[QSslSocketPrivate],
      errorCode: QAbstractSocket.SocketError,
      errorDescription: str,
  ) -> None:
    """
    Calls Qt's 'void
    QTlsPrivate::TlsCryptograph::setErrorAndEmit(QSslSocketPrivate *d,
    QAbstractSocket::SocketError errorCode, const QString &errorDescription)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#setErrorAndEmit

    Parameters
    ----------

    d : Optional[QSslSocketPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errorCode : QAbstractSocket.SocketError
      Passed on as its number.

    errorDescription : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTlsPrivate::TlsCryptograph::setErrorAndEmit(QSslSocketPrivate
    #      *d, QAbstractSocket::SocketError errorCode, const QString
    #      &errorDescription) const
    self.uglySide.call(
        'ritual_ZNK11QTlsPrivate14TlsCryptograph15setErrorAndEmitEP17QSslSo'
        'cketPrivateN15QAbstractSocket11SocketErrorERK7QString',
        self._addressOf(d), errorCode.value, errorDescription,
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

  @overload(QSslSocket, QSslSocketPrivate)
  @overload(QSslSocket, NoneType)
  @overload(NoneType, QSslSocketPrivate)
  @overload(NoneType, NoneType)
  def init(
      self,
      q: Optional[QSslSocket],
      d: Optional[QSslSocketPrivate],
  ) -> None:
    """
    Calls Qt's 'void QTlsPrivate::TlsCryptograph::init(QSslSocket *q,
    QSslSocketPrivate *d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#init

    Parameters
    ----------

    q : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    d : Optional[QSslSocketPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTlsPrivate::TlsCryptograph::init(QSslSocket *q,
    #      QSslSocketPrivate *d)
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate14TlsCryptograph4initEP10QSslSocketP17QSslSo'
        'cketPrivate',
        self._addressOf(q), self._addressOf(d),
    )

  def startClientEncryption(self) -> None:
    """
    Calls Qt's 'void QTlsPrivate::TlsCryptograph::startClientEncryption()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html
    """
    #  void QTlsPrivate::TlsCryptograph::startClientEncryption()
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate14TlsCryptograph21startClientEncryptionEv',
    )

  def startServerEncryption(self) -> None:
    """
    Calls Qt's 'void QTlsPrivate::TlsCryptograph::startServerEncryption()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html
    """
    #  void QTlsPrivate::TlsCryptograph::startServerEncryption()
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate14TlsCryptograph21startServerEncryptionEv',
    )

  def continueHandshake(self) -> None:
    """
    Calls Qt's 'void QTlsPrivate::TlsCryptograph::continueHandshake()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#continueHandshake
    """
    #  void QTlsPrivate::TlsCryptograph::continueHandshake()
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate14TlsCryptograph17continueHandshakeEv',
    )

  def enableHandshakeContinuation(self) -> None:
    """
    Calls Qt's 'void
    QTlsPrivate::TlsCryptograph::enableHandshakeContinuation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html
    """
    #  void QTlsPrivate::TlsCryptograph::enableHandshakeContinuation()
    ritual = (
        'ritual_ZN11QTlsPrivate14TlsCryptograph27enableHandshakeContinuatio'
        'nEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QTlsPrivate14TlsCryptograph27enableHandshakeConti'
          'nuationEv')
    self.uglySide.call(ritual)

  def disconnectFromHost(self) -> None:
    """
    Calls Qt's 'void QTlsPrivate::TlsCryptograph::disconnectFromHost()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#disconnectFromHost
    """
    #  void QTlsPrivate::TlsCryptograph::disconnectFromHost()
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate14TlsCryptograph18disconnectFromHostEv',
    )

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QTlsPrivate::TlsCryptograph::disconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#disconnected
    """
    #  void QTlsPrivate::TlsCryptograph::disconnected()
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate14TlsCryptograph12disconnectedEv',
    )

  def cancelCAFetch(self) -> None:
    """
    Calls Qt's 'void QTlsPrivate::TlsCryptograph::cancelCAFetch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#cancelCAFetch
    """
    #  void QTlsPrivate::TlsCryptograph::cancelCAFetch()
    ritual = 'ritual_ZN11QTlsPrivate14TlsCryptograph13cancelCAFetchEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QTlsPrivate14TlsCryptograph13cancelCAFetchEv'
    self.uglySide.call(ritual)

  def transmit(self) -> None:
    """
    Calls Qt's 'void QTlsPrivate::TlsCryptograph::transmit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-tlscryptograph.html#transmit
    """
    #  void QTlsPrivate::TlsCryptograph::transmit()
    self.uglySide.call('ritual_ZN11QTlsPrivate14TlsCryptograph8transmitEv')

  @staticmethod
  def checkSettingSslContext(*__, **_) -> Never:
    """
    Qt's 'void QTlsPrivate::TlsCryptograph::checkSettingSslContext(std::
    shared_ptr<QSslContext> tlsContext)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QTlsPrivate.TlsCryptograph.checkSettingSslContext' has no cute "
        "function yet. Qt's 'void "
        "QTlsPrivate::TlsCryptograph::checkSettingSslContext(std::shared_ptr"
        "<QSslContext> tlsContext)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def sslContext(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<QSslContext>
    QTlsPrivate::TlsCryptograph::sslContext() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QTlsPrivate.TlsCryptograph.sslContext' has no cute function yet. "
        "Qt's 'std::shared_ptr<QSslContext> "
        "QTlsPrivate::TlsCryptograph::sslContext() const': gives a type "
        "Python has no way to take yet.")
