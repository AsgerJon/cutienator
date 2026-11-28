"""
QDnsLookup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qdnslookup.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QDnsDomainNameRecord, QDnsHostAddressRecord
  from . import QDnsLookupPrivate, QDnsMailExchangeRecord, QDnsServiceRecord
  from . import QDnsTextRecord, QDnsTlsAssociationRecord, QHostAddress
  from . import QSslConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']
  QSslConfiguration = WAIT['QSslConfiguration']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDnsLookup(QObject):
  """
  The cute side of Qt's QDnsLookup: a plain Python object standing in front
  of one C++ QDnsLookup.

  It is built on the cute 'QObject', as Qt's QDnsLookup is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDnsLookup that has a ritual and that Python can
  call so far, 37 names in all: 'metaObject', 'tr', 'isAuthenticData',
  'error', 'errorString', 'isFinished', 'name', 'setName', 'type', 'setType',
  'nameserver', 'setNameserver', 'nameserverPort', 'setNameserverPort',
  'nameserverProtocol', 'setNameserverProtocol', 'canonicalNameRecords',
  'hostAddressRecords', 'mailExchangeRecords', 'nameServerRecords',
  'pointerRecords', 'serviceRecords', 'textRecords', 'tlsAssociationRecords',
  'setSslConfiguration', 'sslConfiguration', 'isProtocolSupported',
  'defaultPortForProtocol', 'abort', 'lookup', 'finished', 'nameChanged',
  'typeChanged', 'nameserverChanged', 'nameserverPortChanged',
  'nameserverProtocolChanged', 'd_func'. It can be made from Python, in 5
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDnsLookup::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QDnsLookup::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QDnsLookup::~QDnsLookup()': the destructor: Python never removes a
    C++ QDnsLookup.
  - Qt's 'QBindable<QString> QDnsLookup::bindableName()': gives a type Python
    has no way to take yet.
  - Qt's 'QBindable<Type> QDnsLookup::bindableType()': gives a type Python
    has no way to take yet.
  - Qt's 'QBindable<QHostAddress> QDnsLookup::bindableNameserver()': gives a
    type Python has no way to take yet.
  - Qt's 'QBindable<quint16> QDnsLookup::bindableNameserverPort()': gives a
    type Python has no way to take yet.
  - Qt's 'QBindable<Protocol> QDnsLookup::bindableNameserverProtocol()':
    gives a type Python has no way to take yet.
  - Qt's 'const QDnsLookupPrivate *QDnsLookup::d_func() const': takes in
    Python what 'QDnsLookupPrivate *QDnsLookup::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 55 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDnsLookup is created at the first use, not by 'QDnsLookup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDnsLookup.
  - Qt tells when it has removed the C++ QDnsLookup. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QDnsLookup that has no cute function yet,
    'bindableName', 'bindableNameserver', 'bindableNameserverPort',
    'bindableNameserverProtocol', 'bindableType', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDnsLookup, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QDnsLookup::Error' of Qt, with the 9 names Qt gives in it.
    """

    NoError = Kee[int](0)
    ResolverError = Kee[int](1)
    OperationCancelledError = Kee[int](2)
    InvalidRequestError = Kee[int](3)
    InvalidReplyError = Kee[int](4)
    ServerFailureError = Kee[int](5)
    ServerRefusedError = Kee[int](6)
    NotFoundError = Kee[int](7)
    TimeoutError = Kee[int](8)

  class Protocol(CuteNum):
    """
    The enum 'QDnsLookup::Protocol' of Qt, with the 2 names Qt gives in it.
    """

    Standard = Kee[int](0)
    DnsOverTls = Kee[int](1)

  class Type(CuteNum):
    """
    The enum 'QDnsLookup::Type' of Qt, with the 10 names Qt gives in it.
    """

    A = Kee[int](1)
    AAAA = Kee[int](28)
    ANY = Kee[int](255)
    CNAME = Kee[int](5)
    MX = Kee[int](15)
    NS = Kee[int](2)
    PTR = Kee[int](12)
    SRV = Kee[int](33)
    TLSA = Kee[int](52)
    TXT = Kee[int](16)

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
    Calls Qt's 'QString QDnsLookup::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#tr

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
    #  QString QDnsLookup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QDnsLookup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(Protocol)
  def isProtocolSupported(protocol: Protocol) -> bool:
    """
    Calls Qt's 'bool QDnsLookup::isProtocolSupported(Protocol protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookup.html#isProtocolSupported

    Parameters
    ----------

    protocol : Protocol
      Passed on as its number.
    """
    #  bool QDnsLookup::isProtocolSupported(Protocol protocol)
    return Rituals.call(
        'ritual_ZN10QDnsLookup19isProtocolSupportedENS_8ProtocolE',
        protocol.value,
    )

  @staticmethod
  @overload(Protocol)
  def defaultPortForProtocol(protocol: Protocol) -> int:
    """
    Calls Qt's 'quint16 QDnsLookup::defaultPortForProtocol(Protocol
    protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookup.html#defaultPortForProtocol

    Parameters
    ----------

    protocol : Protocol
      Passed on as its number.
    """
    #  quint16 QDnsLookup::defaultPortForProtocol(Protocol protocol)
    return Rituals.call(
        'ritual_ZN10QDnsLookup22defaultPortForProtocolENS_8ProtocolE',
        protocol.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDnsLookup'

  #  A C++ QDnsLookup Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDnsLookup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDnsLookup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDnsLookup::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QDnsLookup10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isAuthenticData(self) -> bool:
    """
    Calls Qt's 'bool QDnsLookup::isAuthenticData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#isAuthenticData
    """
    #  bool QDnsLookup::isAuthenticData() const
    return self.uglySide.call('ritual_ZNK10QDnsLookup15isAuthenticDataEv')

  def error(self) -> Error:
    """
    Calls Qt's 'Error QDnsLookup::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QDnsLookup::error() const
    return QDnsLookup.Error(self.uglySide.call(
        'ritual_ZNK10QDnsLookup5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QDnsLookup::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDnsLookup::errorString() const
    return self.uglySide.call('ritual_ZNK10QDnsLookup11errorStringEv')

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QDnsLookup::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#isFinished
    """
    #  bool QDnsLookup::isFinished() const
    return self.uglySide.call('ritual_ZNK10QDnsLookup10isFinishedEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QDnsLookup::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDnsLookup::name() const
    return self.uglySide.call('ritual_ZNK10QDnsLookup4nameEv')

  def type(self) -> Type:
    """
    Calls Qt's 'Type QDnsLookup::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QDnsLookup::type() const
    return QDnsLookup.Type(self.uglySide.call(
        'ritual_ZNK10QDnsLookup4typeEv',
    ))

  def nameserver(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QDnsLookup::nameserver() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#nameserver

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QDnsLookup::nameserver() const
    address = self.uglySide.call('ritual_ZNK10QDnsLookup10nameserverEv')
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def nameserverPort(self) -> int:
    """
    Calls Qt's 'quint16 QDnsLookup::nameserverPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#nameserverPort
    """
    #  quint16 QDnsLookup::nameserverPort() const
    return self.uglySide.call('ritual_ZNK10QDnsLookup14nameserverPortEv')

  def nameserverProtocol(self) -> Protocol:
    """
    Calls Qt's 'Protocol QDnsLookup::nameserverProtocol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#nameserverProtocol

    Returns
    -------

    Protocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Protocol(number)' gives.
    """
    #  Protocol QDnsLookup::nameserverProtocol() const
    return QDnsLookup.Protocol(self.uglySide.call(
        'ritual_ZNK10QDnsLookup18nameserverProtocolEv',
    ))

  def canonicalNameRecords(self) -> QList[QDnsDomainNameRecord]:
    """
    Calls Qt's 'QList<QDnsDomainNameRecord>
    QDnsLookup::canonicalNameRecords() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookup.html#canonicalNameRecords

    Returns
    -------

    QList[QDnsDomainNameRecord]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDnsDomainNameRecord> QDnsLookup::canonicalNameRecords() const
    address = self.uglySide.call(
        'ritual_ZNK10QDnsLookup20canonicalNameRecordsEv',
    )
    from . import QDnsDomainNameRecord
    return QList[QDnsDomainNameRecord]._cuteOwning(address)

  def hostAddressRecords(self) -> QList[QDnsHostAddressRecord]:
    """
    Calls Qt's 'QList<QDnsHostAddressRecord> QDnsLookup::hostAddressRecords()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#hostAddressRecords

    Returns
    -------

    QList[QDnsHostAddressRecord]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDnsHostAddressRecord> QDnsLookup::hostAddressRecords() const
    address = self.uglySide.call(
        'ritual_ZNK10QDnsLookup18hostAddressRecordsEv',
    )
    from . import QDnsHostAddressRecord
    return QList[QDnsHostAddressRecord]._cuteOwning(address)

  def mailExchangeRecords(self) -> QList[QDnsMailExchangeRecord]:
    """
    Calls Qt's 'QList<QDnsMailExchangeRecord>
    QDnsLookup::mailExchangeRecords() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookup.html#mailExchangeRecords

    Returns
    -------

    QList[QDnsMailExchangeRecord]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDnsMailExchangeRecord> QDnsLookup::mailExchangeRecords() const
    address = self.uglySide.call(
        'ritual_ZNK10QDnsLookup19mailExchangeRecordsEv',
    )
    from . import QDnsMailExchangeRecord
    return QList[QDnsMailExchangeRecord]._cuteOwning(address)

  def nameServerRecords(self) -> QList[QDnsDomainNameRecord]:
    """
    Calls Qt's 'QList<QDnsDomainNameRecord> QDnsLookup::nameServerRecords()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#nameServerRecords

    Returns
    -------

    QList[QDnsDomainNameRecord]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDnsDomainNameRecord> QDnsLookup::nameServerRecords() const
    address = self.uglySide.call(
        'ritual_ZNK10QDnsLookup17nameServerRecordsEv',
    )
    from . import QDnsDomainNameRecord
    return QList[QDnsDomainNameRecord]._cuteOwning(address)

  def pointerRecords(self) -> QList[QDnsDomainNameRecord]:
    """
    Calls Qt's 'QList<QDnsDomainNameRecord> QDnsLookup::pointerRecords()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#pointerRecords

    Returns
    -------

    QList[QDnsDomainNameRecord]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDnsDomainNameRecord> QDnsLookup::pointerRecords() const
    address = self.uglySide.call('ritual_ZNK10QDnsLookup14pointerRecordsEv')
    from . import QDnsDomainNameRecord
    return QList[QDnsDomainNameRecord]._cuteOwning(address)

  def serviceRecords(self) -> QList[QDnsServiceRecord]:
    """
    Calls Qt's 'QList<QDnsServiceRecord> QDnsLookup::serviceRecords() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#serviceRecords

    Returns
    -------

    QList[QDnsServiceRecord]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDnsServiceRecord> QDnsLookup::serviceRecords() const
    address = self.uglySide.call('ritual_ZNK10QDnsLookup14serviceRecordsEv')
    from . import QDnsServiceRecord
    return QList[QDnsServiceRecord]._cuteOwning(address)

  def textRecords(self) -> QList[QDnsTextRecord]:
    """
    Calls Qt's 'QList<QDnsTextRecord> QDnsLookup::textRecords() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#textRecords

    Returns
    -------

    QList[QDnsTextRecord]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDnsTextRecord> QDnsLookup::textRecords() const
    address = self.uglySide.call('ritual_ZNK10QDnsLookup11textRecordsEv')
    from . import QDnsTextRecord
    return QList[QDnsTextRecord]._cuteOwning(address)

  def tlsAssociationRecords(self) -> QList[QDnsTlsAssociationRecord]:
    """
    Calls Qt's 'QList<QDnsTlsAssociationRecord>
    QDnsLookup::tlsAssociationRecords() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookup.html#tlsAssociationRecords

    Returns
    -------

    QList[QDnsTlsAssociationRecord]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDnsTlsAssociationRecord> QDnsLookup::tlsAssociationRecords()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10QDnsLookup21tlsAssociationRecordsEv',
    )
    from . import QDnsTlsAssociationRecord
    return QList[QDnsTlsAssociationRecord]._cuteOwning(address)

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QDnsLookup::sslConfiguration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QDnsLookup::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK10QDnsLookup16sslConfigurationEv',
    )
    from . import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QDnsLookup::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDnsLookup::setName(const QString &name)
    self.uglySide.call('ritual_ZN10QDnsLookup7setNameERK7QString', name)

  @overload(Type)
  def setType(self, a0: Type) -> None:
    """
    Calls Qt's 'void QDnsLookup::setType(QDnsLookup::Type a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#setType

    Parameters
    ----------

    a0 : Type
      Passed on as its number.
    """
    #  void QDnsLookup::setType(QDnsLookup::Type a0)
    self.uglySide.call('ritual_ZN10QDnsLookup7setTypeENS_4TypeE', a0.value)

  @overload(QHostAddress)
  def setNameserver(self, nameserver: QHostAddress) -> None:
    """
    Calls Qt's 'void QDnsLookup::setNameserver(const QHostAddress
    &nameserver)'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#setNameserver

    Parameters
    ----------

    nameserver : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QDnsLookup::setNameserver(const QHostAddress &nameserver)
    self.uglySide.call(
        'ritual_ZN10QDnsLookup13setNameserverERK12QHostAddress',
        self._valueOf(nameserver),
    )

  @overload(Protocol, QHostAddress)
  @overload(Protocol, QHostAddress, int)
  def setNameserver(
      self,
      protocol: Protocol,
      nameserver: QHostAddress,
      port: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QDnsLookup::setNameserver(Protocol protocol, const
    QHostAddress &nameserver, quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#setNameserver

    Parameters
    ----------

    protocol : Protocol
      Passed on as its number.

    nameserver : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QDnsLookup::setNameserver(Protocol protocol, const QHostAddress
    #      &nameserver, quint16 port)
    self.uglySide.call(
        'ritual_ZN10QDnsLookup13setNameserverENS_8ProtocolERK12QHostAddress'
        't',
        protocol.value, self._valueOf(nameserver), port,
    )

  @overload(QHostAddress, int)
  def setNameserver(self, nameserver: QHostAddress, port: int) -> None:
    """
    Calls Qt's 'void QDnsLookup::setNameserver(const QHostAddress
    &nameserver, quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#setNameserver

    Parameters
    ----------

    nameserver : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  void QDnsLookup::setNameserver(const QHostAddress &nameserver, quint16
    #      port)
    self.uglySide.call(
        'ritual_ZN10QDnsLookup13setNameserverERK12QHostAddresst',
        self._valueOf(nameserver), port,
    )

  @overload(int)
  def setNameserverPort(self, port: int) -> None:
    """
    Calls Qt's 'void QDnsLookup::setNameserverPort(quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#setNameserverPort

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QDnsLookup::setNameserverPort(quint16 port)
    self.uglySide.call('ritual_ZN10QDnsLookup17setNameserverPortEt', port)

  @overload(Protocol)
  def setNameserverProtocol(self, protocol: Protocol) -> None:
    """
    Calls Qt's 'void QDnsLookup::setNameserverProtocol(Protocol protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookup.html#setNameserverProtocol

    Parameters
    ----------

    protocol : Protocol
      Passed on as its number.
    """
    #  void QDnsLookup::setNameserverProtocol(Protocol protocol)
    self.uglySide.call(
        'ritual_ZN10QDnsLookup21setNameserverProtocolENS_8ProtocolE',
        protocol.value,
    )

  @overload(QSslConfiguration)
  def setSslConfiguration(self, sslConfiguration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QDnsLookup::setSslConfiguration(const QSslConfiguration
    &sslConfiguration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookup.html#setSslConfiguration

    Parameters
    ----------

    sslConfiguration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QDnsLookup::setSslConfiguration(const QSslConfiguration
    #      &sslConfiguration)
    self.uglySide.call(
        'ritual_ZN10QDnsLookup19setSslConfigurationERK17QSslConfiguration',
        self._valueOf(sslConfiguration),
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
    Notes what was given, for Qt's 'QDnsLookup::QDnsLookup(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#QDnsLookup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDnsLookup::QDnsLookup(QObject *parent)
    self._noteCreation(QDnsLookup, lambda: Rituals.call(
        'ritual_ZN10QDnsLookupC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(Type, str)
  @overload(Type, str, QObject)
  @overload(Type, str, NoneType)
  def __init__(
      self,
      type: Type,
      name: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDnsLookup::QDnsLookup(Type type, const
    QString &name, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#QDnsLookup

    Parameters
    ----------

    type : Type
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDnsLookup::QDnsLookup(Type type, const QString &name, QObject
    #      *parent)
    self._noteCreation(QDnsLookup, lambda: Rituals.call(
        'ritual_ZN10QDnsLookupC1ENS_4TypeERK7QStringP7QObject',
        type.value, name, self._addressOf(parent, 'QObject'),
    ))

  @overload(Type, str, QHostAddress)
  @overload(Type, str, QHostAddress, QObject)
  @overload(Type, str, QHostAddress, NoneType)
  def __init__(
      self,
      type: Type,
      name: str,
      nameserver: QHostAddress,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDnsLookup::QDnsLookup(Type type, const
    QString &name, const QHostAddress &nameserver, QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#QDnsLookup

    Parameters
    ----------

    type : Type
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.

    nameserver : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDnsLookup::QDnsLookup(Type type, const QString &name, const
    #      QHostAddress &nameserver, QObject *parent)
    self._noteCreation(QDnsLookup, lambda: Rituals.call(
        'ritual_ZN10QDnsLookupC1ENS_4TypeERK7QStringRK12QHostAddressP7QObje'
        'ct',
        type.value, name, self._valueOf(nameserver), self._addressOf(parent,
        'QObject'),
    ))

  @overload(Type, str, QHostAddress, int)
  @overload(Type, str, QHostAddress, int, QObject)
  @overload(Type, str, QHostAddress, int, NoneType)
  def __init__(
      self,
      type: Type,
      name: str,
      nameserver: QHostAddress,
      port: int,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDnsLookup::QDnsLookup(Type type, const
    QString &name, const QHostAddress &nameserver, quint16 port, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#QDnsLookup

    Parameters
    ----------

    type : Type
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.

    nameserver : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDnsLookup::QDnsLookup(Type type, const QString &name, const
    #      QHostAddress &nameserver, quint16 port, QObject *parent)
    self._noteCreation(QDnsLookup, lambda: Rituals.call(
        'ritual_ZN10QDnsLookupC1ENS_4TypeERK7QStringRK12QHostAddresstP7QObj'
        'ect',
        type.value, name, self._valueOf(nameserver), port,
        self._addressOf(parent, 'QObject'),
    ))

  @overload(Type, str, Protocol, QHostAddress)
  @overload(Type, str, Protocol, QHostAddress, int)
  @overload(Type, str, Protocol, QHostAddress, int, QObject)
  @overload(Type, str, Protocol, QHostAddress, int, NoneType)
  def __init__(
      self,
      type: Type,
      name: str,
      protocol: Protocol,
      nameserver: QHostAddress,
      port: int = 0,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDnsLookup::QDnsLookup(Type type, const
    QString &name, Protocol protocol, const QHostAddress &nameserver, quint16
    port, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#QDnsLookup

    Parameters
    ----------

    type : Type
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.

    protocol : Protocol
      Passed on as its number.

    nameserver : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDnsLookup::QDnsLookup(Type type, const QString &name, Protocol
    #      protocol, const QHostAddress &nameserver, quint16 port, QObject
    #      *parent)
    self._noteCreation(QDnsLookup, lambda: Rituals.call(
        'ritual_ZN10QDnsLookupC1ENS_4TypeERK7QStringNS_8ProtocolERK12QHostA'
        'ddresstP7QObject',
        type.value, name, protocol.value, self._valueOf(nameserver), port,
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

  def abort(self) -> None:
    """
    Calls Qt's 'void QDnsLookup::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#abort
    """
    #  void QDnsLookup::abort()
    self.uglySide.call('ritual_ZN10QDnsLookup5abortEv')

  def lookup(self) -> None:
    """
    Calls Qt's 'void QDnsLookup::lookup()'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#lookup
    """
    #  void QDnsLookup::lookup()
    self.uglySide.call('ritual_ZN10QDnsLookup6lookupEv')

  def finished(self) -> None:
    """
    Calls Qt's 'void QDnsLookup::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#finished
    """
    #  void QDnsLookup::finished()
    self.uglySide.call('ritual_ZN10QDnsLookup8finishedEv')

  @overload(str)
  def nameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void QDnsLookup::nameChanged(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#nameChanged

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDnsLookup::nameChanged(const QString &name)
    self.uglySide.call('ritual_ZN10QDnsLookup11nameChangedERK7QString', name)

  @overload(Type)
  def typeChanged(self, type: Type) -> None:
    """
    Calls Qt's 'void QDnsLookup::typeChanged(QDnsLookup::Type type)'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#typeChanged

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  void QDnsLookup::typeChanged(QDnsLookup::Type type)
    self.uglySide.call(
        'ritual_ZN10QDnsLookup11typeChangedENS_4TypeE', type.value,
    )

  @overload(QHostAddress)
  def nameserverChanged(self, nameserver: QHostAddress) -> None:
    """
    Calls Qt's 'void QDnsLookup::nameserverChanged(const QHostAddress
    &nameserver)'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#nameserverChanged

    Parameters
    ----------

    nameserver : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QDnsLookup::nameserverChanged(const QHostAddress &nameserver)
    self.uglySide.call(
        'ritual_ZN10QDnsLookup17nameserverChangedERK12QHostAddress',
        self._valueOf(nameserver),
    )

  @overload(int)
  def nameserverPortChanged(self, port: int) -> None:
    """
    Calls Qt's 'void QDnsLookup::nameserverPortChanged(quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookup.html#nameserverPortChanged

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QDnsLookup::nameserverPortChanged(quint16 port)
    self.uglySide.call(
        'ritual_ZN10QDnsLookup21nameserverPortChangedEt', port,
    )

  @overload(Protocol)
  def nameserverProtocolChanged(self, protocol: Protocol) -> None:
    """
    Calls Qt's 'void
    QDnsLookup::nameserverProtocolChanged(QDnsLookup::Protocol protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookup.html#nameserverProtocolChanged

    Parameters
    ----------

    protocol : Protocol
      Passed on as its number.
    """
    #  void QDnsLookup::nameserverProtocolChanged(QDnsLookup::Protocol
    #      protocol)
    self.uglySide.call(
        'ritual_ZN10QDnsLookup25nameserverProtocolChangedENS_8ProtocolE',
        protocol.value,
    )

  def d_func(self) -> Optional[QDnsLookupPrivate]:
    """
    Calls Qt's 'QDnsLookupPrivate *QDnsLookup::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookup.html#d_func

    Returns
    -------

    Optional[QDnsLookupPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDnsLookupPrivate *QDnsLookup::d_func()
    address = self.uglySide.call('ritual_ZN10QDnsLookup6d_funcEv')
    from . import QDnsLookupPrivate
    return QDnsLookupPrivate._cuteAt(address)

  @staticmethod
  def bindableName(*__, **_) -> Never:
    """
    Qt's 'QBindable<QString> QDnsLookup::bindableName()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QDnsLookup.bindableName' has no cute function yet. Qt's "
        "'QBindable<QString> QDnsLookup::bindableName()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableNameserver(*__, **_) -> Never:
    """
    Qt's 'QBindable<QHostAddress> QDnsLookup::bindableNameserver()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDnsLookup.bindableNameserver' has no cute function yet. Qt's "
        "'QBindable<QHostAddress> QDnsLookup::bindableNameserver()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def bindableNameserverPort(*__, **_) -> Never:
    """
    Qt's 'QBindable<quint16> QDnsLookup::bindableNameserverPort()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDnsLookup.bindableNameserverPort' has no cute function yet. Qt's "
        "'QBindable<quint16> QDnsLookup::bindableNameserverPort()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableNameserverProtocol(*__, **_) -> Never:
    """
    Qt's 'QBindable<Protocol> QDnsLookup::bindableNameserverProtocol()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDnsLookup.bindableNameserverProtocol' has no cute function yet. "
        "Qt's 'QBindable<Protocol> "
        "QDnsLookup::bindableNameserverProtocol()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def bindableType(*__, **_) -> Never:
    """
    Qt's 'QBindable<Type> QDnsLookup::bindableType()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QDnsLookup.bindableType' has no cute function yet. Qt's "
        "'QBindable<Type> QDnsLookup::bindableType()': gives a type Python "
        "has no way to take yet.")
