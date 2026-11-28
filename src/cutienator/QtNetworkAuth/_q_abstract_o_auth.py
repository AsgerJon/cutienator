"""
QAbstractOAuth binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/qabstractoauth.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl, QVariant
  from ..QtNetwork import QNetworkAccessManager, QNetworkReply
  from ..QtNetwork import QNetworkRequest
  from . import QAbstractOAuthPrivate, QAbstractOAuthReplyHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractOAuthReplyHandler = WAIT['QAbstractOAuthReplyHandler']
  QByteArray = WAIT['QByteArray']
  QNetworkAccessManager = WAIT['QNetworkAccessManager']
  QNetworkReply = WAIT['QNetworkReply']
  QNetworkRequest = WAIT['QNetworkRequest']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractOAuth(QObject):
  """
  The cute side of Qt's QAbstractOAuth: a plain Python object standing in
  front of one C++ QAbstractOAuth.

  It is built on the cute 'QObject', as Qt's QAbstractOAuth is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractOAuth that has a ritual and that Python can
  call so far, 37 names in all: 'metaObject', 'tr', 'clientIdentifier',
  'setClientIdentifier', 'token', 'setToken', 'networkAccessManager',
  'setNetworkAccessManager', 'status', 'authorizationUrl',
  'setAuthorizationUrl', 'extraTokens', 'replyHandler', 'setReplyHandler',
  'head', 'get', 'post', 'put', 'deleteResource', 'prepareRequest',
  'contentType', 'setContentType', 'grant', 'clientIdentifierChanged',
  'tokenChanged', 'statusChanged', 'authorizationUrlChanged',
  'extraTokensChanged', 'contentTypeChanged', 'authorizeWithBrowser',
  'granted', 'finished', 'replyDataReceived', 'setStatus', 'callback',
  'generateRandomString', 'd_func'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractOAuth::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAbstractOAuth::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractOAuth::~QAbstractOAuth()': the destructor: Python never
    removes a C++ QAbstractOAuth.
  - Qt's 'ModifyParametersFunction QAbstractOAuth::modifyParametersFunction()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QAbstractOAuth::setModifyParametersFunction(const
    ModifyParametersFunction &modifyParametersFunction)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QAbstractOAuth::requestFailed(const Error error)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QAbstractOAuth::resourceOwnerAuthorization(const QUrl &url,
    const QMultiMap<QString, QVariant> &parameters)': takes a type Python has
    no way to hand over yet.
  - Qt's 'const QAbstractOAuthPrivate *QAbstractOAuth::d_func() const': takes
    in Python what 'QAbstractOAuthPrivate *QAbstractOAuth::d_func()' takes.

  What has no ritual
  ------------------

  5 of the 50 functions Qt declares: 2 not a gap; 2 forbidden; 1 the class is
  abstract, so C++ cannot make one, and the C++ class of ours does not fill
  in every function it leaves open.

  What to expect
  --------------

  - The C++ QAbstractOAuth is created at the first use, not by
    'QAbstractOAuth(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractOAuth.
  - Qt tells when it has removed the C++ QAbstractOAuth. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractOAuth that has no cute function yet,
    '__init__', 'modifyParametersFunction', 'requestFailed',
    'resourceOwnerAuthorization', 'setModifyParametersFunction', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QAbstractOAuth, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ContentType(CuteNum, scoped=True):
    """
    The enum 'QAbstractOAuth::ContentType' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    WwwFormUrlEncoded = Kee[int](0)
    Json = Kee[int](1)

  class Error(CuteNum, scoped=True):
    """
    The enum 'QAbstractOAuth::Error' of Qt, with the 8 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NoError = Kee[int](0)
    NetworkError = Kee[int](1)
    ServerError = Kee[int](2)
    OAuthTokenNotFoundError = Kee[int](3)
    OAuthTokenSecretNotFoundError = Kee[int](4)
    OAuthCallbackNotVerified = Kee[int](5)
    ClientError = Kee[int](6)
    ExpiredError = Kee[int](7)

  class Stage(CuteNum, scoped=True):
    """
    The enum 'QAbstractOAuth::Stage' of Qt, with the 4 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    RequestingTemporaryCredentials = Kee[int](0)
    RequestingAuthorization = Kee[int](1)
    RequestingAccessToken = Kee[int](2)
    RefreshingAccessToken = Kee[int](3)

  class Status(CuteNum, scoped=True):
    """
    The enum 'QAbstractOAuth::Status' of Qt, with the 4 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NotAuthenticated = Kee[int](0)
    TemporaryCredentialsReceived = Kee[int](1)
    Granted = Kee[int](2)
    RefreshingToken = Kee[int](3)

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
    Calls Qt's 'QString QAbstractOAuth::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#tr

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
    #  QString QAbstractOAuth::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QAbstractOAuth2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(int)
  def generateRandomString(length: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QAbstractOAuth::generateRandomString(quint8
    length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#generateRandomString

    Parameters
    ----------

    length : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QAbstractOAuth::generateRandomString(quint8 length)
    address = Rituals.call(
        'ritual_ZN14QAbstractOAuth20generateRandomStringEh', length,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractOAuth'

  #  A C++ QAbstractOAuth Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractOAuth'

  #  The functions Qt calls itself that QAbstractOAuth is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'head': (
          'QNetworkReply *QAbstractOAuth::head(const QUrl &, const '
          'QVariantMap &)',
      ),
      'get': (
          'QNetworkReply *QAbstractOAuth::get(const QUrl &, const '
          'QVariantMap &)',
      ),
      'post': (
          'QNetworkReply *QAbstractOAuth::post(const QUrl &, const '
          'QVariantMap &)',
      ),
      'put': (
          'QNetworkReply *QAbstractOAuth::put(const QUrl &, const '
          'QVariantMap &)',
      ),
      'deleteResource': (
          'QNetworkReply *QAbstractOAuth::deleteResource(const QUrl &, '
          'const QVariantMap &)',
      ),
      'resourceOwnerAuthorization': (
          'void QAbstractOAuth::resourceOwnerAuthorization(const QUrl &, '
          'const QMultiMap<QString, QVariant> &)',
      ),
  }

  #  The functions Qt calls itself that QAbstractOAuth is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'prepareRequest': (
          ('_ZN14QAbstractOAuth14prepareRequestEP15QNetworkRequestRK10QByte'
           'ArrayS4_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtNetwork:QNetworkRequest'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'grant': (
          ('_ZN14QAbstractOAuth5grantEv',
           ('nothing', 'nothing', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractOAuth::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractOAuth::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QAbstractOAuth10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def clientIdentifier(self) -> str:
    """
    Calls Qt's 'QString QAbstractOAuth::clientIdentifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#clientIdentifier

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth::clientIdentifier() const
    return self.uglySide.call(
        'ritual_ZNK14QAbstractOAuth16clientIdentifierEv',
    )

  def token(self) -> str:
    """
    Calls Qt's 'QString QAbstractOAuth::token() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#token

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth::token() const
    return self.uglySide.call('ritual_ZNK14QAbstractOAuth5tokenEv')

  def networkAccessManager(self) -> Optional[QNetworkAccessManager]:
    """
    Calls Qt's 'QNetworkAccessManager *QAbstractOAuth::networkAccessManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#networkAccessManager

    Returns
    -------

    Optional[QNetworkAccessManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkAccessManager *QAbstractOAuth::networkAccessManager() const
    address = self.uglySide.call(
        'ritual_ZNK14QAbstractOAuth20networkAccessManagerEv',
    )
    from ..QtNetwork import QNetworkAccessManager
    return QNetworkAccessManager._cuteAt(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QAbstractOAuth::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QAbstractOAuth::status() const
    return QAbstractOAuth.Status(self.uglySide.call(
        'ritual_ZNK14QAbstractOAuth6statusEv',
    ))

  def authorizationUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QAbstractOAuth::authorizationUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#authorizationUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QAbstractOAuth::authorizationUrl() const
    address = self.uglySide.call(
        'ritual_ZNK14QAbstractOAuth16authorizationUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def extraTokens(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QAbstractOAuth::extraTokens() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#extraTokens

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QAbstractOAuth::extraTokens() const
    address = self.uglySide.call('ritual_ZNK14QAbstractOAuth11extraTokensEv')
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def replyHandler(self) -> Optional[QAbstractOAuthReplyHandler]:
    """
    Calls Qt's 'QAbstractOAuthReplyHandler *QAbstractOAuth::replyHandler()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#replyHandler

    Returns
    -------

    Optional[QAbstractOAuthReplyHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractOAuthReplyHandler *QAbstractOAuth::replyHandler() const
    address = self.uglySide.call(
        'ritual_ZNK14QAbstractOAuth12replyHandlerEv',
    )
    from . import QAbstractOAuthReplyHandler
    return QAbstractOAuthReplyHandler._cuteAt(address)

  def contentType(self) -> ContentType:
    """
    Calls Qt's 'ContentType QAbstractOAuth::contentType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#contentType

    Returns
    -------

    ContentType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ContentType(number)'
      gives.
    """
    #  ContentType QAbstractOAuth::contentType() const
    return QAbstractOAuth.ContentType(self.uglySide.call(
        'ritual_ZNK14QAbstractOAuth11contentTypeEv',
    ))

  def callback(self) -> str:
    """
    Calls Qt's 'QString QAbstractOAuth::callback() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#callback

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth::callback() const
    return self.uglySide.call('ritual_ZNK14QAbstractOAuth8callbackEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setClientIdentifier(self, clientIdentifier: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::setClientIdentifier(const QString
    &clientIdentifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#setClientIdentifier

    Parameters
    ----------

    clientIdentifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth::setClientIdentifier(const QString
    #      &clientIdentifier)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth19setClientIdentifierERK7QString',
        clientIdentifier,
    )

  @overload(str)
  def setToken(self, token: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::setToken(const QString &token)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#setToken

    Parameters
    ----------

    token : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth::setToken(const QString &token)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth8setTokenERK7QString', token,
    )

  @overload(QNetworkAccessManager)
  @overload(NoneType)
  def setNetworkAccessManager(
      self,
      networkAccessManager: Optional[QNetworkAccessManager],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractOAuth::setNetworkAccessManager(QNetworkAccessManager
    *networkAccessManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#setNetworkAccessManager

    Parameters
    ----------

    networkAccessManager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractOAuth::setNetworkAccessManager(QNetworkAccessManager
    #      *networkAccessManager)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth23setNetworkAccessManagerEP21QNetworkAcce'
        'ssManager',
        self._addressOf(networkAccessManager),
    )

  @overload(QUrl)
  def setAuthorizationUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::setAuthorizationUrl(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#setAuthorizationUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QAbstractOAuth::setAuthorizationUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth19setAuthorizationUrlERK4QUrl',
        self._valueOf(url),
    )

  @overload(QAbstractOAuthReplyHandler)
  @overload(NoneType)
  def setReplyHandler(
      self,
      handler: Optional[QAbstractOAuthReplyHandler],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractOAuth::setReplyHandler(QAbstractOAuthReplyHandler *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#setReplyHandler

    Parameters
    ----------

    handler : Optional[QAbstractOAuthReplyHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractOAuth::setReplyHandler(QAbstractOAuthReplyHandler
    #      *handler)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth15setReplyHandlerEP26QAbstractOAuthReplyH'
        'andler',
        self._addressOf(handler),
    )

  @overload(ContentType)
  def setContentType(self, contentType: ContentType) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::setContentType(ContentType
    contentType)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#setContentType

    Parameters
    ----------

    contentType : ContentType
      Passed on as its number.
    """
    #  void QAbstractOAuth::setContentType(ContentType contentType)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth14setContentTypeENS_11ContentTypeE',
        contentType.value,
    )

  @overload(Status)
  def setStatus(self, status: Status) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::setStatus(Status status)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#setStatus

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void QAbstractOAuth::setStatus(Status status)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth9setStatusENS_6StatusE', status.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAbstractOAuth::QAbstractOAuth(QAbstractOAuthPrivate &a0, QObject
    *parent)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QAbstractOAuth.__init__' has no cute function yet. Qt's "
        "'QAbstractOAuth::QAbstractOAuth(QAbstractOAuthPrivate &a0, QObject "
        "*parent)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  @overload(QUrl, QMap[str, QVariant])
  def head(
      self,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QAbstractOAuth::head(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#head

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QAbstractOAuth::head(const QUrl &url, const QVariantMap
    #      &parameters)
    address = self.uglySide.call(
        'ritual_ZN14QAbstractOAuth4headERK4QUrlRK4QMapI7QString8QVariantE',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QUrl, QMap[str, QVariant])
  def get(
      self,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QAbstractOAuth::get(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#get

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QAbstractOAuth::get(const QUrl &url, const QVariantMap
    #      &parameters)
    address = self.uglySide.call(
        'ritual_ZN14QAbstractOAuth3getERK4QUrlRK4QMapI7QString8QVariantE',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QUrl, QMap[str, QVariant])
  def post(
      self,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QAbstractOAuth::post(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#post

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QAbstractOAuth::post(const QUrl &url, const QVariantMap
    #      &parameters)
    address = self.uglySide.call(
        'ritual_ZN14QAbstractOAuth4postERK4QUrlRK4QMapI7QString8QVariantE',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QUrl, QMap[str, QVariant])
  def put(
      self,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QAbstractOAuth::put(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#put

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QAbstractOAuth::put(const QUrl &url, const QVariantMap
    #      &parameters)
    address = self.uglySide.call(
        'ritual_ZN14QAbstractOAuth3putERK4QUrlRK4QMapI7QString8QVariantE',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QUrl, QMap[str, QVariant])
  def deleteResource(
      self,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QAbstractOAuth::deleteResource(const QUrl
    &url, const QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#deleteResource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QAbstractOAuth::deleteResource(const QUrl &url, const
    #      QVariantMap &parameters)
    address = self.uglySide.call(
        'ritual_ZN14QAbstractOAuth14deleteResourceERK4QUrlRK4QMapI7QString8'
        'QVariantE',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray)
  @overload(NoneType, QByteArray)
  @overload(QNetworkRequest, QByteArray, QByteArray)
  @overload(NoneType, QByteArray, QByteArray)
  def prepareRequest(
      self,
      request: Optional[QNetworkRequest],
      verb: QByteArray,
      body: Optional[QByteArray] = None,
  ) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::prepareRequest(QNetworkRequest *request,
    const QByteArray &verb, const QByteArray &body)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#prepareRequest

    Parameters
    ----------

    request : Optional[QNetworkRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    verb : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    body : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  void QAbstractOAuth::prepareRequest(QNetworkRequest *request, const
    #      QByteArray &verb, const QByteArray &body)
    if body is None:
      from ..QtCore import QByteArray
      body = QByteArray()
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth14prepareRequestEP15QNetworkRequestRK10QB'
        'yteArrayS4_',
        self._addressOf(request), self._valueOf(verb), self._valueOf(body),
    )

  def grant(self) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::grant()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#grant
    """
    #  void QAbstractOAuth::grant()
    self.uglySide.call('ritual_ZN14QAbstractOAuth5grantEv')

  @overload(str)
  def clientIdentifierChanged(self, clientIdentifier: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::clientIdentifierChanged(const QString
    &clientIdentifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#clientIdentifierChanged

    Parameters
    ----------

    clientIdentifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth::clientIdentifierChanged(const QString
    #      &clientIdentifier)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth23clientIdentifierChangedERK7QString',
        clientIdentifier,
    )

  @overload(str)
  def tokenChanged(self, token: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::tokenChanged(const QString &token)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#tokenChanged

    Parameters
    ----------

    token : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth::tokenChanged(const QString &token)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth12tokenChangedERK7QString', token,
    )

  @overload(Status)
  def statusChanged(self, status: Status) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::statusChanged(Status status)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#statusChanged

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void QAbstractOAuth::statusChanged(Status status)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth13statusChangedENS_6StatusE', status.value,
    )

  @overload(QUrl)
  def authorizationUrlChanged(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::authorizationUrlChanged(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#authorizationUrlChanged

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QAbstractOAuth::authorizationUrlChanged(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth23authorizationUrlChangedERK4QUrl',
        self._valueOf(url),
    )

  @overload(QMap[str, QVariant])
  def extraTokensChanged(self, tokens: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::extraTokensChanged(const QVariantMap
    &tokens)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#extraTokensChanged

    Parameters
    ----------

    tokens : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QAbstractOAuth::extraTokensChanged(const QVariantMap &tokens)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth18extraTokensChangedERK4QMapI7QString8QVa'
        'riantE',
        self._valueOf(tokens),
    )

  @overload(ContentType)
  def contentTypeChanged(self, contentType: ContentType) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::contentTypeChanged(ContentType
    contentType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#contentTypeChanged

    Parameters
    ----------

    contentType : ContentType
      Passed on as its number.
    """
    #  void QAbstractOAuth::contentTypeChanged(ContentType contentType)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth18contentTypeChangedENS_11ContentTypeE',
        contentType.value,
    )

  @overload(QUrl)
  def authorizeWithBrowser(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::authorizeWithBrowser(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#authorizeWithBrowser

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QAbstractOAuth::authorizeWithBrowser(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth20authorizeWithBrowserERK4QUrl',
        self._valueOf(url),
    )

  def granted(self) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::granted()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#granted
    """
    #  void QAbstractOAuth::granted()
    self.uglySide.call('ritual_ZN14QAbstractOAuth7grantedEv')

  @overload(QNetworkReply)
  @overload(NoneType)
  def finished(self, reply: Optional[QNetworkReply]) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::finished(QNetworkReply *reply)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#finished

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractOAuth::finished(QNetworkReply *reply)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth8finishedEP13QNetworkReply',
        self._addressOf(reply),
    )

  @overload(QByteArray)
  def replyDataReceived(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QAbstractOAuth::replyDataReceived(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth.html#replyDataReceived

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QAbstractOAuth::replyDataReceived(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN14QAbstractOAuth17replyDataReceivedERK10QByteArray',
        self._valueOf(data),
    )

  def d_func(self) -> Optional[QAbstractOAuthPrivate]:
    """
    Calls Qt's 'QAbstractOAuthPrivate *QAbstractOAuth::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth.html#d_func

    Returns
    -------

    Optional[QAbstractOAuthPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractOAuthPrivate *QAbstractOAuth::d_func()
    address = self.uglySide.call('ritual_ZN14QAbstractOAuth6d_funcEv')
    from . import QAbstractOAuthPrivate
    return QAbstractOAuthPrivate._cuteAt(address)

  @staticmethod
  def modifyParametersFunction(*__, **_) -> Never:
    """
    Qt's 'ModifyParametersFunction QAbstractOAuth::modifyParametersFunction()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth.modifyParametersFunction' has no cute function "
        "yet. Qt's 'ModifyParametersFunction "
        "QAbstractOAuth::modifyParametersFunction() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def requestFailed(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth::requestFailed(const Error error)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth.requestFailed' has no cute function yet. Qt's "
        "'void QAbstractOAuth::requestFailed(const Error error)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def resourceOwnerAuthorization(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth::resourceOwnerAuthorization(const QUrl &url,
    const QMultiMap<QString, QVariant> &parameters)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth.resourceOwnerAuthorization' has no cute function "
        "yet. Qt's 'void QAbstractOAuth::resourceOwnerAuthorization(const "
        "QUrl &url, const QMultiMap<QString, QVariant> &parameters)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def setModifyParametersFunction(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth::setModifyParametersFunction(const
    ModifyParametersFunction &modifyParametersFunction)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth.setModifyParametersFunction' has no cute function "
        "yet. Qt's 'void QAbstractOAuth::setModifyParametersFunction(const "
        "ModifyParametersFunction &modifyParametersFunction)': takes a type "
        "Python has no way to hand over yet.")
