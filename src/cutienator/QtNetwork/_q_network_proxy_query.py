"""
QNetworkProxyQuery binding of the Qt C++
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

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QNetworkProxyQuery(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkProxyQuery: a plain Python object standing in
  front of one C++ QNetworkProxyQuery.

  C++ hands a QNetworkProxyQuery around as a copy, so every C++
  QNetworkProxyQuery behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNetworkProxyQuery that has a ritual and that Python
  can call so far, 14 names in all: '__eq__', '__ne__', 'queryType',
  'setQueryType', 'peerPort', 'setPeerPort', 'peerHostName',
  'setPeerHostName', 'localPort', 'setLocalPort', 'protocolTag',
  'setProtocolTag', 'url', 'setUrl'. It can be made from Python, in 5 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkProxyQuery
    &QNetworkProxyQuery::operator=(QNetworkProxyQuery &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QNetworkProxyQuery &QNetworkProxyQuery::operator=(const
    QNetworkProxyQuery &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QNetworkProxyQuery::~QNetworkProxyQuery()': the destructor: Python
    removes its C++ QNetworkProxyQuery by it, and has no other use for it.
  - Qt's 'void QNetworkProxyQuery::swap(QNetworkProxyQuery &other)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 26 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QNetworkProxyQuery is created at the first use, not by
    'QNetworkProxyQuery(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkProxyQuery back gives a copy the ritual made
    for Python, in a new cute QNetworkProxyQuery.
  - Each name of Qt's QNetworkProxyQuery that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QNetworkProxyQuery, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class QueryType(CuteNum):
    """
    The enum 'QNetworkProxyQuery::QueryType' of Qt, with the 6 names Qt gives
    in it.
    """

    TcpSocket = Kee[int](0)
    UdpSocket = Kee[int](1)
    SctpSocket = Kee[int](2)
    TcpServer = Kee[int](100)
    UrlRequest = Kee[int](101)
    SctpServer = Kee[int](102)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkProxyQuery'

  #  Qt's '~QNetworkProxyQuery()'. Naming it makes this a value class: Python
  #  owns every C++ QNetworkProxyQuery behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QNetworkProxyQueryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def queryType(self) -> QueryType:
    """
    Calls Qt's 'QueryType QNetworkProxyQuery::queryType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxyquery.html#queryType

    Returns
    -------

    QueryType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QueryType(number)' gives.
    """
    #  QueryType QNetworkProxyQuery::queryType() const
    return QNetworkProxyQuery.QueryType(self.uglySide.call(
        'ritual_ZNK18QNetworkProxyQuery9queryTypeEv',
    ))

  def peerPort(self) -> int:
    """
    Calls Qt's 'int QNetworkProxyQuery::peerPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxyquery.html#peerPort
    """
    #  int QNetworkProxyQuery::peerPort() const
    return self.uglySide.call('ritual_ZNK18QNetworkProxyQuery8peerPortEv')

  def peerHostName(self) -> str:
    """
    Calls Qt's 'QString QNetworkProxyQuery::peerHostName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyquery.html#peerHostName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkProxyQuery::peerHostName() const
    return self.uglySide.call(
        'ritual_ZNK18QNetworkProxyQuery12peerHostNameEv',
    )

  def localPort(self) -> int:
    """
    Calls Qt's 'int QNetworkProxyQuery::localPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxyquery.html#localPort
    """
    #  int QNetworkProxyQuery::localPort() const
    return self.uglySide.call('ritual_ZNK18QNetworkProxyQuery9localPortEv')

  def protocolTag(self) -> str:
    """
    Calls Qt's 'QString QNetworkProxyQuery::protocolTag() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyquery.html#protocolTag

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkProxyQuery::protocolTag() const
    return self.uglySide.call(
        'ritual_ZNK18QNetworkProxyQuery11protocolTagEv',
    )

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QNetworkProxyQuery::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxyquery.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QNetworkProxyQuery::url() const
    address = self.uglySide.call('ritual_ZNK18QNetworkProxyQuery3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QueryType)
  def setQueryType(self, type: QueryType) -> None:
    """
    Calls Qt's 'void QNetworkProxyQuery::setQueryType(QueryType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyquery.html#setQueryType

    Parameters
    ----------

    type : QueryType
      Passed on as its number.
    """
    #  void QNetworkProxyQuery::setQueryType(QueryType type)
    self.uglySide.call(
        'ritual_ZN18QNetworkProxyQuery12setQueryTypeENS_9QueryTypeE',
        type.value,
    )

  @overload(int)
  def setPeerPort(self, port: int) -> None:
    """
    Calls Qt's 'void QNetworkProxyQuery::setPeerPort(int port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyquery.html#setPeerPort

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QNetworkProxyQuery::setPeerPort(int port)
    self.uglySide.call('ritual_ZN18QNetworkProxyQuery11setPeerPortEi', port)

  @overload(str)
  def setPeerHostName(self, hostname: str) -> None:
    """
    Calls Qt's 'void QNetworkProxyQuery::setPeerHostName(const QString
    &hostname)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyquery.html#setPeerHostName

    Parameters
    ----------

    hostname : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkProxyQuery::setPeerHostName(const QString &hostname)
    self.uglySide.call(
        'ritual_ZN18QNetworkProxyQuery15setPeerHostNameERK7QString',
        hostname,
    )

  @overload(int)
  def setLocalPort(self, port: int) -> None:
    """
    Calls Qt's 'void QNetworkProxyQuery::setLocalPort(int port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyquery.html#setLocalPort

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QNetworkProxyQuery::setLocalPort(int port)
    self.uglySide.call('ritual_ZN18QNetworkProxyQuery12setLocalPortEi', port)

  @overload(str)
  def setProtocolTag(self, protocolTag: str) -> None:
    """
    Calls Qt's 'void QNetworkProxyQuery::setProtocolTag(const QString
    &protocolTag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyquery.html#setProtocolTag

    Parameters
    ----------

    protocolTag : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkProxyQuery::setProtocolTag(const QString &protocolTag)
    self.uglySide.call(
        'ritual_ZN18QNetworkProxyQuery14setProtocolTagERK7QString',
        protocolTag,
    )

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QNetworkProxyQuery::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxyquery.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QNetworkProxyQuery::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN18QNetworkProxyQuery6setUrlERK4QUrl', self._valueOf(url),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QNetworkProxyQuery) -> bool:
    """
    Calls Qt's 'bool QNetworkProxyQuery::operator==(const QNetworkProxyQuery
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxyquery.html#operator==

    Parameters
    ----------

    other : QNetworkProxyQuery
      Passed on as a value: Qt reads the C++ QNetworkProxyQuery, which stays
      Python's own.
    """
    #  bool QNetworkProxyQuery::operator==(const QNetworkProxyQuery &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QNetworkProxyQueryeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QNetworkProxyQuery) -> bool:
    """
    Calls Qt's 'bool QNetworkProxyQuery::operator!=(const QNetworkProxyQuery
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkproxyquery.html#operator!=

    Parameters
    ----------

    other : QNetworkProxyQuery
      Passed on as a value: Qt reads the C++ QNetworkProxyQuery, which stays
      Python's own.
    """
    #  bool QNetworkProxyQuery::operator!=(const QNetworkProxyQuery &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QNetworkProxyQueryneERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's
    'QNetworkProxyQuery::QNetworkProxyQuery()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyquery.html#QNetworkProxyQuery
    """
    #  QNetworkProxyQuery::QNetworkProxyQuery()
    self._noteCreation(QNetworkProxyQuery, lambda: Rituals.call(
        'ritual_ZN18QNetworkProxyQueryC1Ev',
    ))

  @overload(QUrl)
  @overload(QUrl, QueryType)
  def __init__(
      self,
      requestUrl: QUrl,
      queryType: QueryType = QueryType.UrlRequest,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkProxyQuery::QNetworkProxyQuery(const QUrl &requestUrl, QueryType
    queryType)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyquery.html#QNetworkProxyQuery

    Parameters
    ----------

    requestUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    queryType : QueryType
      Passed on as its number. May be left out, as in Qt: it is then
      QueryType.UrlRequest.
    """
    #  QNetworkProxyQuery::QNetworkProxyQuery(const QUrl &requestUrl,
    #      QueryType queryType)
    self._noteCreation(QNetworkProxyQuery, lambda: Rituals.call(
        'ritual_ZN18QNetworkProxyQueryC1ERK4QUrlNS_9QueryTypeE',
        self._valueOf(requestUrl), queryType.value,
    ))

  @overload(str, int)
  @overload(str, int, str)
  @overload(str, int, str, QueryType)
  def __init__(
      self,
      hostname: str,
      port: int,
      protocolTag: str = '',
      queryType: QueryType = QueryType.TcpSocket,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkProxyQuery::QNetworkProxyQuery(const QString &hostname, int
    port, const QString &protocolTag, QueryType queryType)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyquery.html#QNetworkProxyQuery

    Parameters
    ----------

    hostname : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.

    protocolTag : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    queryType : QueryType
      Passed on as its number. May be left out, as in Qt: it is then
      QueryType.TcpSocket.
    """
    #  QNetworkProxyQuery::QNetworkProxyQuery(const QString &hostname, int
    #      port, const QString &protocolTag, QueryType queryType)
    self._noteCreation(QNetworkProxyQuery, lambda: Rituals.call(
        'ritual_ZN18QNetworkProxyQueryC1ERK7QStringiS2_NS_9QueryTypeE',
        hostname, port, protocolTag, queryType.value,
    ))

  @overload(int)
  @overload(int, str)
  @overload(int, str, QueryType)
  def __init__(
      self,
      bindPort: int,
      protocolTag: str = '',
      queryType: QueryType = QueryType.TcpServer,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkProxyQuery::QNetworkProxyQuery(quint16 bindPort, const QString
    &protocolTag, QueryType queryType)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyquery.html#QNetworkProxyQuery

    Parameters
    ----------

    bindPort : int
      Passed on as it is.

    protocolTag : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    queryType : QueryType
      Passed on as its number. May be left out, as in Qt: it is then
      QueryType.TcpServer.
    """
    #  QNetworkProxyQuery::QNetworkProxyQuery(quint16 bindPort, const QString
    #      &protocolTag, QueryType queryType)
    self._noteCreation(QNetworkProxyQuery, lambda: Rituals.call(
        'ritual_ZN18QNetworkProxyQueryC1EtRK7QStringNS_9QueryTypeE',
        bindPort, protocolTag, queryType.value,
    ))

  @overload(THIS)
  def __init__(self, other: QNetworkProxyQuery) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkProxyQuery::QNetworkProxyQuery(const QNetworkProxyQuery
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkproxyquery.html#QNetworkProxyQuery

    Parameters
    ----------

    other : QNetworkProxyQuery
      Passed on as a value: Qt reads the C++ QNetworkProxyQuery, which stays
      Python's own.
    """
    #  QNetworkProxyQuery::QNetworkProxyQuery(const QNetworkProxyQuery
    #      &other)
    self._noteCreation(QNetworkProxyQuery, lambda: Rituals.call(
        'ritual_ZN18QNetworkProxyQueryC1ERKS_', self._valueOf(other),
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
    Qt's 'void QNetworkProxyQuery::swap(QNetworkProxyQuery &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkProxyQuery.swap' has no cute function yet. Qt's 'void "
        "QNetworkProxyQuery::swap(QNetworkProxyQuery &other)': takes a type "
        "Python has no way to hand over yet.")
