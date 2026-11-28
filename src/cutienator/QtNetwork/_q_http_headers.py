"""
QHttpHeaders binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qhttpheaders.h, Qt 6.12.0. Changes made here are lost.
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

  from ..QtCore import QByteArray, QByteArrayView, QDateTime, QDebug
  from ..QtCore import QLatin1String
  from . import QHttpHeaderRangeSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QDateTime = WAIT['QDateTime']
  QDebug = WAIT['QDebug']
  QHttpHeaderRangeSet = WAIT['QHttpHeaderRangeSet']


class QHttpHeaders(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpHeaders: a plain Python object standing in front
  of one C++ QHttpHeaders.

  C++ hands a QHttpHeaders around as a copy, so every C++ QHttpHeaders behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpHeaders that has a ritual and that Python can
  call so far, 21 names in all: 'append', 'insert', 'replace',
  'replaceOrAppend', 'contains', 'clear', 'removeAll', 'removeAt', 'value',
  'values', 'valueAt', 'nameAt', 'combinedValue', 'setDateTimeValue',
  'setRangeValues', 'size', 'reserve', 'isEmpty', 'wellKnownHeaderName',
  '__rlshift__', 'verify'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpHeaders::~QHttpHeaders()': the destructor: Python removes its
    C++ QHttpHeaders by it, and has no other use for it.
  - Qt's 'QHttpHeaders::QHttpHeaders(QHttpHeaders &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QHttpHeaders &QHttpHeaders::operator=(const QHttpHeaders &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QHttpHeaders &QHttpHeaders::operator=(QHttpHeaders &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QHttpHeaders::swap(QHttpHeaders &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'std::optional<qint64> QHttpHeaders::intValue(QAnyStringView name)
    const': gives a type Python has no way to take yet.
  - Qt's 'std::optional<qint64> QHttpHeaders::intValue(WellKnownHeader name)
    const': gives a type Python has no way to take yet.
  - Qt's 'std::optional<QList<qint64>> QHttpHeaders::intValues(QAnyStringView
    name) const': gives a type Python has no way to take yet.
  - Qt's 'std::optional<QList<qint64>>
    QHttpHeaders::intValues(WellKnownHeader name) const': gives a type Python
    has no way to take yet.
  - Qt's 'std::optional<qint64> QHttpHeaders::intValueAt(qsizetype i) const':
    gives a type Python has no way to take yet.
  - Qt's 'std::optional<QDateTime> QHttpHeaders::dateTimeValue(QAnyStringView
    name) const': gives a type Python has no way to take yet.
  - Qt's 'std::optional<QDateTime>
    QHttpHeaders::dateTimeValue(WellKnownHeader name) const': gives a type
    Python has no way to take yet.
  - Qt's 'std::optional<QList<QDateTime>>
    QHttpHeaders::dateTimeValues(QAnyStringView name) const': gives a type
    Python has no way to take yet.
  - Qt's 'std::optional<QList<QDateTime>>
    QHttpHeaders::dateTimeValues(WellKnownHeader name) const': gives a type
    Python has no way to take yet.
  - Qt's 'std::optional<QDateTime> QHttpHeaders::dateTimeValueAt(qsizetype i)
    const': gives a type Python has no way to take yet.
  - Qt's 'std::optional<QHttpHeaderRangeSet> QHttpHeaders::rangeValues()
    const': gives a type Python has no way to take yet.
  - Qt's 'QHttpHeaders QHttpHeaders::fromListOfPairs(const
    QList<std::pair<QByteArray, QByteArray>> &headers)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QHttpHeaders QHttpHeaders::fromMultiMap(const QMultiMap<QByteArray,
    QByteArray> &headers)': takes a type Python has no way to hand over yet.
  - Qt's 'QHttpHeaders QHttpHeaders::fromMultiHash(const
    QMultiHash<QByteArray, QByteArray> &headers)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QList<std::pair<QByteArray, QByteArray>>
    QHttpHeaders::toListOfPairs() const': gives a type Python has no way to
    take yet.
  - Qt's 'QMultiMap<QByteArray, QByteArray> QHttpHeaders::toMultiMap()
    const': gives a type Python has no way to take yet.
  - Qt's 'QMultiHash<QByteArray, QByteArray> QHttpHeaders::toMultiHash()
    const': gives a type Python has no way to take yet.
  - Qt's 'QDataStream &operator<<(QDataStream &stream, const QHttpHeaders
    &headers)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &stream, QHttpHeaders
    &headers)': an operator between other classes, written inside this one.

  What has no ritual
  ------------------

  3 of the 60 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QHttpHeaders is created at the first use, not by
    'QHttpHeaders(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpHeaders back gives a copy the ritual made for
    Python, in a new cute QHttpHeaders.
  - Each name of Qt's QHttpHeaders that has no cute function yet,
    'dateTimeValue', 'dateTimeValueAt', 'dateTimeValues', 'fromListOfPairs',
    'fromMultiHash', 'fromMultiMap', 'intValue', 'intValueAt', 'intValues',
    'rangeValues', 'swap', 'toListOfPairs', 'toMultiHash', 'toMultiMap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QHttpHeaders, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class WellKnownHeader(CuteNum, scoped=True):
    """
    The enum 'QHttpHeaders::WellKnownHeader' of Qt, with the 177 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    AIM = Kee[int](0)
    Accept = Kee[int](1)
    AcceptAdditions = Kee[int](2)
    AcceptCH = Kee[int](3)
    AcceptDatetime = Kee[int](4)
    AcceptEncoding = Kee[int](5)
    AcceptFeatures = Kee[int](6)
    AcceptLanguage = Kee[int](7)
    AcceptPatch = Kee[int](8)
    AcceptPost = Kee[int](9)
    AcceptRanges = Kee[int](10)
    AcceptSignature = Kee[int](11)
    AccessControlAllowCredentials = Kee[int](12)
    AccessControlAllowHeaders = Kee[int](13)
    AccessControlAllowMethods = Kee[int](14)
    AccessControlAllowOrigin = Kee[int](15)
    AccessControlExposeHeaders = Kee[int](16)
    AccessControlMaxAge = Kee[int](17)
    AccessControlRequestHeaders = Kee[int](18)
    AccessControlRequestMethod = Kee[int](19)
    Age = Kee[int](20)
    Allow = Kee[int](21)
    ALPN = Kee[int](22)
    AltSvc = Kee[int](23)
    AltUsed = Kee[int](24)
    Alternates = Kee[int](25)
    ApplyToRedirectRef = Kee[int](26)
    AuthenticationControl = Kee[int](27)
    AuthenticationInfo = Kee[int](28)
    Authorization = Kee[int](29)
    CacheControl = Kee[int](30)
    CacheStatus = Kee[int](31)
    CalManagedID = Kee[int](32)
    CalDAVTimezones = Kee[int](33)
    CapsuleProtocol = Kee[int](34)
    CDNCacheControl = Kee[int](35)
    CDNLoop = Kee[int](36)
    CertNotAfter = Kee[int](37)
    CertNotBefore = Kee[int](38)
    ClearSiteData = Kee[int](39)
    ClientCert = Kee[int](40)
    ClientCertChain = Kee[int](41)
    Close = Kee[int](42)
    Connection = Kee[int](43)
    ContentDigest = Kee[int](44)
    ContentDisposition = Kee[int](45)
    ContentEncoding = Kee[int](46)
    ContentID = Kee[int](47)
    ContentLanguage = Kee[int](48)
    ContentLength = Kee[int](49)
    ContentLocation = Kee[int](50)
    ContentRange = Kee[int](51)
    ContentSecurityPolicy = Kee[int](52)
    ContentSecurityPolicyReportOnly = Kee[int](53)
    ContentType = Kee[int](54)
    Cookie = Kee[int](55)
    CrossOriginEmbedderPolicy = Kee[int](56)
    CrossOriginEmbedderPolicyReportOnly = Kee[int](57)
    CrossOriginOpenerPolicy = Kee[int](58)
    CrossOriginOpenerPolicyReportOnly = Kee[int](59)
    CrossOriginResourcePolicy = Kee[int](60)
    DASL = Kee[int](61)
    Date = Kee[int](62)
    DAV = Kee[int](63)
    DeltaBase = Kee[int](64)
    Depth = Kee[int](65)
    Destination = Kee[int](66)
    DifferentialID = Kee[int](67)
    DPoP = Kee[int](68)
    DPoPNonce = Kee[int](69)
    EarlyData = Kee[int](70)
    ETag = Kee[int](71)
    Expect = Kee[int](72)
    ExpectCT = Kee[int](73)
    Expires = Kee[int](74)
    Forwarded = Kee[int](75)
    From = Kee[int](76)
    Hobareg = Kee[int](77)
    Host = Kee[int](78)
    If = Kee[int](79)
    IfMatch = Kee[int](80)
    IfModifiedSince = Kee[int](81)
    IfNoneMatch = Kee[int](82)
    IfRange = Kee[int](83)
    IfScheduleTagMatch = Kee[int](84)
    IfUnmodifiedSince = Kee[int](85)
    IM = Kee[int](86)
    IncludeReferredTokenBindingID = Kee[int](87)
    KeepAlive = Kee[int](88)
    Label = Kee[int](89)
    LastEventID = Kee[int](90)
    LastModified = Kee[int](91)
    Link = Kee[int](92)
    Location = Kee[int](93)
    LockToken = Kee[int](94)
    MaxForwards = Kee[int](95)
    MementoDatetime = Kee[int](96)
    Meter = Kee[int](97)
    MIMEVersion = Kee[int](98)
    Negotiate = Kee[int](99)
    NEL = Kee[int](100)
    ODataEntityId = Kee[int](101)
    ODataIsolation = Kee[int](102)
    ODataMaxVersion = Kee[int](103)
    ODataVersion = Kee[int](104)
    OptionalWWWAuthenticate = Kee[int](105)
    OrderingType = Kee[int](106)
    Origin = Kee[int](107)
    OriginAgentCluster = Kee[int](108)
    OSCORE = Kee[int](109)
    OSLCCoreVersion = Kee[int](110)
    Overwrite = Kee[int](111)
    PingFrom = Kee[int](112)
    PingTo = Kee[int](113)
    Position = Kee[int](114)
    Prefer = Kee[int](115)
    PreferenceApplied = Kee[int](116)
    Priority = Kee[int](117)
    ProxyAuthenticate = Kee[int](118)
    ProxyAuthenticationInfo = Kee[int](119)
    ProxyAuthorization = Kee[int](120)
    ProxyStatus = Kee[int](121)
    PublicKeyPins = Kee[int](122)
    PublicKeyPinsReportOnly = Kee[int](123)
    Range = Kee[int](124)
    RedirectRef = Kee[int](125)
    Referer = Kee[int](126)
    Refresh = Kee[int](127)
    ReplayNonce = Kee[int](128)
    ReprDigest = Kee[int](129)
    RetryAfter = Kee[int](130)
    ScheduleReply = Kee[int](131)
    ScheduleTag = Kee[int](132)
    SecPurpose = Kee[int](133)
    SecTokenBinding = Kee[int](134)
    SecWebSocketAccept = Kee[int](135)
    SecWebSocketExtensions = Kee[int](136)
    SecWebSocketKey = Kee[int](137)
    SecWebSocketProtocol = Kee[int](138)
    SecWebSocketVersion = Kee[int](139)
    Server = Kee[int](140)
    ServerTiming = Kee[int](141)
    SetCookie = Kee[int](142)
    Signature = Kee[int](143)
    SignatureInput = Kee[int](144)
    SLUG = Kee[int](145)
    SoapAction = Kee[int](146)
    StatusURI = Kee[int](147)
    StrictTransportSecurity = Kee[int](148)
    Sunset = Kee[int](149)
    SurrogateCapability = Kee[int](150)
    SurrogateControl = Kee[int](151)
    TCN = Kee[int](152)
    TE = Kee[int](153)
    Timeout = Kee[int](154)
    Topic = Kee[int](155)
    Traceparent = Kee[int](156)
    Tracestate = Kee[int](157)
    Trailer = Kee[int](158)
    TransferEncoding = Kee[int](159)
    TTL = Kee[int](160)
    Upgrade = Kee[int](161)
    Urgency = Kee[int](162)
    UserAgent = Kee[int](163)
    VariantVary = Kee[int](164)
    Vary = Kee[int](165)
    Via = Kee[int](166)
    WantContentDigest = Kee[int](167)
    WantReprDigest = Kee[int](168)
    WWWAuthenticate = Kee[int](169)
    XContentTypeOptions = Kee[int](170)
    XFrameOptions = Kee[int](171)
    AcceptCharset = Kee[int](172)
    CPEPInfo = Kee[int](173)
    Pragma = Kee[int](174)
    ProtocolInfo = Kee[int](175)
    ProtocolQuery = Kee[int](176)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WellKnownHeader)
  def wellKnownHeaderName(name: WellKnownHeader) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView
    QHttpHeaders::wellKnownHeaderName(WellKnownHeader name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaders.html#wellKnownHeaderName

    Parameters
    ----------

    name : WellKnownHeader
      Passed on as its number.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QHttpHeaders::wellKnownHeaderName(WellKnownHeader name)
    address = Rituals.call(
        'ritual_ZN12QHttpHeaders19wellKnownHeaderNameENS_15WellKnownHeaderE',
        name.value,
    )
    from ..QtCore import QByteArrayView
    return QByteArrayView._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpHeaders'

  #  Qt's '~QHttpHeaders()'. Naming it makes this a value class: Python owns
  #  every C++ QHttpHeaders behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QHttpHeadersD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def contains(self, name: str) -> bool:
    """
    Calls Qt's 'bool QHttpHeaders::contains(QAnyStringView name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#contains

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHttpHeaders::contains(QAnyStringView name) const
    return self.uglySide.call(
        'ritual_ZNK12QHttpHeaders8containsE14QAnyStringView', name,
    )

  @overload(WellKnownHeader)
  def contains(self, name: WellKnownHeader) -> bool:
    """
    Calls Qt's 'bool QHttpHeaders::contains(WellKnownHeader name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#contains

    Parameters
    ----------

    name : WellKnownHeader
      Passed on as its number.
    """
    #  bool QHttpHeaders::contains(WellKnownHeader name) const
    return self.uglySide.call(
        'ritual_ZNK12QHttpHeaders8containsENS_15WellKnownHeaderE',
        name.value,
    )

  @overload(str)
  @overload(str, QByteArrayView)
  def value(
      self,
      name: str,
      defaultValue: Optional[QByteArrayView] = None,
  ) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QHttpHeaders::value(QAnyStringView name,
    QByteArrayView defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#value

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    defaultValue : Optional[QByteArrayView]
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own. May be left out, as in Qt: a new 'QByteArrayView()' is
      then passed on.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QHttpHeaders::value(QAnyStringView name, QByteArrayView
    #      defaultValue) const
    if defaultValue is None:
      from ..QtCore import QByteArrayView
      defaultValue = QByteArrayView()
    address = self.uglySide.call(
        'ritual_ZNK12QHttpHeaders5valueE14QAnyStringView14QByteArrayView',
        name, self._valueOf(defaultValue),
    )
    from ..QtCore import QByteArrayView
    return QByteArrayView._cuteOwning(address)

  @overload(WellKnownHeader)
  @overload(WellKnownHeader, QByteArrayView)
  def value(
      self,
      name: WellKnownHeader,
      defaultValue: Optional[QByteArrayView] = None,
  ) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QHttpHeaders::value(WellKnownHeader name,
    QByteArrayView defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#value

    Parameters
    ----------

    name : WellKnownHeader
      Passed on as its number.

    defaultValue : Optional[QByteArrayView]
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own. May be left out, as in Qt: a new 'QByteArrayView()' is
      then passed on.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QHttpHeaders::value(WellKnownHeader name,
    #      QByteArrayView defaultValue) const
    if defaultValue is None:
      from ..QtCore import QByteArrayView
      defaultValue = QByteArrayView()
    address = self.uglySide.call(
        'ritual_ZNK12QHttpHeaders5valueENS_15WellKnownHeaderE14QByteArrayVi'
        'ew',
        name.value, self._valueOf(defaultValue),
    )
    from ..QtCore import QByteArrayView
    return QByteArrayView._cuteOwning(address)

  @overload(str)
  def values(self, name: str) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QHttpHeaders::values(QAnyStringView name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#values

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QHttpHeaders::values(QAnyStringView name) const
    address = self.uglySide.call(
        'ritual_ZNK12QHttpHeaders6valuesE14QAnyStringView', name,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(WellKnownHeader)
  def values(self, name: WellKnownHeader) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QHttpHeaders::values(WellKnownHeader name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#values

    Parameters
    ----------

    name : WellKnownHeader
      Passed on as its number.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QHttpHeaders::values(WellKnownHeader name) const
    address = self.uglySide.call(
        'ritual_ZNK12QHttpHeaders6valuesENS_15WellKnownHeaderE', name.value,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(int)
  def valueAt(self, i: int) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QHttpHeaders::valueAt(qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#valueAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QHttpHeaders::valueAt(qsizetype i) const
    address = self.uglySide.call('ritual_ZNK12QHttpHeaders7valueAtEx', i)
    from ..QtCore import QByteArrayView
    return QByteArrayView._cuteOwning(address)

  @overload(int)
  def nameAt(self, i: int) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QHttpHeaders::nameAt(qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#nameAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QHttpHeaders::nameAt(qsizetype i) const
    address = self.uglySide.call('ritual_ZNK12QHttpHeaders6nameAtEx', i)
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @overload(str)
  def combinedValue(self, name: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpHeaders::combinedValue(QAnyStringView name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#combinedValue

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpHeaders::combinedValue(QAnyStringView name) const
    address = self.uglySide.call(
        'ritual_ZNK12QHttpHeaders13combinedValueE14QAnyStringView', name,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(WellKnownHeader)
  def combinedValue(self, name: WellKnownHeader) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpHeaders::combinedValue(WellKnownHeader name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#combinedValue

    Parameters
    ----------

    name : WellKnownHeader
      Passed on as its number.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpHeaders::combinedValue(WellKnownHeader name) const
    address = self.uglySide.call(
        'ritual_ZNK12QHttpHeaders13combinedValueENS_15WellKnownHeaderE',
        name.value,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QHttpHeaders::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#size
    """
    #  qsizetype QHttpHeaders::size() const
    return self.uglySide.call('ritual_ZNK12QHttpHeaders4sizeEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QHttpHeaders::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#isEmpty
    """
    #  bool QHttpHeaders::isEmpty() const
    return self.uglySide.call('ritual_ZNK12QHttpHeaders7isEmptyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QDateTime)
  def setDateTimeValue(self, name: str, dateTime: QDateTime) -> None:
    """
    Calls Qt's 'void QHttpHeaders::setDateTimeValue(QAnyStringView name,
    const QDateTime &dateTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#setDateTimeValue

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QHttpHeaders::setDateTimeValue(QAnyStringView name, const
    #      QDateTime &dateTime)
    self.uglySide.call(
        'ritual_ZN12QHttpHeaders16setDateTimeValueE14QAnyStringViewRK9QDate'
        'Time',
        name, self._valueOf(dateTime),
    )

  @overload(WellKnownHeader, QDateTime)
  def setDateTimeValue(
      self,
      name: WellKnownHeader,
      dateTime: QDateTime,
  ) -> None:
    """
    Calls Qt's 'void QHttpHeaders::setDateTimeValue(WellKnownHeader name,
    const QDateTime &dateTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#setDateTimeValue

    Parameters
    ----------

    name : WellKnownHeader
      Passed on as its number.

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QHttpHeaders::setDateTimeValue(WellKnownHeader name, const
    #      QDateTime &dateTime)
    self.uglySide.call(
        'ritual_ZN12QHttpHeaders16setDateTimeValueENS_15WellKnownHeaderERK9'
        'QDateTime',
        name.value, self._valueOf(dateTime),
    )

  @overload(QHttpHeaderRangeSet)
  def setRangeValues(self, ranges: QHttpHeaderRangeSet) -> None:
    """
    Calls Qt's 'void QHttpHeaders::setRangeValues(const QHttpHeaderRangeSet
    &ranges)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#setRangeValues

    Parameters
    ----------

    ranges : QHttpHeaderRangeSet
      Passed on as a value: Qt reads the C++ QHttpHeaderRangeSet, which stays
      Python's own.
    """
    #  void QHttpHeaders::setRangeValues(const QHttpHeaderRangeSet &ranges)
    self.uglySide.call(
        'ritual_ZN12QHttpHeaders14setRangeValuesERK19QHttpHeaderRangeSet',
        self._valueOf(ranges),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QHttpHeaders
    &headers)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QHttpHeaders &headers)
    address = Rituals.call(
        'ritual_Zls6QDebugRK12QHttpHeaders',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QHttpHeaders::QHttpHeaders()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#QHttpHeaders
    """
    #  QHttpHeaders::QHttpHeaders()
    self._noteCreation(QHttpHeaders, lambda: Rituals.call(
        'ritual_ZN12QHttpHeadersC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QHttpHeaders) -> None:
    """
    Notes what was given, for Qt's 'QHttpHeaders::QHttpHeaders(const
    QHttpHeaders &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#QHttpHeaders

    Parameters
    ----------

    other : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.
    """
    #  QHttpHeaders::QHttpHeaders(const QHttpHeaders &other)
    self._noteCreation(QHttpHeaders, lambda: Rituals.call(
        'ritual_ZN12QHttpHeadersC1ERKS_', self._valueOf(other),
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

  @overload(str, str)
  def append(self, name: str, value: str) -> bool:
    """
    Calls Qt's 'bool QHttpHeaders::append(QAnyStringView name, QAnyStringView
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#append

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHttpHeaders::append(QAnyStringView name, QAnyStringView value)
    return self.uglySide.call(
        'ritual_ZN12QHttpHeaders6appendE14QAnyStringViewS0_', name, value,
    )

  @overload(WellKnownHeader, str)
  def append(self, name: WellKnownHeader, value: str) -> bool:
    """
    Calls Qt's 'bool QHttpHeaders::append(WellKnownHeader name,
    QAnyStringView value)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#append

    Parameters
    ----------

    name : WellKnownHeader
      Passed on as its number.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHttpHeaders::append(WellKnownHeader name, QAnyStringView value)
    return self.uglySide.call(
        'ritual_ZN12QHttpHeaders6appendENS_15WellKnownHeaderE14QAnyStringVi'
        'ew',
        name.value, value,
    )

  @overload(int, str, str)
  def insert(self, i: int, name: str, value: str) -> bool:
    """
    Calls Qt's 'bool QHttpHeaders::insert(qsizetype i, QAnyStringView name,
    QAnyStringView value)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#insert

    Parameters
    ----------

    i : int
      Passed on as it is.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHttpHeaders::insert(qsizetype i, QAnyStringView name,
    #      QAnyStringView value)
    return self.uglySide.call(
        'ritual_ZN12QHttpHeaders6insertEx14QAnyStringViewS0_',
        i, name, value,
    )

  @overload(int, WellKnownHeader, str)
  def insert(self, i: int, name: WellKnownHeader, value: str) -> bool:
    """
    Calls Qt's 'bool QHttpHeaders::insert(qsizetype i, WellKnownHeader name,
    QAnyStringView value)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#insert

    Parameters
    ----------

    i : int
      Passed on as it is.

    name : WellKnownHeader
      Passed on as its number.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHttpHeaders::insert(qsizetype i, WellKnownHeader name,
    #      QAnyStringView value)
    return self.uglySide.call(
        'ritual_ZN12QHttpHeaders6insertExNS_15WellKnownHeaderE14QAnyStringV'
        'iew',
        i, name.value, value,
    )

  @overload(int, str, str)
  def replace(self, i: int, name: str, newValue: str) -> bool:
    """
    Calls Qt's 'bool QHttpHeaders::replace(qsizetype i, QAnyStringView name,
    QAnyStringView newValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#replace

    Parameters
    ----------

    i : int
      Passed on as it is.

    name : str
      Passed on as it is: a QString is made of it for the call.

    newValue : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHttpHeaders::replace(qsizetype i, QAnyStringView name,
    #      QAnyStringView newValue)
    return self.uglySide.call(
        'ritual_ZN12QHttpHeaders7replaceEx14QAnyStringViewS0_',
        i, name, newValue,
    )

  @overload(int, WellKnownHeader, str)
  def replace(self, i: int, name: WellKnownHeader, newValue: str) -> bool:
    """
    Calls Qt's 'bool QHttpHeaders::replace(qsizetype i, WellKnownHeader name,
    QAnyStringView newValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#replace

    Parameters
    ----------

    i : int
      Passed on as it is.

    name : WellKnownHeader
      Passed on as its number.

    newValue : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHttpHeaders::replace(qsizetype i, WellKnownHeader name,
    #      QAnyStringView newValue)
    return self.uglySide.call(
        'ritual_ZN12QHttpHeaders7replaceExNS_15WellKnownHeaderE14QAnyString'
        'View',
        i, name.value, newValue,
    )

  @overload(str, str)
  def replaceOrAppend(self, name: str, newValue: str) -> bool:
    """
    Calls Qt's 'bool QHttpHeaders::replaceOrAppend(QAnyStringView name,
    QAnyStringView newValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#replaceOrAppend

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    newValue : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHttpHeaders::replaceOrAppend(QAnyStringView name, QAnyStringView
    #      newValue)
    return self.uglySide.call(
        'ritual_ZN12QHttpHeaders15replaceOrAppendE14QAnyStringViewS0_',
        name, newValue,
    )

  @overload(WellKnownHeader, str)
  def replaceOrAppend(self, name: WellKnownHeader, newValue: str) -> bool:
    """
    Calls Qt's 'bool QHttpHeaders::replaceOrAppend(WellKnownHeader name,
    QAnyStringView newValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#replaceOrAppend

    Parameters
    ----------

    name : WellKnownHeader
      Passed on as its number.

    newValue : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHttpHeaders::replaceOrAppend(WellKnownHeader name,
    #      QAnyStringView newValue)
    return self.uglySide.call(
        'ritual_ZN12QHttpHeaders15replaceOrAppendENS_15WellKnownHeaderE14QA'
        'nyStringView',
        name.value, newValue,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QHttpHeaders::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#clear
    """
    #  void QHttpHeaders::clear()
    self.uglySide.call('ritual_ZN12QHttpHeaders5clearEv')

  @overload(str)
  def removeAll(self, name: str) -> None:
    """
    Calls Qt's 'void QHttpHeaders::removeAll(QAnyStringView name)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#removeAll

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttpHeaders::removeAll(QAnyStringView name)
    self.uglySide.call(
        'ritual_ZN12QHttpHeaders9removeAllE14QAnyStringView', name,
    )

  @overload(WellKnownHeader)
  def removeAll(self, name: WellKnownHeader) -> None:
    """
    Calls Qt's 'void QHttpHeaders::removeAll(WellKnownHeader name)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#removeAll

    Parameters
    ----------

    name : WellKnownHeader
      Passed on as its number.
    """
    #  void QHttpHeaders::removeAll(WellKnownHeader name)
    self.uglySide.call(
        'ritual_ZN12QHttpHeaders9removeAllENS_15WellKnownHeaderE',
        name.value,
    )

  @overload(int)
  def removeAt(self, i: int) -> None:
    """
    Calls Qt's 'void QHttpHeaders::removeAt(qsizetype i)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#removeAt

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QHttpHeaders::removeAt(qsizetype i)
    self.uglySide.call('ritual_ZN12QHttpHeaders8removeAtEx', i)

  @overload(int)
  def reserve(self, size: int) -> None:
    """
    Calls Qt's 'void QHttpHeaders::reserve(qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#reserve

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QHttpHeaders::reserve(qsizetype size)
    self.uglySide.call('ritual_ZN12QHttpHeaders7reserveEx', size)

  @overload()
  @overload(int)
  @overload(int, int)
  def verify(self, pos: int = 0, n: int = 1) -> None:
    """
    Calls Qt's 'void QHttpHeaders::verify(qsizetype pos, qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaders.html#verify

    Parameters
    ----------

    pos : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QHttpHeaders::verify(qsizetype pos, qsizetype n) const
    self.uglySide.call('ritual_ZNK12QHttpHeaders6verifyExx', pos, n)

  @staticmethod
  def dateTimeValue(*__, **_) -> Never:
    """
    - Qt's 'std::optional<QDateTime>
      QHttpHeaders::dateTimeValue(QAnyStringView name) const': gives a type
      Python has no way to take yet.
    - Qt's 'std::optional<QDateTime>
      QHttpHeaders::dateTimeValue(WellKnownHeader name) const': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.dateTimeValue' has no cute function yet. Qt's "
        "'std::optional<QDateTime> "
        "QHttpHeaders::dateTimeValue(QAnyStringView name) const': gives a "
        "type Python has no way to take yet. Qt's 'std::optional<QDateTime> "
        "QHttpHeaders::dateTimeValue(WellKnownHeader name) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def dateTimeValueAt(*__, **_) -> Never:
    """
    Qt's 'std::optional<QDateTime> QHttpHeaders::dateTimeValueAt(qsizetype i)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.dateTimeValueAt' has no cute function yet. Qt's "
        "'std::optional<QDateTime> QHttpHeaders::dateTimeValueAt(qsizetype "
        "i) const': gives a type Python has no way to take yet.")

  @staticmethod
  def dateTimeValues(*__, **_) -> Never:
    """
    - Qt's 'std::optional<QList<QDateTime>>
      QHttpHeaders::dateTimeValues(QAnyStringView name) const': gives a type
      Python has no way to take yet.
    - Qt's 'std::optional<QList<QDateTime>>
      QHttpHeaders::dateTimeValues(WellKnownHeader name) const': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.dateTimeValues' has no cute function yet. Qt's "
        "'std::optional<QList<QDateTime>> "
        "QHttpHeaders::dateTimeValues(QAnyStringView name) const': gives a "
        "type Python has no way to take yet. Qt's "
        "'std::optional<QList<QDateTime>> "
        "QHttpHeaders::dateTimeValues(WellKnownHeader name) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def fromListOfPairs(*__, **_) -> Never:
    """
    Qt's 'QHttpHeaders QHttpHeaders::fromListOfPairs(const
    QList<std::pair<QByteArray, QByteArray>> &headers)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.fromListOfPairs' has no cute function yet. Qt's "
        "'QHttpHeaders QHttpHeaders::fromListOfPairs(const "
        "QList<std::pair<QByteArray, QByteArray>> &headers)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def fromMultiHash(*__, **_) -> Never:
    """
    Qt's 'QHttpHeaders QHttpHeaders::fromMultiHash(const
    QMultiHash<QByteArray, QByteArray> &headers)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.fromMultiHash' has no cute function yet. Qt's "
        "'QHttpHeaders QHttpHeaders::fromMultiHash(const "
        "QMultiHash<QByteArray, QByteArray> &headers)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def fromMultiMap(*__, **_) -> Never:
    """
    Qt's 'QHttpHeaders QHttpHeaders::fromMultiMap(const QMultiMap<QByteArray,
    QByteArray> &headers)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.fromMultiMap' has no cute function yet. Qt's "
        "'QHttpHeaders QHttpHeaders::fromMultiMap(const "
        "QMultiMap<QByteArray, QByteArray> &headers)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def intValue(*__, **_) -> Never:
    """
    - Qt's 'std::optional<qint64> QHttpHeaders::intValue(QAnyStringView name)
      const': gives a type Python has no way to take yet.
    - Qt's 'std::optional<qint64> QHttpHeaders::intValue(WellKnownHeader
      name) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.intValue' has no cute function yet. Qt's "
        "'std::optional<qint64> QHttpHeaders::intValue(QAnyStringView name) "
        "const': gives a type Python has no way to take yet. Qt's "
        "'std::optional<qint64> QHttpHeaders::intValue(WellKnownHeader "
        "name) const': gives a type Python has no way to take yet.")

  @staticmethod
  def intValueAt(*__, **_) -> Never:
    """
    Qt's 'std::optional<qint64> QHttpHeaders::intValueAt(qsizetype i) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.intValueAt' has no cute function yet. Qt's "
        "'std::optional<qint64> QHttpHeaders::intValueAt(qsizetype i) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def intValues(*__, **_) -> Never:
    """
    - Qt's 'std::optional<QList<qint64>>
      QHttpHeaders::intValues(QAnyStringView name) const': gives a type
      Python has no way to take yet.
    - Qt's 'std::optional<QList<qint64>>
      QHttpHeaders::intValues(WellKnownHeader name) const': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.intValues' has no cute function yet. Qt's "
        "'std::optional<QList<qint64>> "
        "QHttpHeaders::intValues(QAnyStringView name) const': gives a type "
        "Python has no way to take yet. Qt's 'std::optional<QList<qint64>> "
        "QHttpHeaders::intValues(WellKnownHeader name) const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def rangeValues(*__, **_) -> Never:
    """
    Qt's 'std::optional<QHttpHeaderRangeSet> QHttpHeaders::rangeValues()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.rangeValues' has no cute function yet. Qt's "
        "'std::optional<QHttpHeaderRangeSet> QHttpHeaders::rangeValues() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHttpHeaders::swap(QHttpHeaders &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.swap' has no cute function yet. Qt's 'void "
        "QHttpHeaders::swap(QHttpHeaders &other)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def toListOfPairs(*__, **_) -> Never:
    """
    Qt's 'QList<std::pair<QByteArray, QByteArray>>
    QHttpHeaders::toListOfPairs() const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.toListOfPairs' has no cute function yet. Qt's "
        "'QList<std::pair<QByteArray, QByteArray>> "
        "QHttpHeaders::toListOfPairs() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def toMultiHash(*__, **_) -> Never:
    """
    Qt's 'QMultiHash<QByteArray, QByteArray> QHttpHeaders::toMultiHash()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.toMultiHash' has no cute function yet. Qt's "
        "'QMultiHash<QByteArray, QByteArray> QHttpHeaders::toMultiHash() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def toMultiMap(*__, **_) -> Never:
    """
    Qt's 'QMultiMap<QByteArray, QByteArray> QHttpHeaders::toMultiMap()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpHeaders.toMultiMap' has no cute function yet. Qt's "
        "'QMultiMap<QByteArray, QByteArray> QHttpHeaders::toMultiMap() "
        "const': gives a type Python has no way to take yet.")
