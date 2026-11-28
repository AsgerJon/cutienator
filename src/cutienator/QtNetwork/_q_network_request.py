"""
QNetworkRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkrequest.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QObject, QUrl, QVariant
  from . import QHttp1Configuration, QHttp2Configuration, QHttpHeaders
  from . import QSslConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHttp1Configuration = WAIT['QHttp1Configuration']
  QHttp2Configuration = WAIT['QHttp2Configuration']
  QHttpHeaders = WAIT['QHttpHeaders']
  QObject = WAIT['QObject']
  QSslConfiguration = WAIT['QSslConfiguration']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkRequest: a plain Python object standing in
  front of one C++ QNetworkRequest.

  C++ hands a QNetworkRequest around as a copy, so every C++ QNetworkRequest
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNetworkRequest that has a ritual and that Python
  can call so far, 34 names in all: '__eq__', '__ne__', 'url', 'setUrl',
  'headers', 'setHeaders', 'header', 'setHeader', 'hasRawHeader',
  'rawHeaderList', 'rawHeader', 'setRawHeader', 'attribute', 'setAttribute',
  'sslConfiguration', 'setSslConfiguration', 'setOriginatingObject',
  'originatingObject', 'priority', 'setPriority', 'maximumRedirectsAllowed',
  'setMaximumRedirectsAllowed', 'peerVerifyName', 'setPeerVerifyName',
  'http1Configuration', 'setHttp1Configuration', 'http2Configuration',
  'setHttp2Configuration', 'decompressedSafetyCheckThreshold',
  'setDecompressedSafetyCheckThreshold', 'tcpKeepAliveProbeCount',
  'setTcpKeepAliveProbeCount', 'transferTimeout', 'setTransferTimeout'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkRequest::~QNetworkRequest()': the destructor: Python
    removes its C++ QNetworkRequest by it, and has no other use for it.
  - Qt's 'QNetworkRequest &QNetworkRequest::operator=(QNetworkRequest
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QNetworkRequest &QNetworkRequest::operator=(const QNetworkRequest
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QNetworkRequest::swap(QNetworkRequest &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QNetworkRequest::setHeaders(QHttpHeaders &&newHeaders)': takes
    a type Python has no way to hand over yet.
  - Qt's 'std::chrono::seconds
    QNetworkRequest::tcpKeepAliveIdleTimeBeforeProbes() const': gives a type
    Python has no way to take yet.
  - Qt's 'void
    QNetworkRequest::setTcpKeepAliveIdleTimeBeforeProbes(std::chrono::seconds
    idle)': takes a type Python has no way to hand over yet.
  - Qt's 'std::chrono::seconds
    QNetworkRequest::tcpKeepAliveIntervalBetweenProbes() const': gives a type
    Python has no way to take yet.
  - Qt's 'void
    QNetworkRequest::setTcpKeepAliveIntervalBetweenProbes(std::chrono::
    seconds interval)': takes a type Python has no way to hand over yet.
  - Qt's 'std::chrono::milliseconds
    QNetworkRequest::transferTimeoutAsDuration() const': gives a type Python
    has no way to take yet.
  - Qt's 'void QNetworkRequest::setTransferTimeout(std::chrono::milliseconds
    duration)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QNetworkRequest::doSetIdleTimeBeforeProbes(std::chrono::duration<int>
    idle)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QNetworkRequest::doSetIntervalBetweenProbes(std::chrono::duration<int>
    interval)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 53 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QNetworkRequest is created at the first use, not by
    'QNetworkRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkRequest back gives a copy the ritual made for
    Python, in a new cute QNetworkRequest.
  - Each name of Qt's QNetworkRequest that has no cute function yet,
    'doSetIdleTimeBeforeProbes', 'doSetIntervalBetweenProbes',
    'setTcpKeepAliveIdleTimeBeforeProbes',
    'setTcpKeepAliveIntervalBetweenProbes', 'swap',
    'tcpKeepAliveIdleTimeBeforeProbes', 'tcpKeepAliveIntervalBetweenProbes',
    'transferTimeoutAsDuration', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QNetworkRequest, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Attribute(CuteNum):
    """
    The enum 'QNetworkRequest::Attribute' of Qt, with the 32 names Qt gives
    in it.
    """

    HttpStatusCodeAttribute = Kee[int](0)
    HttpReasonPhraseAttribute = Kee[int](1)
    RedirectionTargetAttribute = Kee[int](2)
    ConnectionEncryptedAttribute = Kee[int](3)
    CacheLoadControlAttribute = Kee[int](4)
    CacheSaveControlAttribute = Kee[int](5)
    SourceIsFromCacheAttribute = Kee[int](6)
    DoNotBufferUploadDataAttribute = Kee[int](7)
    HttpPipeliningAllowedAttribute = Kee[int](8)
    HttpPipeliningWasUsedAttribute = Kee[int](9)
    CustomVerbAttribute = Kee[int](10)
    CookieLoadControlAttribute = Kee[int](11)
    AuthenticationReuseAttribute = Kee[int](12)
    CookieSaveControlAttribute = Kee[int](13)
    MaximumDownloadBufferSizeAttribute = Kee[int](14)
    DownloadBufferAttribute = Kee[int](15)
    SynchronousRequestAttribute = Kee[int](16)
    BackgroundRequestAttribute = Kee[int](17)
    EmitAllUploadProgressSignalsAttribute = Kee[int](18)
    Http2AllowedAttribute = Kee[int](19)
    Http2WasUsedAttribute = Kee[int](20)
    OriginalContentLengthAttribute = Kee[int](21)
    RedirectPolicyAttribute = Kee[int](22)
    Http2DirectAttribute = Kee[int](23)
    ResourceTypeAttribute = Kee[int](24)
    AutoDeleteReplyOnFinishAttribute = Kee[int](25)
    ConnectionCacheExpiryTimeoutSecondsAttribute = Kee[int](26)
    Http2CleartextAllowedAttribute = Kee[int](27)
    UseCredentialsAttribute = Kee[int](28)
    FullLocalServerNameAttribute = Kee[int](29)
    User = Kee[int](1000)
    UserMax = Kee[int](32767)

  class CacheLoadControl(CuteNum):
    """
    The enum 'QNetworkRequest::CacheLoadControl' of Qt, with the 4 names Qt
    gives in it.
    """

    AlwaysNetwork = Kee[int](0)
    PreferNetwork = Kee[int](1)
    PreferCache = Kee[int](2)
    AlwaysCache = Kee[int](3)

  class KnownHeaders(CuteNum):
    """
    The enum 'QNetworkRequest::KnownHeaders' of Qt, with the 14 names Qt
    gives in it.
    """

    ContentTypeHeader = Kee[int](0)
    ContentLengthHeader = Kee[int](1)
    LocationHeader = Kee[int](2)
    LastModifiedHeader = Kee[int](3)
    CookieHeader = Kee[int](4)
    SetCookieHeader = Kee[int](5)
    ContentDispositionHeader = Kee[int](6)
    UserAgentHeader = Kee[int](7)
    ServerHeader = Kee[int](8)
    IfModifiedSinceHeader = Kee[int](9)
    ETagHeader = Kee[int](10)
    IfMatchHeader = Kee[int](11)
    IfNoneMatchHeader = Kee[int](12)
    NumKnownHeaders = Kee[int](13)

  class LoadControl(CuteNum):
    """
    The enum 'QNetworkRequest::LoadControl' of Qt, with the 2 names Qt gives
    in it.
    """

    Automatic = Kee[int](0)
    Manual = Kee[int](1)

  class Priority(CuteNum):
    """
    The enum 'QNetworkRequest::Priority' of Qt, with the 3 names Qt gives in
    it.
    """

    HighPriority = Kee[int](1)
    NormalPriority = Kee[int](3)
    LowPriority = Kee[int](5)

  class RedirectPolicy(CuteNum):
    """
    The enum 'QNetworkRequest::RedirectPolicy' of Qt, with the 4 names Qt
    gives in it.
    """

    ManualRedirectPolicy = Kee[int](0)
    NoLessSafeRedirectPolicy = Kee[int](1)
    SameOriginRedirectPolicy = Kee[int](2)
    UserVerifiedRedirectPolicy = Kee[int](3)

  class TransferTimeoutConstant(CuteNum):
    """
    The enum 'QNetworkRequest::TransferTimeoutConstant' of Qt, with the 1
    names Qt gives in it.
    """

    DefaultTransferTimeoutConstant = Kee[int](30000)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkRequest'

  #  Qt's '~QNetworkRequest()'. Naming it makes this a value class: Python
  #  owns every C++ QNetworkRequest behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QNetworkRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QNetworkRequest::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QNetworkRequest::url() const
    address = self.uglySide.call('ritual_ZNK15QNetworkRequest3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def headers(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QNetworkRequest::headers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#headers

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QNetworkRequest::headers() const
    address = self.uglySide.call('ritual_ZNK15QNetworkRequest7headersEv')
    from . import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  @overload(KnownHeaders)
  def header(self, header: KnownHeaders) -> QVariant:
    """
    Calls Qt's 'QVariant QNetworkRequest::header(KnownHeaders header) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#header

    Parameters
    ----------

    header : KnownHeaders
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QNetworkRequest::header(KnownHeaders header) const
    address = self.uglySide.call(
        'ritual_ZNK15QNetworkRequest6headerENS_12KnownHeadersE',
        header.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def hasRawHeader(self, headerName: str) -> bool:
    """
    Calls Qt's 'bool QNetworkRequest::hasRawHeader(QAnyStringView headerName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#hasRawHeader

    Parameters
    ----------

    headerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QNetworkRequest::hasRawHeader(QAnyStringView headerName) const
    return self.uglySide.call(
        'ritual_ZNK15QNetworkRequest12hasRawHeaderE14QAnyStringView',
        headerName,
    )

  def rawHeaderList(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QNetworkRequest::rawHeaderList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#rawHeaderList

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QNetworkRequest::rawHeaderList() const
    address = self.uglySide.call(
        'ritual_ZNK15QNetworkRequest13rawHeaderListEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(str)
  def rawHeader(self, headerName: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNetworkRequest::rawHeader(QAnyStringView
    headerName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#rawHeader

    Parameters
    ----------

    headerName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNetworkRequest::rawHeader(QAnyStringView headerName) const
    address = self.uglySide.call(
        'ritual_ZNK15QNetworkRequest9rawHeaderE14QAnyStringView', headerName,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(Attribute)
  @overload(Attribute, QVariant)
  def attribute(
      self,
      code: Attribute,
      defaultValue: Optional[QVariant] = None,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QNetworkRequest::attribute(Attribute code, const
    QVariant &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#attribute

    Parameters
    ----------

    code : Attribute
      Passed on as its number.

    defaultValue : Optional[QVariant]
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own. May be left out, as in Qt: a new 'QVariant()' is then passed on.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QNetworkRequest::attribute(Attribute code, const QVariant
    #      &defaultValue) const
    if defaultValue is None:
      from ..QtCore import QVariant
      defaultValue = QVariant()
    address = self.uglySide.call(
        'ritual_ZNK15QNetworkRequest9attributeENS_9AttributeERK8QVariant',
        code.value, self._valueOf(defaultValue),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QNetworkRequest::sslConfiguration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QNetworkRequest::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK15QNetworkRequest16sslConfigurationEv',
    )
    from . import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  def originatingObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QNetworkRequest::originatingObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#originatingObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QNetworkRequest::originatingObject() const
    address = self.uglySide.call(
        'ritual_ZNK15QNetworkRequest17originatingObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def priority(self) -> Priority:
    """
    Calls Qt's 'Priority QNetworkRequest::priority() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#priority

    Returns
    -------

    Priority
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Priority(number)' gives.
    """
    #  Priority QNetworkRequest::priority() const
    return QNetworkRequest.Priority(self.uglySide.call(
        'ritual_ZNK15QNetworkRequest8priorityEv',
    ))

  def maximumRedirectsAllowed(self) -> int:
    """
    Calls Qt's 'int QNetworkRequest::maximumRedirectsAllowed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#maximumRedirectsAllowed
    """
    #  int QNetworkRequest::maximumRedirectsAllowed() const
    return self.uglySide.call(
        'ritual_ZNK15QNetworkRequest23maximumRedirectsAllowedEv',
    )

  def peerVerifyName(self) -> str:
    """
    Calls Qt's 'QString QNetworkRequest::peerVerifyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#peerVerifyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkRequest::peerVerifyName() const
    return self.uglySide.call(
        'ritual_ZNK15QNetworkRequest14peerVerifyNameEv',
    )

  def http1Configuration(self) -> QHttp1Configuration:
    """
    Calls Qt's 'QHttp1Configuration QNetworkRequest::http1Configuration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#http1Configuration

    Returns
    -------

    QHttp1Configuration
      A new cute QHttp1Configuration around the copy Qt gave back. Python
      owns it.
    """
    #  QHttp1Configuration QNetworkRequest::http1Configuration() const
    address = self.uglySide.call(
        'ritual_ZNK15QNetworkRequest18http1ConfigurationEv',
    )
    from . import QHttp1Configuration
    return QHttp1Configuration._cuteOwning(address)

  def http2Configuration(self) -> QHttp2Configuration:
    """
    Calls Qt's 'QHttp2Configuration QNetworkRequest::http2Configuration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#http2Configuration

    Returns
    -------

    QHttp2Configuration
      A new cute QHttp2Configuration around the copy Qt gave back. Python
      owns it.
    """
    #  QHttp2Configuration QNetworkRequest::http2Configuration() const
    address = self.uglySide.call(
        'ritual_ZNK15QNetworkRequest18http2ConfigurationEv',
    )
    from . import QHttp2Configuration
    return QHttp2Configuration._cuteOwning(address)

  def decompressedSafetyCheckThreshold(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkRequest::decompressedSafetyCheckThreshold()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html
    """
    #  qint64 QNetworkRequest::decompressedSafetyCheckThreshold() const
    return self.uglySide.call(
        'ritual_ZNK15QNetworkRequest32decompressedSafetyCheckThresholdEv',
    )

  def tcpKeepAliveProbeCount(self) -> int:
    """
    Calls Qt's 'int QNetworkRequest::tcpKeepAliveProbeCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#tcpKeepAliveProbeCount
    """
    #  int QNetworkRequest::tcpKeepAliveProbeCount() const
    return self.uglySide.call(
        'ritual_ZNK15QNetworkRequest22tcpKeepAliveProbeCountEv',
    )

  def transferTimeout(self) -> int:
    """
    Calls Qt's 'int QNetworkRequest::transferTimeout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#transferTimeout
    """
    #  int QNetworkRequest::transferTimeout() const
    return self.uglySide.call(
        'ritual_ZNK15QNetworkRequest15transferTimeoutEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QNetworkRequest::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest6setUrlERK4QUrl', self._valueOf(url),
    )

  @overload(QHttpHeaders)
  def setHeaders(self, newHeaders: QHttpHeaders) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setHeaders(const QHttpHeaders
    &newHeaders)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#setHeaders

    Parameters
    ----------

    newHeaders : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.
    """
    #  void QNetworkRequest::setHeaders(const QHttpHeaders &newHeaders)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest10setHeadersERK12QHttpHeaders',
        self._valueOf(newHeaders),
    )

  @overload(KnownHeaders, QVariant)
  def setHeader(self, header: KnownHeaders, value: QVariant) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setHeader(KnownHeaders header, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#setHeader

    Parameters
    ----------

    header : KnownHeaders
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QNetworkRequest::setHeader(KnownHeaders header, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest9setHeaderENS_12KnownHeadersERK8QVariant',
        header.value, self._valueOf(value),
    )

  @overload(QByteArray, QByteArray)
  def setRawHeader(self, headerName: QByteArray, value: QByteArray) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setRawHeader(const QByteArray
    &headerName, const QByteArray &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#setRawHeader

    Parameters
    ----------

    headerName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNetworkRequest::setRawHeader(const QByteArray &headerName, const
    #      QByteArray &value)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest12setRawHeaderERK10QByteArrayS2_',
        self._valueOf(headerName), self._valueOf(value),
    )

  @overload(Attribute, QVariant)
  def setAttribute(self, code: Attribute, value: QVariant) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setAttribute(Attribute code, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#setAttribute

    Parameters
    ----------

    code : Attribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QNetworkRequest::setAttribute(Attribute code, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest12setAttributeENS_9AttributeERK8QVariant',
        code.value, self._valueOf(value),
    )

  @overload(QSslConfiguration)
  def setSslConfiguration(self, configuration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setSslConfiguration(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#setSslConfiguration

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QNetworkRequest::setSslConfiguration(const QSslConfiguration
    #      &configuration)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest19setSslConfigurationERK17QSslConfigurat'
        'ion',
        self._valueOf(configuration),
    )

  @overload(QObject)
  @overload(NoneType)
  def setOriginatingObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setOriginatingObject(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#setOriginatingObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkRequest::setOriginatingObject(QObject *object)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest20setOriginatingObjectEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(Priority)
  def setPriority(self, priority: Priority) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setPriority(Priority priority)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#setPriority

    Parameters
    ----------

    priority : Priority
      Passed on as its number.
    """
    #  void QNetworkRequest::setPriority(Priority priority)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest11setPriorityENS_8PriorityE',
        priority.value,
    )

  @overload(int)
  def setMaximumRedirectsAllowed(self, maximumRedirectsAllowed: int) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setMaximumRedirectsAllowed(int
    maximumRedirectsAllowed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#setMaximumRedirectsAllowed

    Parameters
    ----------

    maximumRedirectsAllowed : int
      Passed on as it is.
    """
    #  void QNetworkRequest::setMaximumRedirectsAllowed(int
    #      maximumRedirectsAllowed)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest26setMaximumRedirectsAllowedEi',
        maximumRedirectsAllowed,
    )

  @overload(str)
  def setPeerVerifyName(self, peerName: str) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setPeerVerifyName(const QString
    &peerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#setPeerVerifyName

    Parameters
    ----------

    peerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkRequest::setPeerVerifyName(const QString &peerName)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest17setPeerVerifyNameERK7QString', peerName,
    )

  @overload(QHttp1Configuration)
  def setHttp1Configuration(
      self,
      configuration: QHttp1Configuration,
  ) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setHttp1Configuration(const
    QHttp1Configuration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#setHttp1Configuration

    Parameters
    ----------

    configuration : QHttp1Configuration
      Passed on as a value: Qt reads the C++ QHttp1Configuration, which stays
      Python's own.
    """
    #  void QNetworkRequest::setHttp1Configuration(const QHttp1Configuration
    #      &configuration)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest21setHttp1ConfigurationERK19QHttp1Config'
        'uration',
        self._valueOf(configuration),
    )

  @overload(QHttp2Configuration)
  def setHttp2Configuration(
      self,
      configuration: QHttp2Configuration,
  ) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setHttp2Configuration(const
    QHttp2Configuration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#setHttp2Configuration

    Parameters
    ----------

    configuration : QHttp2Configuration
      Passed on as a value: Qt reads the C++ QHttp2Configuration, which stays
      Python's own.
    """
    #  void QNetworkRequest::setHttp2Configuration(const QHttp2Configuration
    #      &configuration)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest21setHttp2ConfigurationERK19QHttp2Config'
        'uration',
        self._valueOf(configuration),
    )

  @overload(int)
  def setDecompressedSafetyCheckThreshold(self, threshold: int) -> None:
    """
    Calls Qt's 'void
    QNetworkRequest::setDecompressedSafetyCheckThreshold(qint64 threshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html

    Parameters
    ----------

    threshold : int
      Passed on as it is.
    """
    #  void QNetworkRequest::setDecompressedSafetyCheckThreshold(qint64
    #      threshold)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest35setDecompressedSafetyCheckThresholdEx',
        threshold,
    )

  @overload(int)
  def setTcpKeepAliveProbeCount(self, probes: int) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setTcpKeepAliveProbeCount(int probes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#setTcpKeepAliveProbeCount

    Parameters
    ----------

    probes : int
      Passed on as it is.
    """
    #  void QNetworkRequest::setTcpKeepAliveProbeCount(int probes)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest25setTcpKeepAliveProbeCountEi', probes,
    )

  @overload(int)
  def setTransferTimeout(self, timeout: int) -> None:
    """
    Calls Qt's 'void QNetworkRequest::setTransferTimeout(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#setTransferTimeout

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void QNetworkRequest::setTransferTimeout(int timeout)
    self.uglySide.call(
        'ritual_ZN15QNetworkRequest18setTransferTimeoutEi', timeout,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QNetworkRequest) -> bool:
    """
    Calls Qt's 'bool QNetworkRequest::operator==(const QNetworkRequest
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#operator==

    Parameters
    ----------

    other : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.
    """
    #  bool QNetworkRequest::operator==(const QNetworkRequest &other) const
    return self.uglySide.call(
        'ritual_ZNK15QNetworkRequesteqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QNetworkRequest) -> bool:
    """
    Calls Qt's 'bool QNetworkRequest::operator!=(const QNetworkRequest
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkrequest.html#operator!=

    Parameters
    ----------

    other : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.
    """
    #  bool QNetworkRequest::operator!=(const QNetworkRequest &other) const
    return self.uglySide.call(
        'ritual_ZNK15QNetworkRequestneERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QNetworkRequest::QNetworkRequest()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#QNetworkRequest
    """
    #  QNetworkRequest::QNetworkRequest()
    self._noteCreation(QNetworkRequest, lambda: Rituals.call(
        'ritual_ZN15QNetworkRequestC1Ev',
    ))

  @overload(QUrl)
  def __init__(self, url: QUrl) -> None:
    """
    Notes what was given, for Qt's 'QNetworkRequest::QNetworkRequest(const
    QUrl &url)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#QNetworkRequest

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QNetworkRequest::QNetworkRequest(const QUrl &url)
    self._noteCreation(QNetworkRequest, lambda: Rituals.call(
        'ritual_ZN15QNetworkRequestC1ERK4QUrl', self._valueOf(url),
    ))

  @overload(THIS)
  def __init__(self, other: QNetworkRequest) -> None:
    """
    Notes what was given, for Qt's 'QNetworkRequest::QNetworkRequest(const
    QNetworkRequest &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequest.html#QNetworkRequest

    Parameters
    ----------

    other : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.
    """
    #  QNetworkRequest::QNetworkRequest(const QNetworkRequest &other)
    self._noteCreation(QNetworkRequest, lambda: Rituals.call(
        'ritual_ZN15QNetworkRequestC1ERKS_', self._valueOf(other),
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
  def doSetIdleTimeBeforeProbes(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkRequest::doSetIdleTimeBeforeProbes(std::chrono::duration<int>
    idle)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkRequest.doSetIdleTimeBeforeProbes' has no cute function "
        "yet. Qt's 'void "
        "QNetworkRequest::doSetIdleTimeBeforeProbes(std::chrono::duration<in"
        "t> idle)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def doSetIntervalBetweenProbes(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkRequest::doSetIntervalBetweenProbes(std::chrono::duration<int>
    interval)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkRequest.doSetIntervalBetweenProbes' has no cute function "
        "yet. Qt's 'void "
        "QNetworkRequest::doSetIntervalBetweenProbes(std::chrono::duration<i"
        "nt> interval)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setTcpKeepAliveIdleTimeBeforeProbes(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkRequest::setTcpKeepAliveIdleTimeBeforeProbes(std::chrono::seconds
    idle)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkRequest.setTcpKeepAliveIdleTimeBeforeProbes' has no cute "
        "function yet. Qt's 'void "
        "QNetworkRequest::setTcpKeepAliveIdleTimeBeforeProbes(std::chrono::s"
        "econds idle)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setTcpKeepAliveIntervalBetweenProbes(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkRequest::setTcpKeepAliveIntervalBetweenProbes(std::chrono::
    seconds interval)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkRequest.setTcpKeepAliveIntervalBetweenProbes' has no cute "
        "function yet. Qt's 'void "
        "QNetworkRequest::setTcpKeepAliveIntervalBetweenProbes(std::chrono::"
        "seconds interval)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QNetworkRequest::swap(QNetworkRequest &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkRequest.swap' has no cute function yet. Qt's 'void "
        "QNetworkRequest::swap(QNetworkRequest &other)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def tcpKeepAliveIdleTimeBeforeProbes(*__, **_) -> Never:
    """
    Qt's 'std::chrono::seconds
    QNetworkRequest::tcpKeepAliveIdleTimeBeforeProbes() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkRequest.tcpKeepAliveIdleTimeBeforeProbes' has no cute "
        "function yet. Qt's 'std::chrono::seconds "
        "QNetworkRequest::tcpKeepAliveIdleTimeBeforeProbes() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def tcpKeepAliveIntervalBetweenProbes(*__, **_) -> Never:
    """
    Qt's 'std::chrono::seconds
    QNetworkRequest::tcpKeepAliveIntervalBetweenProbes() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkRequest.tcpKeepAliveIntervalBetweenProbes' has no cute "
        "function yet. Qt's 'std::chrono::seconds "
        "QNetworkRequest::tcpKeepAliveIntervalBetweenProbes() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def transferTimeoutAsDuration(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds
    QNetworkRequest::transferTimeoutAsDuration() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkRequest.transferTimeoutAsDuration' has no cute function "
        "yet. Qt's 'std::chrono::milliseconds "
        "QNetworkRequest::transferTimeoutAsDuration() const': gives a type "
        "Python has no way to take yet.")
