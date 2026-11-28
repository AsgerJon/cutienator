"""
QNetworkReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkreply.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QIODevice, QList, QObject
from . import QHttpHeaders, QNetworkAccessManager, QNetworkRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QByteArrayView, QMetaObject, QUrl
  from ..QtCore import QVariant
  from . import QNetworkReplyPrivate, QSslConfiguration, QSslError
  from . import QSslPreSharedKeyAuthenticator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkReply(QIODevice):
  """
  The cute side of Qt's QNetworkReply: a plain Python object standing in
  front of one C++ QNetworkReply.

  It is built on the cute 'QIODevice', as Qt's QNetworkReply is built on Qt's
  QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkReply that has a ritual and that Python can
  call so far, 49 names in all: 'metaObject', 'tr', 'close', 'isSequential',
  'readBufferSize', 'setReadBufferSize', 'manager', 'operation', 'request',
  'error', 'isFinished', 'isRunning', 'url', 'header', 'hasRawHeader',
  'rawHeaderList', 'rawHeader', 'headers', 'attribute', 'sslConfiguration',
  'setSslConfiguration', 'ignoreSslErrors', 'abort',
  'socketStartedConnecting', 'requestSent', 'metaDataChanged', 'finished',
  'errorOccurred', 'encrypted', 'sslErrors',
  'preSharedKeyAuthenticationRequired', 'redirected', 'redirectAllowed',
  'uploadProgress', 'downloadProgress', 'writeData', 'setOperation',
  'setRequest', 'setError', 'setFinished', 'setUrl', 'setHeader',
  'setRawHeader', 'setHeaders', 'setWellKnownHeader', 'setAttribute',
  'setSslConfigurationImplementation', 'ignoreSslErrorsImplementation',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkReply::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QNetworkReply::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkReply::~QNetworkReply()': the destructor: Python never
    removes a C++ QNetworkReply.
  - Qt's 'const QList<RawHeaderPair> &QNetworkReply::rawHeaderPairs() const':
    gives a type Python has no way to take yet.
  - Qt's 'QNetworkReply::QNetworkReply(QNetworkReplyPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'void QNetworkReply::setHeaders(QHttpHeaders &&newHeaders)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void
    QNetworkReply::sslConfigurationImplementation(QSslConfiguration &a0)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'const QNetworkReplyPrivate *QNetworkReply::d_func() const': takes
    in Python what 'QNetworkReplyPrivate *QNetworkReply::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 61 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QNetworkReply is created at the first use, not by
    'QNetworkReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkReply.
  - Qt tells when it has removed the C++ QNetworkReply. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNetworkReply that has no cute function yet,
    'rawHeaderPairs', 'sslConfigurationImplementation', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QNetworkReply, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class NetworkError(CuteNum):
    """
    The enum 'QNetworkReply::NetworkError' of Qt, with the 34 names Qt gives
    in it.
    """

    NoError = Kee[int](0)
    ConnectionRefusedError = Kee[int](1)
    RemoteHostClosedError = Kee[int](2)
    HostNotFoundError = Kee[int](3)
    TimeoutError = Kee[int](4)
    OperationCanceledError = Kee[int](5)
    SslHandshakeFailedError = Kee[int](6)
    TemporaryNetworkFailureError = Kee[int](7)
    NetworkSessionFailedError = Kee[int](8)
    BackgroundRequestNotAllowedError = Kee[int](9)
    TooManyRedirectsError = Kee[int](10)
    InsecureRedirectError = Kee[int](11)
    UnknownNetworkError = Kee[int](99)
    ProxyConnectionRefusedError = Kee[int](101)
    ProxyConnectionClosedError = Kee[int](102)
    ProxyNotFoundError = Kee[int](103)
    ProxyTimeoutError = Kee[int](104)
    ProxyAuthenticationRequiredError = Kee[int](105)
    UnknownProxyError = Kee[int](199)
    ContentAccessDenied = Kee[int](201)
    ContentOperationNotPermittedError = Kee[int](202)
    ContentNotFoundError = Kee[int](203)
    AuthenticationRequiredError = Kee[int](204)
    ContentReSendError = Kee[int](205)
    ContentConflictError = Kee[int](206)
    ContentGoneError = Kee[int](207)
    UnknownContentError = Kee[int](299)
    ProtocolUnknownError = Kee[int](301)
    ProtocolInvalidOperationError = Kee[int](302)
    ProtocolFailure = Kee[int](399)
    InternalServerError = Kee[int](401)
    OperationNotImplementedError = Kee[int](402)
    ServiceUnavailableError = Kee[int](403)
    UnknownServerError = Kee[int](499)

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
    Calls Qt's 'QString QNetworkReply::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#tr

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
    #  QString QNetworkReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QNetworkReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkReply'

  #  A C++ QNetworkReply Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkReply'

  #  The functions Qt calls itself that QNetworkReply is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'sslConfigurationImplementation': (
          'void '
          'QNetworkReply::sslConfigurationImplementation(QSslConfiguration '
          '&) const',
      ),
      'ignoreSslErrorsImplementation': (
          'void QNetworkReply::ignoreSslErrorsImplementation(const '
          'QList<QSslError> &)',
      ),
  }

  #  The functions Qt calls itself that QNetworkReply is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setReadBufferSize': (
          ('_ZN13QNetworkReply17setReadBufferSizeEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'abort': (
          ('_ZN13QNetworkReply5abortEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'ignoreSslErrors': (
          ('_ZN13QNetworkReply15ignoreSslErrorsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setSslConfigurationImplementation': (
          ('_ZN13QNetworkReply33setSslConfigurationImplementationERK17QSslC'
           'onfiguration',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtNetwork:QSslConfiguration'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNetworkReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkReply::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QNetworkReply10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QNetworkReply::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#isSequential
    """
    #  bool QNetworkReply::isSequential() const
    ritual = 'ritual_ZNK13QNetworkReply12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QNetworkReply12isSequentialEv'
    return self.uglySide.call(ritual)

  def readBufferSize(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkReply::readBufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#readBufferSize
    """
    #  qint64 QNetworkReply::readBufferSize() const
    return self.uglySide.call('ritual_ZNK13QNetworkReply14readBufferSizeEv')

  def manager(self) -> Optional[QNetworkAccessManager]:
    """
    Calls Qt's 'QNetworkAccessManager *QNetworkReply::manager() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#manager

    Returns
    -------

    Optional[QNetworkAccessManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkAccessManager *QNetworkReply::manager() const
    address = self.uglySide.call('ritual_ZNK13QNetworkReply7managerEv')
    return QNetworkAccessManager._cuteAt(address)

  def operation(self) -> QNetworkAccessManager.Operation:
    """
    Calls Qt's 'QNetworkAccessManager::Operation QNetworkReply::operation()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#operation

    Returns
    -------

    QNetworkAccessManager.Operation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QNetworkAccessManager.Operation(number)' gives.
    """
    #  QNetworkAccessManager::Operation QNetworkReply::operation() const
    return QNetworkAccessManager.Operation(self.uglySide.call(
        'ritual_ZNK13QNetworkReply9operationEv',
    ))

  def request(self) -> QNetworkRequest:
    """
    Calls Qt's 'QNetworkRequest QNetworkReply::request() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#request

    Returns
    -------

    QNetworkRequest
      A new cute QNetworkRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkRequest QNetworkReply::request() const
    address = self.uglySide.call('ritual_ZNK13QNetworkReply7requestEv')
    return QNetworkRequest._cuteOwning(address)

  def error(self) -> NetworkError:
    """
    Calls Qt's 'NetworkError QNetworkReply::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#error

    Returns
    -------

    NetworkError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'NetworkError(number)'
      gives.
    """
    #  NetworkError QNetworkReply::error() const
    return QNetworkReply.NetworkError(self.uglySide.call(
        'ritual_ZNK13QNetworkReply5errorEv',
    ))

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QNetworkReply::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#isFinished
    """
    #  bool QNetworkReply::isFinished() const
    return self.uglySide.call('ritual_ZNK13QNetworkReply10isFinishedEv')

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QNetworkReply::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#isRunning
    """
    #  bool QNetworkReply::isRunning() const
    return self.uglySide.call('ritual_ZNK13QNetworkReply9isRunningEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QNetworkReply::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QNetworkReply::url() const
    address = self.uglySide.call('ritual_ZNK13QNetworkReply3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QNetworkRequest.KnownHeaders)
  def header(self, header: QNetworkRequest.KnownHeaders) -> QVariant:
    """
    Calls Qt's 'QVariant QNetworkReply::header(QNetworkRequest::KnownHeaders
    header) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#header

    Parameters
    ----------

    header : QNetworkRequest.KnownHeaders
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QNetworkReply::header(QNetworkRequest::KnownHeaders header)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QNetworkReply6headerEN15QNetworkRequest12KnownHeadersE',
        header.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def hasRawHeader(self, headerName: str) -> bool:
    """
    Calls Qt's 'bool QNetworkReply::hasRawHeader(QAnyStringView headerName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#hasRawHeader

    Parameters
    ----------

    headerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QNetworkReply::hasRawHeader(QAnyStringView headerName) const
    return self.uglySide.call(
        'ritual_ZNK13QNetworkReply12hasRawHeaderE14QAnyStringView',
        headerName,
    )

  def rawHeaderList(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QNetworkReply::rawHeaderList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#rawHeaderList

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QNetworkReply::rawHeaderList() const
    address = self.uglySide.call(
        'ritual_ZNK13QNetworkReply13rawHeaderListEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(str)
  def rawHeader(self, headerName: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNetworkReply::rawHeader(QAnyStringView
    headerName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#rawHeader

    Parameters
    ----------

    headerName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNetworkReply::rawHeader(QAnyStringView headerName) const
    address = self.uglySide.call(
        'ritual_ZNK13QNetworkReply9rawHeaderE14QAnyStringView', headerName,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def headers(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QNetworkReply::headers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#headers

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QNetworkReply::headers() const
    address = self.uglySide.call('ritual_ZNK13QNetworkReply7headersEv')
    return QHttpHeaders._cuteOwning(address)

  @overload(QNetworkRequest.Attribute)
  def attribute(self, code: QNetworkRequest.Attribute) -> QVariant:
    """
    Calls Qt's 'QVariant QNetworkReply::attribute(QNetworkRequest::Attribute
    code) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#attribute

    Parameters
    ----------

    code : QNetworkRequest.Attribute
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QNetworkReply::attribute(QNetworkRequest::Attribute code)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QNetworkReply9attributeEN15QNetworkRequest9AttributeE',
        code.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QNetworkReply::sslConfiguration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreply.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QNetworkReply::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK13QNetworkReply16sslConfigurationEv',
    )
    from . import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setReadBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QNetworkReply::setReadBufferSize(qint64 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreply.html#setReadBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QNetworkReply::setReadBufferSize(qint64 size)
    ritual = 'ritual_ZN13QNetworkReply17setReadBufferSizeEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QNetworkReply17setReadBufferSizeEx'
    self.uglySide.call(ritual, size)

  @overload(QSslConfiguration)
  def setSslConfiguration(self, configuration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QNetworkReply::setSslConfiguration(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreply.html#setSslConfiguration

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QNetworkReply::setSslConfiguration(const QSslConfiguration
    #      &configuration)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply19setSslConfigurationERK17QSslConfiguratio'
        'n',
        self._valueOf(configuration),
    )

  @overload(QNetworkAccessManager.Operation)
  def setOperation(self, operation: QNetworkAccessManager.Operation) -> None:
    """
    Calls Qt's 'void
    QNetworkReply::setOperation(QNetworkAccessManager::Operation operation)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#setOperation

    Parameters
    ----------

    operation : QNetworkAccessManager.Operation
      Passed on as its number.
    """
    #  void QNetworkReply::setOperation(QNetworkAccessManager::Operation
    #      operation)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply12setOperationEN21QNetworkAccessManager9Op'
        'erationE',
        operation.value,
    )

  @overload(QNetworkRequest)
  def setRequest(self, request: QNetworkRequest) -> None:
    """
    Calls Qt's 'void QNetworkReply::setRequest(const QNetworkRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#setRequest

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.
    """
    #  void QNetworkReply::setRequest(const QNetworkRequest &request)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply10setRequestERK15QNetworkRequest',
        self._valueOf(request),
    )

  @overload(NetworkError, str)
  def setError(self, errorCode: NetworkError, errorString: str) -> None:
    """
    Calls Qt's 'void QNetworkReply::setError(NetworkError errorCode, const
    QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#setError

    Parameters
    ----------

    errorCode : NetworkError
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkReply::setError(NetworkError errorCode, const QString
    #      &errorString)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply8setErrorENS_12NetworkErrorERK7QString',
        errorCode.value, errorString,
    )

  @overload(bool)
  def setFinished(self, a0: bool) -> None:
    """
    Calls Qt's 'void QNetworkReply::setFinished(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#setFinished

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QNetworkReply::setFinished(bool a0)
    self.uglySide.call('ritual_ZN13QNetworkReply11setFinishedEb', a0)

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QNetworkReply::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QNetworkReply::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply6setUrlERK4QUrl', self._valueOf(url),
    )

  @overload(QNetworkRequest.KnownHeaders, QVariant)
  def setHeader(
      self,
      header: QNetworkRequest.KnownHeaders,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QNetworkReply::setHeader(QNetworkRequest::KnownHeaders
    header, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#setHeader

    Parameters
    ----------

    header : QNetworkRequest.KnownHeaders
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QNetworkReply::setHeader(QNetworkRequest::KnownHeaders header,
    #      const QVariant &value)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply9setHeaderEN15QNetworkRequest12KnownHeader'
        'sERK8QVariant',
        header.value, self._valueOf(value),
    )

  @overload(QByteArray, QByteArray)
  def setRawHeader(self, headerName: QByteArray, value: QByteArray) -> None:
    """
    Calls Qt's 'void QNetworkReply::setRawHeader(const QByteArray
    &headerName, const QByteArray &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#setRawHeader

    Parameters
    ----------

    headerName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNetworkReply::setRawHeader(const QByteArray &headerName, const
    #      QByteArray &value)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply12setRawHeaderERK10QByteArrayS2_',
        self._valueOf(headerName), self._valueOf(value),
    )

  @overload(QHttpHeaders)
  def setHeaders(self, newHeaders: QHttpHeaders) -> None:
    """
    Calls Qt's 'void QNetworkReply::setHeaders(const QHttpHeaders
    &newHeaders)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#setHeaders

    Parameters
    ----------

    newHeaders : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.
    """
    #  void QNetworkReply::setHeaders(const QHttpHeaders &newHeaders)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply10setHeadersERK12QHttpHeaders',
        self._valueOf(newHeaders),
    )

  @overload(QHttpHeaders.WellKnownHeader, QByteArrayView)
  def setWellKnownHeader(
      self,
      name: QHttpHeaders.WellKnownHeader,
      value: QByteArrayView,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkReply::setWellKnownHeader(QHttpHeaders::WellKnownHeader name,
    QByteArrayView value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreply.html#setWellKnownHeader

    Parameters
    ----------

    name : QHttpHeaders.WellKnownHeader
      Passed on as its number.

    value : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void QNetworkReply::setWellKnownHeader(QHttpHeaders::WellKnownHeader
    #      name, QByteArrayView value)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply18setWellKnownHeaderEN12QHttpHeaders15Well'
        'KnownHeaderE14QByteArrayView',
        name.value, self._valueOf(value),
    )

  @overload(QNetworkRequest.Attribute, QVariant)
  def setAttribute(
      self,
      code: QNetworkRequest.Attribute,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QNetworkReply::setAttribute(QNetworkRequest::Attribute
    code, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#setAttribute

    Parameters
    ----------

    code : QNetworkRequest.Attribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QNetworkReply::setAttribute(QNetworkRequest::Attribute code,
    #      const QVariant &value)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply12setAttributeEN15QNetworkRequest9Attribut'
        'eERK8QVariant',
        code.value, self._valueOf(value),
    )

  @overload(QSslConfiguration)
  def setSslConfigurationImplementation(self, a0: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QNetworkReply::setSslConfigurationImplementation(const
    QSslConfiguration &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreply.html

    Parameters
    ----------

    a0 : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QNetworkReply::setSslConfigurationImplementation(const
    #      QSslConfiguration &a0)
    ritual = (
        'ritual_ZN13QNetworkReply33setSslConfigurationImplementationERK17QS'
        'slConfiguration')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QNetworkReply33setSslConfigurationImplementationE'
          'RK17QSslConfiguration')
    self.uglySide.call(ritual, self._valueOf(a0))

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
    Notes what was given, for Qt's 'QNetworkReply::QNetworkReply(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#QNetworkReply

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QNetworkReply::QNetworkReply(QObject *parent)
    self._noteCreation(QNetworkReply, lambda: Rituals.call(
        'ritual_ZN13QNetworkReplyC1EP7QObject',
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

  def close(self) -> None:
    """
    Calls Qt's 'void QNetworkReply::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#close
    """
    #  void QNetworkReply::close()
    ritual = 'ritual_ZN13QNetworkReply5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QNetworkReply5closeEv'
    self.uglySide.call(ritual)

  @overload(QList[QSslError])
  def ignoreSslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QNetworkReply::ignoreSslErrors(const QList<QSslError>
    &errors)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#ignoreSslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNetworkReply::ignoreSslErrors(const QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply15ignoreSslErrorsERK5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  @overload()
  def ignoreSslErrors(self) -> None:
    """
    Calls Qt's 'void QNetworkReply::ignoreSslErrors()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#ignoreSslErrors
    """
    #  void QNetworkReply::ignoreSslErrors()
    ritual = 'ritual_ZN13QNetworkReply15ignoreSslErrorsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QNetworkReply15ignoreSslErrorsEv'
    self.uglySide.call(ritual)

  def abort(self) -> None:
    """
    Calls Qt's 'void QNetworkReply::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#abort
    """
    #  void QNetworkReply::abort()
    self.uglySide.call('ritual_ZN13QNetworkReply5abortEv')

  def socketStartedConnecting(self) -> None:
    """
    Calls Qt's 'void QNetworkReply::socketStartedConnecting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreply.html#socketStartedConnecting
    """
    #  void QNetworkReply::socketStartedConnecting()
    self.uglySide.call('ritual_ZN13QNetworkReply23socketStartedConnectingEv')

  def requestSent(self) -> None:
    """
    Calls Qt's 'void QNetworkReply::requestSent()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#requestSent
    """
    #  void QNetworkReply::requestSent()
    self.uglySide.call('ritual_ZN13QNetworkReply11requestSentEv')

  def metaDataChanged(self) -> None:
    """
    Calls Qt's 'void QNetworkReply::metaDataChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#metaDataChanged
    """
    #  void QNetworkReply::metaDataChanged()
    self.uglySide.call('ritual_ZN13QNetworkReply15metaDataChangedEv')

  def finished(self) -> None:
    """
    Calls Qt's 'void QNetworkReply::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#finished
    """
    #  void QNetworkReply::finished()
    self.uglySide.call('ritual_ZN13QNetworkReply8finishedEv')

  @overload(NetworkError)
  def errorOccurred(self, a0: NetworkError) -> None:
    """
    Calls Qt's 'void QNetworkReply::errorOccurred(QNetworkReply::NetworkError
    a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#errorOccurred

    Parameters
    ----------

    a0 : NetworkError
      Passed on as its number.
    """
    #  void QNetworkReply::errorOccurred(QNetworkReply::NetworkError a0)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply13errorOccurredENS_12NetworkErrorE',
        a0.value,
    )

  def encrypted(self) -> None:
    """
    Calls Qt's 'void QNetworkReply::encrypted()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#encrypted
    """
    #  void QNetworkReply::encrypted()
    self.uglySide.call('ritual_ZN13QNetworkReply9encryptedEv')

  @overload(QList[QSslError])
  def sslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QNetworkReply::sslErrors(const QList<QSslError>
    &errors)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#sslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNetworkReply::sslErrors(const QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply9sslErrorsERK5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  @overload(QSslPreSharedKeyAuthenticator)
  @overload(NoneType)
  def preSharedKeyAuthenticationRequired(
      self,
      authenticator: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QNetworkReply::preSharedKeyAuthenticationRequired(
    QSslPreSharedKeyAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreply.html

    Parameters
    ----------

    authenticator : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkReply::preSharedKeyAuthenticationRequired(
    #      QSslPreSharedKeyAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply34preSharedKeyAuthenticationRequiredEP29QS'
        'slPreSharedKeyAuthenticator',
        self._addressOf(authenticator),
    )

  @overload(QUrl)
  def redirected(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QNetworkReply::redirected(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#redirected

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QNetworkReply::redirected(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply10redirectedERK4QUrl', self._valueOf(url),
    )

  def redirectAllowed(self) -> None:
    """
    Calls Qt's 'void QNetworkReply::redirectAllowed()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#redirectAllowed
    """
    #  void QNetworkReply::redirectAllowed()
    self.uglySide.call('ritual_ZN13QNetworkReply15redirectAllowedEv')

  @overload(int, int)
  def uploadProgress(self, bytesSent: int, bytesTotal: int) -> None:
    """
    Calls Qt's 'void QNetworkReply::uploadProgress(qint64 bytesSent, qint64
    bytesTotal)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#uploadProgress

    Parameters
    ----------

    bytesSent : int
      Passed on as it is.

    bytesTotal : int
      Passed on as it is.
    """
    #  void QNetworkReply::uploadProgress(qint64 bytesSent, qint64
    #      bytesTotal)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply14uploadProgressExx', bytesSent, bytesTotal,
    )

  @overload(int, int)
  def downloadProgress(self, bytesReceived: int, bytesTotal: int) -> None:
    """
    Calls Qt's 'void QNetworkReply::downloadProgress(qint64 bytesReceived,
    qint64 bytesTotal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreply.html#downloadProgress

    Parameters
    ----------

    bytesReceived : int
      Passed on as it is.

    bytesTotal : int
      Passed on as it is.
    """
    #  void QNetworkReply::downloadProgress(qint64 bytesReceived, qint64
    #      bytesTotal)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply16downloadProgressExx',
        bytesReceived, bytesTotal,
    )

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QNetworkReply::writeData(const char *data, qint64
    len)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QNetworkReply::writeData(const char *data, qint64 len)
    return self.uglySide.call(
        'ritual_ZN13QNetworkReply9writeDataEPKcx', self._bytesOf(data), len,
    )

  @overload(QList[QSslError])
  def ignoreSslErrorsImplementation(self, a0: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QNetworkReply::ignoreSslErrorsImplementation(const
    QList<QSslError> &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreply.html#ignoreSslErrorsImplementation

    Parameters
    ----------

    a0 : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNetworkReply::ignoreSslErrorsImplementation(const
    #      QList<QSslError> &a0)
    self.uglySide.call(
        'ritual_ZN13QNetworkReply29ignoreSslErrorsImplementationERK5QListI9'
        'QSslErrorE',
        self._valueOf(a0),
    )

  def d_func(self) -> Optional[QNetworkReplyPrivate]:
    """
    Calls Qt's 'QNetworkReplyPrivate *QNetworkReply::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreply.html#d_func

    Returns
    -------

    Optional[QNetworkReplyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReplyPrivate *QNetworkReply::d_func()
    address = self.uglySide.call('ritual_ZN13QNetworkReply6d_funcEv')
    from . import QNetworkReplyPrivate
    return QNetworkReplyPrivate._cuteAt(address)

  @staticmethod
  def rawHeaderPairs(*__, **_) -> Never:
    """
    Qt's 'const QList<RawHeaderPair> &QNetworkReply::rawHeaderPairs() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkReply.rawHeaderPairs' has no cute function yet. Qt's "
        "'const QList<RawHeaderPair> &QNetworkReply::rawHeaderPairs() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def sslConfigurationImplementation(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkReply::sslConfigurationImplementation(QSslConfiguration &a0)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkReply.sslConfigurationImplementation' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReply::sslConfigurationImplementation(QSslConfiguration "
        "&a0) const': takes a type Python has no way to hand over yet.")
