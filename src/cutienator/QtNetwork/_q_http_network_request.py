"""
QHttpNetworkRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkrequest_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpNetworkRequest to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QHttpNetworkHeader, QNetworkRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QByteArrayView, QNonContiguousByteDevice
  from ..QtCore import QUrl
  from . import QHttpHeaders
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QNonContiguousByteDevice = WAIT['QNonContiguousByteDevice']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpNetworkRequest(QHttpNetworkHeader):
  """
  The cute side of Qt's QHttpNetworkRequest: a plain Python object standing
  in front of one C++ QHttpNetworkRequest.

  It is built on the cute 'QHttpNetworkHeader', as Qt's QHttpNetworkRequest
  is built on Qt's QHttpNetworkHeader, and has everything that class has.

  C++ hands a QHttpNetworkRequest around as a copy, so every C++
  QHttpNetworkRequest behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpNetworkRequest that has a ritual and that
  Python can call so far, 46 names in all: '__eq__', 'url', 'setUrl',
  'majorVersion', 'minorVersion', 'contentLength', 'setContentLength',
  'header', 'headerField', 'setHeaderField', 'prependHeaderField',
  'clearHeaders', 'operation', 'setOperation', 'customVerb', 'setCustomVerb',
  'priority', 'setPriority', 'isPipeliningAllowed', 'setPipeliningAllowed',
  'isHTTP2Allowed', 'setHTTP2Allowed', 'isHTTP2Direct', 'setHTTP2Direct',
  'isH2cAllowed', 'setH2cAllowed', 'withCredentials', 'setWithCredentials',
  'isSsl', 'setSsl', 'isPreConnect', 'setPreConnect', 'isFollowRedirects',
  'setRedirectPolicy', 'redirectPolicy', 'redirectCount', 'setRedirectCount',
  'setUploadByteDevice', 'uploadByteDevice', 'methodName', 'uri',
  'peerVerifyName', 'setPeerVerifyName', 'fullLocalServerName',
  'setFullLocalServerName', 'methodIsIdempotent'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpNetworkRequest::~QHttpNetworkRequest()': the destructor:
    Python removes its C++ QHttpNetworkRequest by it, and has no other use
    for it.
  - Qt's 'QHttpNetworkRequest &QHttpNetworkRequest::operator=(const
    QHttpNetworkRequest &other)': assignment: Python binds a name and has no
    operator for it.

  What to expect
  --------------

  - The C++ QHttpNetworkRequest is created at the first use, not by
    'QHttpNetworkRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpNetworkRequest back gives a copy the ritual made
    for Python, in a new cute QHttpNetworkRequest.
  """

  #  The enums Qt writes inside QHttpNetworkRequest, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Operation(CuteNum):
    """
    The enum 'QHttpNetworkRequest::Operation' of Qt, with the 9 names Qt
    gives in it.
    """

    Options = Kee[int](0)
    Get = Kee[int](1)
    Head = Kee[int](2)
    Post = Kee[int](3)
    Put = Kee[int](4)
    Delete = Kee[int](5)
    Trace = Kee[int](6)
    Connect = Kee[int](7)
    Custom = Kee[int](8)

  class Priority(CuteNum):
    """
    The enum 'QHttpNetworkRequest::Priority' of Qt, with the 3 names Qt gives
    in it.
    """

    HighPriority = Kee[int](0)
    NormalPriority = Kee[int](1)
    LowPriority = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpNetworkRequest'

  #  A C++ QHttpNetworkRequest Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttpNetworkRequest'

  #  Qt's '~QHttpNetworkRequest()'. Naming it makes this a value class:
  #  Python owns every C++ QHttpNetworkRequest behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QHttpNetworkRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QHttpNetworkRequest::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkrequest.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QHttpNetworkRequest::url() const
    ritual = 'ritual_ZNK19QHttpNetworkRequest3urlEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QHttpNetworkRequest3urlEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def majorVersion(self) -> int:
    """
    Calls Qt's 'int QHttpNetworkRequest::majorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#majorVersion
    """
    #  int QHttpNetworkRequest::majorVersion() const
    ritual = 'ritual_ZNK19QHttpNetworkRequest12majorVersionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QHttpNetworkRequest12majorVersionEv'
    return self.uglySide.call(ritual)

  def minorVersion(self) -> int:
    """
    Calls Qt's 'int QHttpNetworkRequest::minorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#minorVersion
    """
    #  int QHttpNetworkRequest::minorVersion() const
    ritual = 'ritual_ZNK19QHttpNetworkRequest12minorVersionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QHttpNetworkRequest12minorVersionEv'
    return self.uglySide.call(ritual)

  def contentLength(self) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkRequest::contentLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#contentLength
    """
    #  qint64 QHttpNetworkRequest::contentLength() const
    ritual = 'ritual_ZNK19QHttpNetworkRequest13contentLengthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QHttpNetworkRequest13contentLengthEv'
    return self.uglySide.call(ritual)

  def header(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QHttpNetworkRequest::header() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkrequest.html#header

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QHttpNetworkRequest::header() const
    ritual = 'ritual_ZNK19QHttpNetworkRequest6headerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QHttpNetworkRequest6headerEv'
    address = self.uglySide.call(ritual)
    from . import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  @overload(QByteArrayView)
  @overload(QByteArrayView, QByteArray)
  def headerField(
      self,
      name: QByteArrayView,
      defaultValue: Optional[QByteArray] = None,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpNetworkRequest::headerField(QByteArrayView
    name, const QByteArray &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#headerField

    Parameters
    ----------

    name : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    defaultValue : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpNetworkRequest::headerField(QByteArrayView name, const
    #      QByteArray &defaultValue) const
    if defaultValue is None:
      from ..QtCore import QByteArray
      defaultValue = QByteArray()
    ritual = (
        'ritual_ZNK19QHttpNetworkRequest11headerFieldE14QByteArrayViewRK10Q'
        'ByteArray')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QHttpNetworkRequest11headerFieldE14QByteArrayVie'
          'wRK10QByteArray')
    address = self.uglySide.call(
        ritual, self._valueOf(name), self._valueOf(defaultValue),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def operation(self) -> Operation:
    """
    Calls Qt's 'Operation QHttpNetworkRequest::operation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkrequest.html#operation

    Returns
    -------

    Operation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Operation(number)' gives.
    """
    #  Operation QHttpNetworkRequest::operation() const
    return QHttpNetworkRequest.Operation(self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest9operationEv',
    ))

  def customVerb(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpNetworkRequest::customVerb() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#customVerb

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpNetworkRequest::customVerb() const
    address = self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest10customVerbEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def priority(self) -> Priority:
    """
    Calls Qt's 'Priority QHttpNetworkRequest::priority() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkrequest.html#priority

    Returns
    -------

    Priority
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Priority(number)' gives.
    """
    #  Priority QHttpNetworkRequest::priority() const
    return QHttpNetworkRequest.Priority(self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest8priorityEv',
    ))

  def isPipeliningAllowed(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkRequest::isPipeliningAllowed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#isPipeliningAllowed
    """
    #  bool QHttpNetworkRequest::isPipeliningAllowed() const
    return self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest19isPipeliningAllowedEv',
    )

  def isHTTP2Allowed(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkRequest::isHTTP2Allowed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#isHTTP2Allowed
    """
    #  bool QHttpNetworkRequest::isHTTP2Allowed() const
    return self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest14isHTTP2AllowedEv',
    )

  def isHTTP2Direct(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkRequest::isHTTP2Direct() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#isHTTP2Direct
    """
    #  bool QHttpNetworkRequest::isHTTP2Direct() const
    return self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest13isHTTP2DirectEv',
    )

  def isH2cAllowed(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkRequest::isH2cAllowed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#isH2cAllowed
    """
    #  bool QHttpNetworkRequest::isH2cAllowed() const
    return self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest12isH2cAllowedEv',
    )

  def withCredentials(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkRequest::withCredentials() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#withCredentials
    """
    #  bool QHttpNetworkRequest::withCredentials() const
    return self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest15withCredentialsEv',
    )

  def isSsl(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkRequest::isSsl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkrequest.html#isSsl
    """
    #  bool QHttpNetworkRequest::isSsl() const
    return self.uglySide.call('ritual_ZNK19QHttpNetworkRequest5isSslEv')

  def isPreConnect(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkRequest::isPreConnect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#isPreConnect
    """
    #  bool QHttpNetworkRequest::isPreConnect() const
    return self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest12isPreConnectEv',
    )

  def isFollowRedirects(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkRequest::isFollowRedirects() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#isFollowRedirects
    """
    #  bool QHttpNetworkRequest::isFollowRedirects() const
    return self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest17isFollowRedirectsEv',
    )

  def redirectPolicy(self) -> QNetworkRequest.RedirectPolicy:
    """
    Calls Qt's 'QNetworkRequest::RedirectPolicy
    QHttpNetworkRequest::redirectPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#redirectPolicy

    Returns
    -------

    QNetworkRequest.RedirectPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QNetworkRequest.RedirectPolicy(number)' gives.
    """
    #  QNetworkRequest::RedirectPolicy QHttpNetworkRequest::redirectPolicy()
    #      const
    return QNetworkRequest.RedirectPolicy(self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest14redirectPolicyEv',
    ))

  def redirectCount(self) -> int:
    """
    Calls Qt's 'int QHttpNetworkRequest::redirectCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#redirectCount
    """
    #  int QHttpNetworkRequest::redirectCount() const
    return self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest13redirectCountEv',
    )

  def uploadByteDevice(self) -> Optional[QNonContiguousByteDevice]:
    """
    Calls Qt's 'QNonContiguousByteDevice
    *QHttpNetworkRequest::uploadByteDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#uploadByteDevice

    Returns
    -------

    Optional[QNonContiguousByteDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNonContiguousByteDevice *QHttpNetworkRequest::uploadByteDevice()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest16uploadByteDeviceEv',
    )
    from ..QtCore import QNonContiguousByteDevice
    return QNonContiguousByteDevice._cuteAt(address)

  def methodName(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpNetworkRequest::methodName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#methodName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpNetworkRequest::methodName() const
    address = self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest10methodNameEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(bool)
  def uri(self, throughProxy: bool) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpNetworkRequest::uri(bool throughProxy)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkrequest.html#uri

    Parameters
    ----------

    throughProxy : bool
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpNetworkRequest::uri(bool throughProxy) const
    address = self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest3uriEb', throughProxy,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def peerVerifyName(self) -> str:
    """
    Calls Qt's 'QString QHttpNetworkRequest::peerVerifyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#peerVerifyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHttpNetworkRequest::peerVerifyName() const
    return self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest14peerVerifyNameEv',
    )

  def fullLocalServerName(self) -> str:
    """
    Calls Qt's 'QString QHttpNetworkRequest::fullLocalServerName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#fullLocalServerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHttpNetworkRequest::fullLocalServerName() const
    return self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest19fullLocalServerNameEv',
    )

  def methodIsIdempotent(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkRequest::methodIsIdempotent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#methodIsIdempotent
    """
    #  bool QHttpNetworkRequest::methodIsIdempotent() const
    return self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequest18methodIsIdempotentEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QHttpNetworkRequest::setUrl(const QUrl &url)
    ritual = 'ritual_ZN19QHttpNetworkRequest6setUrlERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QHttpNetworkRequest6setUrlERK4QUrl'
    self.uglySide.call(ritual, self._valueOf(url))

  @overload(int)
  def setContentLength(self, length: int) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setContentLength(qint64 length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setContentLength

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  void QHttpNetworkRequest::setContentLength(qint64 length)
    ritual = 'ritual_ZN19QHttpNetworkRequest16setContentLengthEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QHttpNetworkRequest16setContentLengthEx'
    self.uglySide.call(ritual, length)

  @overload(QByteArray, QByteArray)
  def setHeaderField(self, name: QByteArray, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setHeaderField(const QByteArray
    &name, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setHeaderField

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpNetworkRequest::setHeaderField(const QByteArray &name, const
    #      QByteArray &data)
    ritual = (
        'ritual_ZN19QHttpNetworkRequest14setHeaderFieldERK10QByteArrayS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QHttpNetworkRequest14setHeaderFieldERK10QByteArra'
          'yS2_')
    self.uglySide.call(ritual, self._valueOf(name), self._valueOf(data))

  @overload(Operation)
  def setOperation(self, operation: Operation) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setOperation(Operation operation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setOperation

    Parameters
    ----------

    operation : Operation
      Passed on as its number.
    """
    #  void QHttpNetworkRequest::setOperation(Operation operation)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest12setOperationENS_9OperationE',
        operation.value,
    )

  @overload(QByteArray)
  def setCustomVerb(self, customOperation: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setCustomVerb(const QByteArray
    &customOperation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setCustomVerb

    Parameters
    ----------

    customOperation : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpNetworkRequest::setCustomVerb(const QByteArray
    #      &customOperation)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest13setCustomVerbERK10QByteArray',
        self._valueOf(customOperation),
    )

  @overload(Priority)
  def setPriority(self, priority: Priority) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setPriority(Priority priority)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setPriority

    Parameters
    ----------

    priority : Priority
      Passed on as its number.
    """
    #  void QHttpNetworkRequest::setPriority(Priority priority)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest11setPriorityENS_8PriorityE',
        priority.value,
    )

  @overload(bool)
  def setPipeliningAllowed(self, b: bool) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setPipeliningAllowed(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setPipeliningAllowed

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QHttpNetworkRequest::setPipeliningAllowed(bool b)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest20setPipeliningAllowedEb', b,
    )

  @overload(bool)
  def setHTTP2Allowed(self, b: bool) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setHTTP2Allowed(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setHTTP2Allowed

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QHttpNetworkRequest::setHTTP2Allowed(bool b)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest15setHTTP2AllowedEb', b,
    )

  @overload(bool)
  def setHTTP2Direct(self, b: bool) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setHTTP2Direct(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setHTTP2Direct

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QHttpNetworkRequest::setHTTP2Direct(bool b)
    self.uglySide.call('ritual_ZN19QHttpNetworkRequest14setHTTP2DirectEb', b)

  @overload(bool)
  def setH2cAllowed(self, b: bool) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setH2cAllowed(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setH2cAllowed

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QHttpNetworkRequest::setH2cAllowed(bool b)
    self.uglySide.call('ritual_ZN19QHttpNetworkRequest13setH2cAllowedEb', b)

  @overload(bool)
  def setWithCredentials(self, b: bool) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setWithCredentials(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setWithCredentials

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QHttpNetworkRequest::setWithCredentials(bool b)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest18setWithCredentialsEb', b,
    )

  @overload(bool)
  def setSsl(self, a0: bool) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setSsl(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setSsl

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QHttpNetworkRequest::setSsl(bool a0)
    self.uglySide.call('ritual_ZN19QHttpNetworkRequest6setSslEb', a0)

  @overload(bool)
  def setPreConnect(self, preConnect: bool) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setPreConnect(bool preConnect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setPreConnect

    Parameters
    ----------

    preConnect : bool
      Passed on as it is.
    """
    #  void QHttpNetworkRequest::setPreConnect(bool preConnect)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest13setPreConnectEb', preConnect,
    )

  @overload(QNetworkRequest.RedirectPolicy)
  def setRedirectPolicy(
      self,
      policy: QNetworkRequest.RedirectPolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkRequest::setRedirectPolicy(QNetworkRequest::RedirectPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setRedirectPolicy

    Parameters
    ----------

    policy : QNetworkRequest.RedirectPolicy
      Passed on as its number.
    """
    #  void QHttpNetworkRequest::setRedirectPolicy(QNetworkRequest::
    #      RedirectPolicy policy)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest17setRedirectPolicyEN15QNetworkReque'
        'st14RedirectPolicyE',
        policy.value,
    )

  @overload(int)
  def setRedirectCount(self, count: int) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setRedirectCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setRedirectCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QHttpNetworkRequest::setRedirectCount(int count)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest16setRedirectCountEi', count,
    )

  @overload(QNonContiguousByteDevice)
  @overload(NoneType)
  def setUploadByteDevice(
      self,
      bd: Optional[QNonContiguousByteDevice],
  ) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkRequest::setUploadByteDevice(QNonContiguousByteDevice *bd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setUploadByteDevice

    Parameters
    ----------

    bd : Optional[QNonContiguousByteDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpNetworkRequest::setUploadByteDevice(QNonContiguousByteDevice
    #      *bd)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest19setUploadByteDeviceEP24QNonContigu'
        'ousByteDevice',
        self._addressOf(bd),
    )

  @overload(str)
  def setPeerVerifyName(self, peerName: str) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setPeerVerifyName(const QString
    &peerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setPeerVerifyName

    Parameters
    ----------

    peerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttpNetworkRequest::setPeerVerifyName(const QString &peerName)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest17setPeerVerifyNameERK7QString',
        peerName,
    )

  @overload(str)
  def setFullLocalServerName(self, fullServerName: str) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::setFullLocalServerName(const
    QString &fullServerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#setFullLocalServerName

    Parameters
    ----------

    fullServerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttpNetworkRequest::setFullLocalServerName(const QString
    #      &fullServerName)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest22setFullLocalServerNameERK7QString',
        fullServerName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QHttpNetworkRequest) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkRequest::operator==(const
    QHttpNetworkRequest &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#operator==

    Parameters
    ----------

    other : QHttpNetworkRequest
      Passed on as a value: Qt reads the C++ QHttpNetworkRequest, which stays
      Python's own.
    """
    #  bool QHttpNetworkRequest::operator==(const QHttpNetworkRequest &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QHttpNetworkRequesteqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
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
  @overload(QUrl)
  @overload(QUrl, Operation)
  @overload(QUrl, Operation, Priority)
  def __init__(
      self,
      url: Optional[QUrl] = None,
      operation: Operation = Operation.Get,
      priority: Priority = Priority.NormalPriority,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpNetworkRequest::QHttpNetworkRequest(const QUrl &url, Operation
    operation, Priority priority)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#QHttpNetworkRequest

    Parameters
    ----------

    url : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.

    operation : Operation
      Passed on as its number. May be left out, as in Qt: it is then
      Operation.Get.

    priority : Priority
      Passed on as its number. May be left out, as in Qt: it is then
      Priority.NormalPriority.
    """
    #  QHttpNetworkRequest::QHttpNetworkRequest(const QUrl &url, Operation
    #      operation, Priority priority)
    if url is None:
      from ..QtCore import QUrl
      url = QUrl()
    self._noteCreation(QHttpNetworkRequest, lambda: Rituals.call(
        'ritual_ZN19QHttpNetworkRequestC1ERK4QUrlNS_9OperationENS_8Priority'
        'E',
        self._valueOf(url), operation.value, priority.value,
    ))

  @overload(THIS)
  def __init__(self, other: QHttpNetworkRequest) -> None:
    """
    Notes what was given, for Qt's
    'QHttpNetworkRequest::QHttpNetworkRequest(const QHttpNetworkRequest
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#QHttpNetworkRequest

    Parameters
    ----------

    other : QHttpNetworkRequest
      Passed on as a value: Qt reads the C++ QHttpNetworkRequest, which stays
      Python's own.
    """
    #  QHttpNetworkRequest::QHttpNetworkRequest(const QHttpNetworkRequest
    #      &other)
    self._noteCreation(QHttpNetworkRequest, lambda: Rituals.call(
        'ritual_ZN19QHttpNetworkRequestC1ERKS_', self._valueOf(other),
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

  @overload(QByteArray, QByteArray)
  def prependHeaderField(self, name: QByteArray, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::prependHeaderField(const QByteArray
    &name, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#prependHeaderField

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpNetworkRequest::prependHeaderField(const QByteArray &name,
    #      const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN19QHttpNetworkRequest18prependHeaderFieldERK10QByteArrayS'
        '2_',
        self._valueOf(name), self._valueOf(data),
    )

  def clearHeaders(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkRequest::clearHeaders()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequest.html#clearHeaders
    """
    #  void QHttpNetworkRequest::clearHeaders()
    self.uglySide.call('ritual_ZN19QHttpNetworkRequest12clearHeadersEv')
