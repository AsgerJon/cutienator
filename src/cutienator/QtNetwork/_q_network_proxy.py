"""
QNetworkProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkproxy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QNetworkRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QVariant
  from . import QHttpHeaders
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHttpHeaders = WAIT['QHttpHeaders']
  QVariant = WAIT['QVariant']


class QNetworkProxy(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkProxy: a plain Python object standing in
  front of one C++ QNetworkProxy.

  C++ hands a QNetworkProxy around as a copy, so every C++ QNetworkProxy
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNetworkProxy that has a ritual and that Python can
  call so far, 26 names in all: '__eq__', '__ne__', 'setType', 'type',
  'setCapabilities', 'capabilities', 'isCachingProxy', 'isTransparentProxy',
  'setUser', 'user', 'setPassword', 'password', 'setHostName', 'hostName',
  'setPort', 'port', 'setApplicationProxy', 'applicationProxy', 'headers',
  'setHeaders', 'header', 'setHeader', 'hasRawHeader', 'rawHeaderList',
  'rawHeader', 'setRawHeader'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkProxy &QNetworkProxy::operator=(QNetworkProxy &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QNetworkProxy &QNetworkProxy::operator=(const QNetworkProxy
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QNetworkProxy::~QNetworkProxy()': the destructor: Python removes
    its C++ QNetworkProxy by it, and has no other use for it.
  - Qt's 'void QNetworkProxy::swap(QNetworkProxy &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QNetworkProxy::setHeaders(QHttpHeaders &&newHeaders)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 37 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QNetworkProxy is created at the first use, not by
    'QNetworkProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkProxy back gives a copy the ritual made for
    Python, in a new cute QNetworkProxy.
  - Each name of Qt's QNetworkProxy that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QNetworkProxy, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Capability(CuteFlags):
    """
    The flags enum 'QNetworkProxy::Capability' of Qt, with the 7 names Qt
    gives in it. Qt names the type of its combinations
    'QNetworkProxy::Capabilities'.
    """

    TunnelingCapability = 0x1
    ListeningCapability = 0x2
    UdpTunnelingCapability = 0x4
    CachingCapability = 0x8
    HostNameLookupCapability = 0x10
    SctpTunnelingCapability = 0x20
    SctpListeningCapability = 0x40

  Capabilities = Capability

  class ProxyType(CuteNum):
    """
    The enum 'QNetworkProxy::ProxyType' of Qt, with the 6 names Qt gives in
    it.
    """

    DefaultProxy = Kee[int](0)
    Socks5Proxy = Kee[int](1)
    NoProxy = Kee[int](2)
    HttpProxy = Kee[int](3)
    HttpCachingProxy = Kee[int](4)
    FtpCachingProxy = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS)
  def setApplicationProxy(proxy: QNetworkProxy) -> None:
    """
    Calls Qt's 'void QNetworkProxy::setApplicationProxy(const QNetworkProxy
    &proxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxy.html#setApplicationProxy

    Parameters
    ----------

    proxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  void QNetworkProxy::setApplicationProxy(const QNetworkProxy &proxy)
    Rituals.call(
        'ritual_ZN13QNetworkProxy19setApplicationProxyERKS_',
        CuteMixin._valueOf(proxy),
    )

  @staticmethod
  def applicationProxy() -> QNetworkProxy:
    """
    Calls Qt's 'QNetworkProxy QNetworkProxy::applicationProxy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxy.html#applicationProxy

    Returns
    -------

    QNetworkProxy
      A new cute QNetworkProxy around the copy Qt gave back. Python owns it.
    """
    #  QNetworkProxy QNetworkProxy::applicationProxy()
    address = Rituals.call('ritual_ZN13QNetworkProxy16applicationProxyEv')
    return QNetworkProxy._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkProxy'

  #  Qt's '~QNetworkProxy()'. Naming it makes this a value class: Python owns
  #  every C++ QNetworkProxy behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QNetworkProxyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> ProxyType:
    """
    Calls Qt's 'QNetworkProxy::ProxyType QNetworkProxy::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#type

    Returns
    -------

    ProxyType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ProxyType(number)' gives.
    """
    #  QNetworkProxy::ProxyType QNetworkProxy::type() const
    return QNetworkProxy.ProxyType(self.uglySide.call(
        'ritual_ZNK13QNetworkProxy4typeEv',
    ))

  def capabilities(self) -> Capabilities:
    """
    Calls Qt's 'Capabilities QNetworkProxy::capabilities() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#capabilities

    Returns
    -------

    Capabilities
      The value standing for the combination Qt gave back.
    """
    #  Capabilities QNetworkProxy::capabilities() const
    return QNetworkProxy.Capabilities(self.uglySide.call(
        'ritual_ZNK13QNetworkProxy12capabilitiesEv',
    ))

  def isCachingProxy(self) -> bool:
    """
    Calls Qt's 'bool QNetworkProxy::isCachingProxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#isCachingProxy
    """
    #  bool QNetworkProxy::isCachingProxy() const
    return self.uglySide.call('ritual_ZNK13QNetworkProxy14isCachingProxyEv')

  def isTransparentProxy(self) -> bool:
    """
    Calls Qt's 'bool QNetworkProxy::isTransparentProxy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxy.html#isTransparentProxy
    """
    #  bool QNetworkProxy::isTransparentProxy() const
    return self.uglySide.call(
        'ritual_ZNK13QNetworkProxy18isTransparentProxyEv',
    )

  def user(self) -> str:
    """
    Calls Qt's 'QString QNetworkProxy::user() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#user

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkProxy::user() const
    return self.uglySide.call('ritual_ZNK13QNetworkProxy4userEv')

  def password(self) -> str:
    """
    Calls Qt's 'QString QNetworkProxy::password() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#password

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkProxy::password() const
    return self.uglySide.call('ritual_ZNK13QNetworkProxy8passwordEv')

  def hostName(self) -> str:
    """
    Calls Qt's 'QString QNetworkProxy::hostName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#hostName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkProxy::hostName() const
    return self.uglySide.call('ritual_ZNK13QNetworkProxy8hostNameEv')

  def port(self) -> int:
    """
    Calls Qt's 'quint16 QNetworkProxy::port() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#port
    """
    #  quint16 QNetworkProxy::port() const
    return self.uglySide.call('ritual_ZNK13QNetworkProxy4portEv')

  def headers(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QNetworkProxy::headers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#headers

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QNetworkProxy::headers() const
    address = self.uglySide.call('ritual_ZNK13QNetworkProxy7headersEv')
    from . import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  @overload(QNetworkRequest.KnownHeaders)
  def header(self, header: QNetworkRequest.KnownHeaders) -> QVariant:
    """
    Calls Qt's 'QVariant QNetworkProxy::header(QNetworkRequest::KnownHeaders
    header) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#header

    Parameters
    ----------

    header : QNetworkRequest.KnownHeaders
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QNetworkProxy::header(QNetworkRequest::KnownHeaders header)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QNetworkProxy6headerEN15QNetworkRequest12KnownHeadersE',
        header.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QByteArray)
  def hasRawHeader(self, headerName: QByteArray) -> bool:
    """
    Calls Qt's 'bool QNetworkProxy::hasRawHeader(const QByteArray
    &headerName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#hasRawHeader

    Parameters
    ----------

    headerName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QNetworkProxy::hasRawHeader(const QByteArray &headerName) const
    return self.uglySide.call(
        'ritual_ZNK13QNetworkProxy12hasRawHeaderERK10QByteArray',
        self._valueOf(headerName),
    )

  def rawHeaderList(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QNetworkProxy::rawHeaderList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#rawHeaderList

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QNetworkProxy::rawHeaderList() const
    address = self.uglySide.call(
        'ritual_ZNK13QNetworkProxy13rawHeaderListEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(QByteArray)
  def rawHeader(self, headerName: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNetworkProxy::rawHeader(const QByteArray
    &headerName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#rawHeader

    Parameters
    ----------

    headerName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNetworkProxy::rawHeader(const QByteArray &headerName)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QNetworkProxy9rawHeaderERK10QByteArray',
        self._valueOf(headerName),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ProxyType)
  def setType(self, type: ProxyType) -> None:
    """
    Calls Qt's 'void QNetworkProxy::setType(QNetworkProxy::ProxyType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#setType

    Parameters
    ----------

    type : ProxyType
      Passed on as its number.
    """
    #  void QNetworkProxy::setType(QNetworkProxy::ProxyType type)
    self.uglySide.call(
        'ritual_ZN13QNetworkProxy7setTypeENS_9ProxyTypeE', type.value,
    )

  @overload(Capabilities)
  def setCapabilities(self, capab: Capabilities) -> None:
    """
    Calls Qt's 'void QNetworkProxy::setCapabilities(Capabilities capab)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#setCapabilities

    Parameters
    ----------

    capab : Capabilities
      Passed on as its number.
    """
    #  void QNetworkProxy::setCapabilities(Capabilities capab)
    self.uglySide.call(
        'ritual_ZN13QNetworkProxy15setCapabilitiesE6QFlagsINS_10CapabilityE'
        'E',
        capab.value,
    )

  @overload(str)
  def setUser(self, userName: str) -> None:
    """
    Calls Qt's 'void QNetworkProxy::setUser(const QString &userName)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#setUser

    Parameters
    ----------

    userName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkProxy::setUser(const QString &userName)
    self.uglySide.call(
        'ritual_ZN13QNetworkProxy7setUserERK7QString', userName,
    )

  @overload(str)
  def setPassword(self, password: str) -> None:
    """
    Calls Qt's 'void QNetworkProxy::setPassword(const QString &password)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#setPassword

    Parameters
    ----------

    password : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkProxy::setPassword(const QString &password)
    self.uglySide.call(
        'ritual_ZN13QNetworkProxy11setPasswordERK7QString', password,
    )

  @overload(str)
  def setHostName(self, hostName: str) -> None:
    """
    Calls Qt's 'void QNetworkProxy::setHostName(const QString &hostName)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#setHostName

    Parameters
    ----------

    hostName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkProxy::setHostName(const QString &hostName)
    self.uglySide.call(
        'ritual_ZN13QNetworkProxy11setHostNameERK7QString', hostName,
    )

  @overload(int)
  def setPort(self, port: int) -> None:
    """
    Calls Qt's 'void QNetworkProxy::setPort(quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#setPort

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QNetworkProxy::setPort(quint16 port)
    self.uglySide.call('ritual_ZN13QNetworkProxy7setPortEt', port)

  @overload(QHttpHeaders)
  def setHeaders(self, newHeaders: QHttpHeaders) -> None:
    """
    Calls Qt's 'void QNetworkProxy::setHeaders(const QHttpHeaders
    &newHeaders)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#setHeaders

    Parameters
    ----------

    newHeaders : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.
    """
    #  void QNetworkProxy::setHeaders(const QHttpHeaders &newHeaders)
    self.uglySide.call(
        'ritual_ZN13QNetworkProxy10setHeadersERK12QHttpHeaders',
        self._valueOf(newHeaders),
    )

  @overload(QNetworkRequest.KnownHeaders, QVariant)
  def setHeader(
      self,
      header: QNetworkRequest.KnownHeaders,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QNetworkProxy::setHeader(QNetworkRequest::KnownHeaders
    header, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#setHeader

    Parameters
    ----------

    header : QNetworkRequest.KnownHeaders
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QNetworkProxy::setHeader(QNetworkRequest::KnownHeaders header,
    #      const QVariant &value)
    self.uglySide.call(
        'ritual_ZN13QNetworkProxy9setHeaderEN15QNetworkRequest12KnownHeader'
        'sERK8QVariant',
        header.value, self._valueOf(value),
    )

  @overload(QByteArray, QByteArray)
  def setRawHeader(self, headerName: QByteArray, value: QByteArray) -> None:
    """
    Calls Qt's 'void QNetworkProxy::setRawHeader(const QByteArray
    &headerName, const QByteArray &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#setRawHeader

    Parameters
    ----------

    headerName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNetworkProxy::setRawHeader(const QByteArray &headerName, const
    #      QByteArray &value)
    self.uglySide.call(
        'ritual_ZN13QNetworkProxy12setRawHeaderERK10QByteArrayS2_',
        self._valueOf(headerName), self._valueOf(value),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QNetworkProxy) -> bool:
    """
    Calls Qt's 'bool QNetworkProxy::operator==(const QNetworkProxy &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#operator==

    Parameters
    ----------

    other : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  bool QNetworkProxy::operator==(const QNetworkProxy &other) const
    return self.uglySide.call(
        'ritual_ZNK13QNetworkProxyeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QNetworkProxy) -> bool:
    """
    Calls Qt's 'bool QNetworkProxy::operator!=(const QNetworkProxy &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#operator!=

    Parameters
    ----------

    other : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  bool QNetworkProxy::operator!=(const QNetworkProxy &other) const
    return self.uglySide.call(
        'ritual_ZNK13QNetworkProxyneERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QNetworkProxy::QNetworkProxy()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#QNetworkProxy
    """
    #  QNetworkProxy::QNetworkProxy()
    self._noteCreation(QNetworkProxy, lambda: Rituals.call(
        'ritual_ZN13QNetworkProxyC1Ev',
    ))

  @overload(ProxyType)
  @overload(ProxyType, str)
  @overload(ProxyType, str, int)
  @overload(ProxyType, str, int, str)
  @overload(ProxyType, str, int, str, str)
  def __init__(
      self,
      type: ProxyType,
      hostName: str = '',
      port: int = 0,
      user: str = '',
      password: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's 'QNetworkProxy::QNetworkProxy(ProxyType
    type, const QString &hostName, quint16 port, const QString &user, const
    QString &password)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#QNetworkProxy

    Parameters
    ----------

    type : ProxyType
      Passed on as its number.

    hostName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    user : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    password : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QNetworkProxy::QNetworkProxy(ProxyType type, const QString &hostName,
    #      quint16 port, const QString &user, const QString &password)
    self._noteCreation(QNetworkProxy, lambda: Rituals.call(
        'ritual_ZN13QNetworkProxyC1ENS_9ProxyTypeERK7QStringtS3_S3_',
        type.value, hostName, port, user, password,
    ))

  @overload(THIS)
  def __init__(self, other: QNetworkProxy) -> None:
    """
    Notes what was given, for Qt's 'QNetworkProxy::QNetworkProxy(const
    QNetworkProxy &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxy.html#QNetworkProxy

    Parameters
    ----------

    other : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  QNetworkProxy::QNetworkProxy(const QNetworkProxy &other)
    self._noteCreation(QNetworkProxy, lambda: Rituals.call(
        'ritual_ZN13QNetworkProxyC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QNetworkProxy::swap(QNetworkProxy &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkProxy.swap' has no cute function yet. Qt's 'void "
        "QNetworkProxy::swap(QNetworkProxy &other)': takes a type Python "
        "has no way to hand over yet.")


#  Qt's 'QList<QNetworkProxy>': the list of QNetworkProxy, which
#  'QList[QNetworkProxy]' gives. It is made here, so that there is one as
#  soon as there can be a QNetworkProxy.
QList.createKind(
    QNetworkProxy, 'value',
    make='ritual_list_make_QNetworkProxy',
    add='ritual_list_add_QNetworkProxy',
    size='ritual_list_size_QNetworkProxy',
    at='ritual_list_at_QNetworkProxy',
    drop='ritual_list_drop_QNetworkProxy',
)
