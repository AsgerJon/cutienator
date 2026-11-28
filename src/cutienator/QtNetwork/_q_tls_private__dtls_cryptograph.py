"""
QTlsPrivate::DtlsCryptograph binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTlsPrivate::DtlsCryptograph to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import QSsl, QDtls, QSslSocket, QTlsPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from . import QHostAddress, QSslCipher, QSslError, QUdpSocket
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHostAddress = WAIT['QHostAddress']
  QSslError = WAIT['QSslError']
  QUdpSocket = WAIT['QUdpSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DtlsCryptograph(QTlsPrivate.DtlsBase):
  """
  The cute side of Qt's QTlsPrivate::DtlsCryptograph: a plain Python object
  standing in front of one C++ QTlsPrivate::DtlsCryptograph.

  It is built on the cute 'QTlsPrivate::DtlsBase', as Qt's
  QTlsPrivate::DtlsCryptograph is built on Qt's QTlsPrivate::DtlsBase, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QTlsPrivate::DtlsCryptograph that has a ritual and
  that Python can call so far, 22 names in all: 'cryptographMode', 'setPeer',
  'peerAddress', 'peerPort', 'setPeerVerificationName',
  'peerVerificationName', 'setDtlsMtuHint', 'dtlsMtuHint', 'state',
  'isConnectionEncrypted', 'startHandshake', 'handleTimeout',
  'continueHandshake', 'resumeHandshake', 'abortHandshake',
  'sendShutdownAlert', 'peerVerificationErrors', 'ignoreVerificationErrors',
  'dtlsSessionCipher', 'dtlsSessionProtocol', 'writeDatagramEncrypted',
  'decryptDatagram'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What to expect
  --------------

  - The C++ QTlsPrivate::DtlsCryptograph is created at the first use, not by
    'QTlsPrivate::DtlsCryptograph(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTlsPrivate::DtlsCryptograph.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTlsPrivate::DtlsCryptograph'

  #  A C++ QTlsPrivate::DtlsCryptograph Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTlsPrivate_DtlsCryptograph'

  #  The functions Qt calls itself that QTlsPrivate::DtlsCryptograph is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'peerVerificationErrors': (
          'QList<QSslError> '
          'QTlsPrivate::DtlsCryptograph::peerVerificationErrors() const',
      ),
      'ignoreVerificationErrors': (
          'void '
          'QTlsPrivate::DtlsCryptograph::ignoreVerificationErrors(const '
          'QList<QSslError> &)',
      ),
  }

  #  The functions Qt calls itself that QTlsPrivate::DtlsCryptograph is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'cryptographMode': (
          ('_ZNK11QTlsPrivate15DtlsCryptograph15cryptographModeEv',
           ('int', 'enum', 'QtNetwork:QSslSocket.SslMode'),
           ()),
      ),
      'setPeer': (
          ('_ZN11QTlsPrivate15DtlsCryptograph7setPeerERK12QHostAddresstRK7Q'
           'String',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtNetwork:QHostAddress'),
               ('unsigned short', 'number', ''),
               ('address', 'text', ''),
           )),
      ),
      'peerAddress': (
          ('_ZNK11QTlsPrivate15DtlsCryptograph11peerAddressEv',
           ('address', 'value', 'QtNetwork:QHostAddress'),
           ()),
      ),
      'peerPort': (
          ('_ZNK11QTlsPrivate15DtlsCryptograph8peerPortEv',
           ('unsigned short', 'number', ''),
           ()),
      ),
      'setPeerVerificationName': (
          ('_ZN11QTlsPrivate15DtlsCryptograph23setPeerVerificationNameERK7Q'
           'String',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'peerVerificationName': (
          ('_ZNK11QTlsPrivate15DtlsCryptograph20peerVerificationNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'setDtlsMtuHint': (
          ('_ZN11QTlsPrivate15DtlsCryptograph14setDtlsMtuHintEt',
           ('nothing', 'nothing', ''),
           (
               ('unsigned short', 'number', ''),
           )),
      ),
      'dtlsMtuHint': (
          ('_ZNK11QTlsPrivate15DtlsCryptograph11dtlsMtuHintEv',
           ('unsigned short', 'number', ''),
           ()),
      ),
      'state': (
          ('_ZNK11QTlsPrivate15DtlsCryptograph5stateEv',
           ('int', 'enum', 'QtNetwork:QDtls.HandshakeState'),
           ()),
      ),
      'isConnectionEncrypted': (
          ('_ZNK11QTlsPrivate15DtlsCryptograph21isConnectionEncryptedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'startHandshake': (
          ('_ZN11QTlsPrivate15DtlsCryptograph14startHandshakeEP10QUdpSocket'
           'RK10QByteArray',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtNetwork:QUdpSocket'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'handleTimeout': (
          ('_ZN11QTlsPrivate15DtlsCryptograph13handleTimeoutEP10QUdpSocket',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtNetwork:QUdpSocket'),
           )),
      ),
      'continueHandshake': (
          ('_ZN11QTlsPrivate15DtlsCryptograph17continueHandshakeEP10QUdpSoc'
           'ketRK10QByteArray',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtNetwork:QUdpSocket'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'resumeHandshake': (
          ('_ZN11QTlsPrivate15DtlsCryptograph15resumeHandshakeEP10QUdpSocke'
           't',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtNetwork:QUdpSocket'),
           )),
      ),
      'abortHandshake': (
          ('_ZN11QTlsPrivate15DtlsCryptograph14abortHandshakeEP10QUdpSocket',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtNetwork:QUdpSocket'),
           )),
      ),
      'sendShutdownAlert': (
          ('_ZN11QTlsPrivate15DtlsCryptograph17sendShutdownAlertEP10QUdpSoc'
           'ket',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtNetwork:QUdpSocket'),
           )),
      ),
      'dtlsSessionCipher': (
          ('_ZNK11QTlsPrivate15DtlsCryptograph17dtlsSessionCipherEv',
           ('address', 'value', 'QtNetwork:QSslCipher'),
           ()),
      ),
      'dtlsSessionProtocol': (
          ('_ZNK11QTlsPrivate15DtlsCryptograph19dtlsSessionProtocolEv',
           ('int', 'enum', 'QtNetwork:QSsl.SslProtocol'),
           ()),
      ),
      'writeDatagramEncrypted': (
          ('_ZN11QTlsPrivate15DtlsCryptograph22writeDatagramEncryptedEP10QU'
           'dpSocketRK10QByteArray',
           ('long long', 'number', ''),
           (
               ('address', 'address', 'QtNetwork:QUdpSocket'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'decryptDatagram': (
          ('_ZN11QTlsPrivate15DtlsCryptograph15decryptDatagramEP10QUdpSocke'
           'tRK10QByteArray',
           ('address', 'value', 'QtCore:QByteArray'),
           (
               ('address', 'address', 'QtNetwork:QUdpSocket'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def cryptographMode(self) -> QSslSocket.SslMode:
    """
    Calls Qt's 'QSslSocket::SslMode
    QTlsPrivate::DtlsCryptograph::cryptographMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#cryptographMode

    Returns
    -------

    QSslSocket.SslMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSslSocket.SslMode(number)' gives.
    """
    #  QSslSocket::SslMode QTlsPrivate::DtlsCryptograph::cryptographMode()
    #      const
    return QSslSocket.SslMode(self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15DtlsCryptograph15cryptographModeEv',
    ))

  def peerAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QTlsPrivate::DtlsCryptograph::peerAddress()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#peerAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QTlsPrivate::DtlsCryptograph::peerAddress() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15DtlsCryptograph11peerAddressEv',
    )
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def peerPort(self) -> int:
    """
    Calls Qt's 'quint16 QTlsPrivate::DtlsCryptograph::peerPort() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#peerPort
    """
    #  quint16 QTlsPrivate::DtlsCryptograph::peerPort() const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15DtlsCryptograph8peerPortEv',
    )

  def peerVerificationName(self) -> str:
    """
    Calls Qt's 'QString QTlsPrivate::DtlsCryptograph::peerVerificationName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTlsPrivate::DtlsCryptograph::peerVerificationName() const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15DtlsCryptograph20peerVerificationNameEv',
    )

  def dtlsMtuHint(self) -> int:
    """
    Calls Qt's 'quint16 QTlsPrivate::DtlsCryptograph::dtlsMtuHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#dtlsMtuHint
    """
    #  quint16 QTlsPrivate::DtlsCryptograph::dtlsMtuHint() const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15DtlsCryptograph11dtlsMtuHintEv',
    )

  def state(self) -> QDtls.HandshakeState:
    """
    Calls Qt's 'QDtls::HandshakeState QTlsPrivate::DtlsCryptograph::state()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#state

    Returns
    -------

    QDtls.HandshakeState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDtls.HandshakeState(number)' gives.
    """
    #  QDtls::HandshakeState QTlsPrivate::DtlsCryptograph::state() const
    return QDtls.HandshakeState(self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15DtlsCryptograph5stateEv',
    ))

  def isConnectionEncrypted(self) -> bool:
    """
    Calls Qt's 'bool QTlsPrivate::DtlsCryptograph::isConnectionEncrypted()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html
    """
    #  bool QTlsPrivate::DtlsCryptograph::isConnectionEncrypted() const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15DtlsCryptograph21isConnectionEncryptedEv',
    )

  def peerVerificationErrors(self) -> QList[QSslError]:
    """
    Calls Qt's 'QList<QSslError>
    QTlsPrivate::DtlsCryptograph::peerVerificationErrors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html

    Returns
    -------

    QList[QSslError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSslError>
    #      QTlsPrivate::DtlsCryptograph::peerVerificationErrors() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15DtlsCryptograph22peerVerificationErrorsEv',
    )
    from . import QSslError
    return QList[QSslError]._cuteOwning(address)

  def dtlsSessionCipher(self) -> QSslCipher:
    """
    Calls Qt's 'QSslCipher QTlsPrivate::DtlsCryptograph::dtlsSessionCipher()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#dtlsSessionCipher

    Returns
    -------

    QSslCipher
      A new cute QSslCipher around the copy Qt gave back. Python owns it.
    """
    #  QSslCipher QTlsPrivate::DtlsCryptograph::dtlsSessionCipher() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15DtlsCryptograph17dtlsSessionCipherEv',
    )
    from . import QSslCipher
    return QSslCipher._cuteOwning(address)

  def dtlsSessionProtocol(self) -> QSsl.SslProtocol:
    """
    Calls Qt's 'QSsl::SslProtocol
    QTlsPrivate::DtlsCryptograph::dtlsSessionProtocol() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html

    Returns
    -------

    QSsl.SslProtocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSsl.SslProtocol(number)'
      gives.
    """
    #  QSsl::SslProtocol QTlsPrivate::DtlsCryptograph::dtlsSessionProtocol()
    #      const
    return QSsl.SslProtocol(self.uglySide.call(
        'ritual_ZNK11QTlsPrivate15DtlsCryptograph19dtlsSessionProtocolEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHostAddress, int, str)
  def setPeer(self, addr: QHostAddress, port: int, name: str) -> None:
    """
    Calls Qt's 'void QTlsPrivate::DtlsCryptograph::setPeer(const QHostAddress
    &addr, quint16 port, const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#setPeer

    Parameters
    ----------

    addr : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTlsPrivate::DtlsCryptograph::setPeer(const QHostAddress &addr,
    #      quint16 port, const QString &name)
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate15DtlsCryptograph7setPeerERK12QHostAddresstR'
        'K7QString',
        self._valueOf(addr), port, name,
    )

  @overload(str)
  def setPeerVerificationName(self, name: str) -> None:
    """
    Calls Qt's 'void
    QTlsPrivate::DtlsCryptograph::setPeerVerificationName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTlsPrivate::DtlsCryptograph::setPeerVerificationName(const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate15DtlsCryptograph23setPeerVerificationNameER'
        'K7QString',
        name,
    )

  @overload(int)
  def setDtlsMtuHint(self, mtu: int) -> None:
    """
    Calls Qt's 'void QTlsPrivate::DtlsCryptograph::setDtlsMtuHint(quint16
    mtu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#setDtlsMtuHint

    Parameters
    ----------

    mtu : int
      Passed on as it is.
    """
    #  void QTlsPrivate::DtlsCryptograph::setDtlsMtuHint(quint16 mtu)
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate15DtlsCryptograph14setDtlsMtuHintEt', mtu,
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

  @overload(QUdpSocket, QByteArray)
  @overload(NoneType, QByteArray)
  def startHandshake(
      self,
      socket: Optional[QUdpSocket],
      dgram: QByteArray,
  ) -> bool:
    """
    Calls Qt's 'bool QTlsPrivate::DtlsCryptograph::startHandshake(QUdpSocket
    *socket, const QByteArray &dgram)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#startHandshake

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dgram : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QTlsPrivate::DtlsCryptograph::startHandshake(QUdpSocket *socket,
    #      const QByteArray &dgram)
    return self.uglySide.call(
        'ritual_ZN11QTlsPrivate15DtlsCryptograph14startHandshakeEP10QUdpSoc'
        'ketRK10QByteArray',
        self._addressOf(socket), self._valueOf(dgram),
    )

  @overload(QUdpSocket)
  @overload(NoneType)
  def handleTimeout(self, socket: Optional[QUdpSocket]) -> bool:
    """
    Calls Qt's 'bool QTlsPrivate::DtlsCryptograph::handleTimeout(QUdpSocket
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#handleTimeout

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTlsPrivate::DtlsCryptograph::handleTimeout(QUdpSocket *socket)
    return self.uglySide.call(
        'ritual_ZN11QTlsPrivate15DtlsCryptograph13handleTimeoutEP10QUdpSock'
        'et',
        self._addressOf(socket),
    )

  @overload(QUdpSocket, QByteArray)
  @overload(NoneType, QByteArray)
  def continueHandshake(
      self,
      socket: Optional[QUdpSocket],
      dgram: QByteArray,
  ) -> bool:
    """
    Calls Qt's 'bool
    QTlsPrivate::DtlsCryptograph::continueHandshake(QUdpSocket *socket, const
    QByteArray &dgram)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#continueHandshake

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dgram : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QTlsPrivate::DtlsCryptograph::continueHandshake(QUdpSocket
    #      *socket, const QByteArray &dgram)
    return self.uglySide.call(
        'ritual_ZN11QTlsPrivate15DtlsCryptograph17continueHandshakeEP10QUdp'
        'SocketRK10QByteArray',
        self._addressOf(socket), self._valueOf(dgram),
    )

  @overload(QUdpSocket)
  @overload(NoneType)
  def resumeHandshake(self, socket: Optional[QUdpSocket]) -> bool:
    """
    Calls Qt's 'bool QTlsPrivate::DtlsCryptograph::resumeHandshake(QUdpSocket
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#resumeHandshake

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTlsPrivate::DtlsCryptograph::resumeHandshake(QUdpSocket *socket)
    return self.uglySide.call(
        'ritual_ZN11QTlsPrivate15DtlsCryptograph15resumeHandshakeEP10QUdpSo'
        'cket',
        self._addressOf(socket),
    )

  @overload(QUdpSocket)
  @overload(NoneType)
  def abortHandshake(self, socket: Optional[QUdpSocket]) -> None:
    """
    Calls Qt's 'void QTlsPrivate::DtlsCryptograph::abortHandshake(QUdpSocket
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#abortHandshake

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTlsPrivate::DtlsCryptograph::abortHandshake(QUdpSocket *socket)
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate15DtlsCryptograph14abortHandshakeEP10QUdpSoc'
        'ket',
        self._addressOf(socket),
    )

  @overload(QUdpSocket)
  @overload(NoneType)
  def sendShutdownAlert(self, socket: Optional[QUdpSocket]) -> None:
    """
    Calls Qt's 'void
    QTlsPrivate::DtlsCryptograph::sendShutdownAlert(QUdpSocket *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#sendShutdownAlert

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTlsPrivate::DtlsCryptograph::sendShutdownAlert(QUdpSocket
    #      *socket)
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate15DtlsCryptograph17sendShutdownAlertEP10QUdp'
        'Socket',
        self._addressOf(socket),
    )

  @overload(QList[QSslError])
  def ignoreVerificationErrors(
      self,
      errorsToIgnore: QList[QSslError],
  ) -> None:
    """
    Calls Qt's 'void
    QTlsPrivate::DtlsCryptograph::ignoreVerificationErrors(const
    QList<QSslError> &errorsToIgnore)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html

    Parameters
    ----------

    errorsToIgnore : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTlsPrivate::DtlsCryptograph::ignoreVerificationErrors(const
    #      QList<QSslError> &errorsToIgnore)
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate15DtlsCryptograph24ignoreVerificationErrorsE'
        'RK5QListI9QSslErrorE',
        self._valueOf(errorsToIgnore),
    )

  @overload(QUdpSocket, QByteArray)
  @overload(NoneType, QByteArray)
  def writeDatagramEncrypted(
      self,
      socket: Optional[QUdpSocket],
      dgram: QByteArray,
  ) -> int:
    """
    Calls Qt's 'qint64
    QTlsPrivate::DtlsCryptograph::writeDatagramEncrypted(QUdpSocket *socket,
    const QByteArray &dgram)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dgram : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  qint64 QTlsPrivate::DtlsCryptograph::writeDatagramEncrypted(QUdpSocket
    #      *socket, const QByteArray &dgram)
    return self.uglySide.call(
        'ritual_ZN11QTlsPrivate15DtlsCryptograph22writeDatagramEncryptedEP1'
        '0QUdpSocketRK10QByteArray',
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
    Calls Qt's 'QByteArray
    QTlsPrivate::DtlsCryptograph::decryptDatagram(QUdpSocket *socket, const
    QByteArray &dgram)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscryptograph.html#decryptDatagram

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
    #  QByteArray QTlsPrivate::DtlsCryptograph::decryptDatagram(QUdpSocket
    #      *socket, const QByteArray &dgram)
    address = self.uglySide.call(
        'ritual_ZN11QTlsPrivate15DtlsCryptograph15decryptDatagramEP10QUdpSo'
        'cketRK10QByteArray',
        self._addressOf(socket), self._valueOf(dgram),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)
