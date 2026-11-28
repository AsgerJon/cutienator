"""
QAbstractOAuth2 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/qabstractoauth2.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject
from . import QAbstractOAuth

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QDateTime, QMetaObject, QUrl, QVariant
  from ..QtNetwork import QHttpMultiPart, QNetworkAccessManager
  from ..QtNetwork import QNetworkReply, QNetworkRequest, QSslConfiguration
  from . import QAbstractOAuth2Private
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDateTime = WAIT['QDateTime']
  QHttpMultiPart = WAIT['QHttpMultiPart']
  QNetworkAccessManager = WAIT['QNetworkAccessManager']
  QNetworkRequest = WAIT['QNetworkRequest']
  QSslConfiguration = WAIT['QSslConfiguration']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractOAuth2(QAbstractOAuth):
  """
  The cute side of Qt's QAbstractOAuth2: a plain Python object standing in
  front of one C++ QAbstractOAuth2.

  It is built on the cute 'QAbstractOAuth', as Qt's QAbstractOAuth2 is built
  on Qt's QAbstractOAuth, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractOAuth2 that has a ritual and that Python
  can call so far, 54 names in all: 'metaObject', 'tr',
  'createAuthenticatedUrl', 'head', 'get', 'post', 'put', 'deleteResource',
  'scope', 'setScope', 'userAgent', 'setUserAgent', 'responseType',
  'clientIdentifierSharedKey', 'setClientIdentifierSharedKey', 'state',
  'setState', 'expirationAt', 'refreshToken', 'setRefreshToken',
  'autoRefresh', 'setAutoRefresh', 'nonceMode', 'setNonceMode', 'nonce',
  'setNonce', 'idToken', 'tokenUrl', 'setTokenUrl', 'sslConfiguration',
  'setSslConfiguration', 'prepareRequest', 'clearNetworkRequestModifier',
  'refreshTokensImplementation', 'refreshTokens', 'scopeChanged',
  'userAgentChanged', 'responseTypeChanged',
  'clientIdentifierSharedKeyChanged', 'stateChanged', 'expirationAtChanged',
  'refreshTokenChanged', 'accessTokenAboutToExpire', 'autoRefreshChanged',
  'nonceModeChanged', 'nonceChanged', 'idTokenChanged', 'tokenUrlChanged',
  'sslConfigurationChanged', 'error', 'serverReportedErrorOccurred',
  'authorizationCallbackReceived', 'setResponseType', 'd_func'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractOAuth2::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAbstractOAuth2::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractOAuth2::~QAbstractOAuth2()': the destructor: Python never
    removes a C++ QAbstractOAuth2.
  - Qt's 'QSet<QByteArray> QAbstractOAuth2::grantedScopeTokens() const':
    gives a type Python has no way to take yet.
  - Qt's 'QSet<QByteArray> QAbstractOAuth2::requestedScopeTokens() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QAbstractOAuth2::setRequestedScopeTokens(const
    QSet<QByteArray> &tokens)': takes a type Python has no way to hand over
    yet.
  - Qt's 'std::chrono::seconds QAbstractOAuth2::refreshLeadTime() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QAbstractOAuth2::setRefreshLeadTime(std::chrono::seconds
    leadTime)': takes a type Python has no way to hand over yet.
  - Qt's 'void QAbstractOAuth2::grantedScopeTokensChanged(const
    QSet<QByteArray> &tokens)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QAbstractOAuth2::requestedScopeTokensChanged(const
    QSet<QByteArray> &tokens)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QAbstractOAuth2::refreshLeadTimeChanged(std::chrono::seconds
    leadTime)': takes a type Python has no way to hand over yet.
  - Qt's 'QAbstractOAuth2::QAbstractOAuth2(QAbstractOAuth2Private &a0,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'void QAbstractOAuth2::setNetworkRequestModifierImpl(const QObject
    *context, QtPrivate::QSlotObjectBase *slot)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'const QAbstractOAuth2Private *QAbstractOAuth2::d_func() const':
    takes in Python what 'QAbstractOAuth2Private *QAbstractOAuth2::d_func()'
    takes.

  What has no ritual
  ------------------

  3 of the 77 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QAbstractOAuth2 is created at the first use, not by
    'QAbstractOAuth2(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractOAuth2.
  - Qt tells when it has removed the C++ QAbstractOAuth2. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractOAuth2 that has no cute function yet,
    'grantedScopeTokens', 'grantedScopeTokensChanged', 'refreshLeadTime',
    'refreshLeadTimeChanged', 'requestedScopeTokens',
    'requestedScopeTokensChanged', 'setNetworkRequestModifier',
    'setNetworkRequestModifierImpl', 'setRefreshLeadTime',
    'setRequestedScopeTokens', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QAbstractOAuth2, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class NonceMode(CuteNum, scoped=True):
    """
    The enum 'QAbstractOAuth2::NonceMode' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Automatic = Kee[int](0)
    Enabled = Kee[int](1)
    Disabled = Kee[int](2)

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
    Calls Qt's 'QString QAbstractOAuth2::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#tr

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
    #  QString QAbstractOAuth2::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QAbstractOAuth22trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractOAuth2'

  #  A C++ QAbstractOAuth2 Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractOAuth2'

  #  The functions Qt calls itself that QAbstractOAuth2 is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'createAuthenticatedUrl': (
          'QUrl QAbstractOAuth2::createAuthenticatedUrl(const QUrl &, '
          'const QVariantMap &)',
      ),
  }

  #  The functions Qt calls itself that QAbstractOAuth2 is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'post': (
          ('_ZN15QAbstractOAuth24postERK4QUrlRK10QByteArray',
           ('address', 'address', 'QtNetwork:QNetworkReply'),
           (
               ('address', 'value', 'QtCore:QUrl'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
          ('_ZN15QAbstractOAuth24postERK4QUrlP14QHttpMultiPart',
           ('address', 'address', 'QtNetwork:QNetworkReply'),
           (
               ('address', 'value', 'QtCore:QUrl'),
               ('address', 'address', 'QtNetwork:QHttpMultiPart'),
           )),
      ),
      'put': (
          ('_ZN15QAbstractOAuth23putERK4QUrlRK10QByteArray',
           ('address', 'address', 'QtNetwork:QNetworkReply'),
           (
               ('address', 'value', 'QtCore:QUrl'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
          ('_ZN15QAbstractOAuth23putERK4QUrlP14QHttpMultiPart',
           ('address', 'address', 'QtNetwork:QNetworkReply'),
           (
               ('address', 'value', 'QtCore:QUrl'),
               ('address', 'address', 'QtNetwork:QHttpMultiPart'),
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
    Calls Qt's 'const QMetaObject *QAbstractOAuth2::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractOAuth2::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QAbstractOAuth210metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def scope(self) -> str:
    """
    Calls Qt's 'QString QAbstractOAuth2::scope() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#scope

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth2::scope() const
    return self.uglySide.call('ritual_ZNK15QAbstractOAuth25scopeEv')

  def userAgent(self) -> str:
    """
    Calls Qt's 'QString QAbstractOAuth2::userAgent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#userAgent

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth2::userAgent() const
    return self.uglySide.call('ritual_ZNK15QAbstractOAuth29userAgentEv')

  def responseType(self) -> str:
    """
    Calls Qt's 'QString QAbstractOAuth2::responseType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#responseType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth2::responseType() const
    return self.uglySide.call('ritual_ZNK15QAbstractOAuth212responseTypeEv')

  def clientIdentifierSharedKey(self) -> str:
    """
    Calls Qt's 'QString QAbstractOAuth2::clientIdentifierSharedKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#clientIdentifierSharedKey

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth2::clientIdentifierSharedKey() const
    return self.uglySide.call(
        'ritual_ZNK15QAbstractOAuth225clientIdentifierSharedKeyEv',
    )

  def state(self) -> str:
    """
    Calls Qt's 'QString QAbstractOAuth2::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#state

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth2::state() const
    return self.uglySide.call('ritual_ZNK15QAbstractOAuth25stateEv')

  def expirationAt(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QAbstractOAuth2::expirationAt() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#expirationAt

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QAbstractOAuth2::expirationAt() const
    address = self.uglySide.call(
        'ritual_ZNK15QAbstractOAuth212expirationAtEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def refreshToken(self) -> str:
    """
    Calls Qt's 'QString QAbstractOAuth2::refreshToken() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#refreshToken

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth2::refreshToken() const
    return self.uglySide.call('ritual_ZNK15QAbstractOAuth212refreshTokenEv')

  def autoRefresh(self) -> bool:
    """
    Calls Qt's 'bool QAbstractOAuth2::autoRefresh() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#autoRefresh
    """
    #  bool QAbstractOAuth2::autoRefresh() const
    return self.uglySide.call('ritual_ZNK15QAbstractOAuth211autoRefreshEv')

  def nonceMode(self) -> NonceMode:
    """
    Calls Qt's 'NonceMode QAbstractOAuth2::nonceMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#nonceMode

    Returns
    -------

    NonceMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'NonceMode(number)' gives.
    """
    #  NonceMode QAbstractOAuth2::nonceMode() const
    return QAbstractOAuth2.NonceMode(self.uglySide.call(
        'ritual_ZNK15QAbstractOAuth29nonceModeEv',
    ))

  def nonce(self) -> str:
    """
    Calls Qt's 'QString QAbstractOAuth2::nonce() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#nonce

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth2::nonce() const
    return self.uglySide.call('ritual_ZNK15QAbstractOAuth25nonceEv')

  def idToken(self) -> str:
    """
    Calls Qt's 'QString QAbstractOAuth2::idToken() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#idToken

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth2::idToken() const
    return self.uglySide.call('ritual_ZNK15QAbstractOAuth27idTokenEv')

  def tokenUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QAbstractOAuth2::tokenUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#tokenUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QAbstractOAuth2::tokenUrl() const
    address = self.uglySide.call('ritual_ZNK15QAbstractOAuth28tokenUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QAbstractOAuth2::sslConfiguration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QAbstractOAuth2::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK15QAbstractOAuth216sslConfigurationEv',
    )
    from ..QtNetwork import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setScope(self, scope: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::setScope(const QString &scope)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#setScope

    Parameters
    ----------

    scope : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::setScope(const QString &scope)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth28setScopeERK7QString', scope,
    )

  @overload(str)
  def setUserAgent(self, userAgent: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::setUserAgent(const QString
    &userAgent)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#setUserAgent

    Parameters
    ----------

    userAgent : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::setUserAgent(const QString &userAgent)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth212setUserAgentERK7QString', userAgent,
    )

  @overload(str)
  def setClientIdentifierSharedKey(
      self,
      clientIdentifierSharedKey: str,
  ) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::setClientIdentifierSharedKey(const
    QString &clientIdentifierSharedKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#setClientIdentifierSharedKey

    Parameters
    ----------

    clientIdentifierSharedKey : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::setClientIdentifierSharedKey(const QString
    #      &clientIdentifierSharedKey)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth228setClientIdentifierSharedKeyERK7QStrin'
        'g',
        clientIdentifierSharedKey,
    )

  @overload(str)
  def setState(self, state: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::setState(const QString &state)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#setState

    Parameters
    ----------

    state : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::setState(const QString &state)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth28setStateERK7QString', state,
    )

  @overload(str)
  def setRefreshToken(self, refreshToken: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::setRefreshToken(const QString
    &refreshToken)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#setRefreshToken

    Parameters
    ----------

    refreshToken : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::setRefreshToken(const QString &refreshToken)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth215setRefreshTokenERK7QString',
        refreshToken,
    )

  @overload(bool)
  def setAutoRefresh(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::setAutoRefresh(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#setAutoRefresh

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstractOAuth2::setAutoRefresh(bool enable)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth214setAutoRefreshEb', enable,
    )

  @overload(NonceMode)
  def setNonceMode(self, mode: NonceMode) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::setNonceMode(NonceMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#setNonceMode

    Parameters
    ----------

    mode : NonceMode
      Passed on as its number.
    """
    #  void QAbstractOAuth2::setNonceMode(NonceMode mode)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth212setNonceModeENS_9NonceModeE',
        mode.value,
    )

  @overload(str)
  def setNonce(self, nonce: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::setNonce(const QString &nonce)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#setNonce

    Parameters
    ----------

    nonce : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::setNonce(const QString &nonce)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth28setNonceERK7QString', nonce,
    )

  @overload(QUrl)
  def setTokenUrl(self, tokenUrl: QUrl) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::setTokenUrl(const QUrl &tokenUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#setTokenUrl

    Parameters
    ----------

    tokenUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QAbstractOAuth2::setTokenUrl(const QUrl &tokenUrl)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth211setTokenUrlERK4QUrl',
        self._valueOf(tokenUrl),
    )

  @overload(QSslConfiguration)
  def setSslConfiguration(self, configuration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::setSslConfiguration(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#setSslConfiguration

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QAbstractOAuth2::setSslConfiguration(const QSslConfiguration
    #      &configuration)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth219setSslConfigurationERK17QSslConfigurat'
        'ion',
        self._valueOf(configuration),
    )

  @overload(str)
  def setResponseType(self, responseType: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::setResponseType(const QString
    &responseType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#setResponseType

    Parameters
    ----------

    responseType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::setResponseType(const QString &responseType)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth215setResponseTypeERK7QString',
        responseType,
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

  @overload(QNetworkAccessManager)
  @overload(QNetworkAccessManager, QObject)
  @overload(QNetworkAccessManager, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      manager: Optional[QNetworkAccessManager],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractOAuth2::QAbstractOAuth2(QNetworkAccessManager *manager, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#QAbstractOAuth2

    Parameters
    ----------

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractOAuth2::QAbstractOAuth2(QNetworkAccessManager *manager,
    #      QObject *parent)
    self._noteCreation(QAbstractOAuth2, lambda: Rituals.call(
        'ritual_ZN15QAbstractOAuth2C1EP21QNetworkAccessManagerP7QObject',
        self._addressOf(manager), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QAbstractOAuth2::QAbstractOAuth2(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#QAbstractOAuth2

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractOAuth2::QAbstractOAuth2(QObject *parent)
    self._noteCreation(QAbstractOAuth2, lambda: Rituals.call(
        'ritual_ZN15QAbstractOAuth2C1EP7QObject',
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

  @overload(QUrl, QMap[str, QVariant])
  def createAuthenticatedUrl(
      self,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> QUrl:
    """
    Calls Qt's 'QUrl QAbstractOAuth2::createAuthenticatedUrl(const QUrl &url,
    const QVariantMap &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#createAuthenticatedUrl

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

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QAbstractOAuth2::createAuthenticatedUrl(const QUrl &url, const
    #      QVariantMap &parameters)
    address = self.uglySide.call(
        'ritual_ZN15QAbstractOAuth222createAuthenticatedUrlERK4QUrlRK4QMapI'
        '7QString8QVariantE',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QUrl, QMap[str, QVariant])
  def head(
      self,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QAbstractOAuth2::head(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#head

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
    #  QNetworkReply *QAbstractOAuth2::head(const QUrl &url, const
    #      QVariantMap &parameters)
    address = self.uglySide.call(
        'ritual_ZN15QAbstractOAuth24headERK4QUrlRK4QMapI7QString8QVariantE',
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
    Calls Qt's 'QNetworkReply *QAbstractOAuth2::get(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#get

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
    #  QNetworkReply *QAbstractOAuth2::get(const QUrl &url, const QVariantMap
    #      &parameters)
    address = self.uglySide.call(
        'ritual_ZN15QAbstractOAuth23getERK4QUrlRK4QMapI7QString8QVariantE',
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
    Calls Qt's 'QNetworkReply *QAbstractOAuth2::post(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#post

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
    #  QNetworkReply *QAbstractOAuth2::post(const QUrl &url, const
    #      QVariantMap &parameters)
    address = self.uglySide.call(
        'ritual_ZN15QAbstractOAuth24postERK4QUrlRK4QMapI7QString8QVariantE',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QUrl, QByteArray)
  def post(self, url: QUrl, data: QByteArray) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QAbstractOAuth2::post(const QUrl &url, const
    QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#post

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QAbstractOAuth2::post(const QUrl &url, const QByteArray
    #      &data)
    ritual = 'ritual_ZN15QAbstractOAuth24postERK4QUrlRK10QByteArray'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractOAuth24postERK4QUrlRK10QByteArray'
    address = self.uglySide.call(
        ritual, self._valueOf(url), self._valueOf(data),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QUrl, QHttpMultiPart)
  @overload(QUrl, NoneType)
  def post(
      self,
      url: QUrl,
      multiPart: Optional[QHttpMultiPart],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QAbstractOAuth2::post(const QUrl &url,
    QHttpMultiPart *multiPart)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#post

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    multiPart : Optional[QHttpMultiPart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QAbstractOAuth2::post(const QUrl &url, QHttpMultiPart
    #      *multiPart)
    ritual = 'ritual_ZN15QAbstractOAuth24postERK4QUrlP14QHttpMultiPart'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractOAuth24postERK4QUrlP14QHttpMultiPart'
    address = self.uglySide.call(
        ritual, self._valueOf(url), self._addressOf(multiPart),
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
    Calls Qt's 'QNetworkReply *QAbstractOAuth2::put(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#put

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
    #  QNetworkReply *QAbstractOAuth2::put(const QUrl &url, const QVariantMap
    #      &parameters)
    address = self.uglySide.call(
        'ritual_ZN15QAbstractOAuth23putERK4QUrlRK4QMapI7QString8QVariantE',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QUrl, QByteArray)
  def put(self, url: QUrl, data: QByteArray) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QAbstractOAuth2::put(const QUrl &url, const
    QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#put

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QAbstractOAuth2::put(const QUrl &url, const QByteArray
    #      &data)
    ritual = 'ritual_ZN15QAbstractOAuth23putERK4QUrlRK10QByteArray'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractOAuth23putERK4QUrlRK10QByteArray'
    address = self.uglySide.call(
        ritual, self._valueOf(url), self._valueOf(data),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QUrl, QHttpMultiPart)
  @overload(QUrl, NoneType)
  def put(
      self,
      url: QUrl,
      multiPart: Optional[QHttpMultiPart],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QAbstractOAuth2::put(const QUrl &url,
    QHttpMultiPart *multiPart)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#put

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    multiPart : Optional[QHttpMultiPart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QAbstractOAuth2::put(const QUrl &url, QHttpMultiPart
    #      *multiPart)
    ritual = 'ritual_ZN15QAbstractOAuth23putERK4QUrlP14QHttpMultiPart'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractOAuth23putERK4QUrlP14QHttpMultiPart'
    address = self.uglySide.call(
        ritual, self._valueOf(url), self._addressOf(multiPart),
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
    Calls Qt's 'QNetworkReply *QAbstractOAuth2::deleteResource(const QUrl
    &url, const QVariantMap &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#deleteResource

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
    #  QNetworkReply *QAbstractOAuth2::deleteResource(const QUrl &url, const
    #      QVariantMap &parameters)
    address = self.uglySide.call(
        'ritual_ZN15QAbstractOAuth214deleteResourceERK4QUrlRK4QMapI7QString'
        '8QVariantE',
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
    Calls Qt's 'void QAbstractOAuth2::prepareRequest(QNetworkRequest
    *request, const QByteArray &verb, const QByteArray &body)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#prepareRequest

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
    #  void QAbstractOAuth2::prepareRequest(QNetworkRequest *request, const
    #      QByteArray &verb, const QByteArray &body)
    if body is None:
      from ..QtCore import QByteArray
      body = QByteArray()
    ritual = (
        'ritual_ZN15QAbstractOAuth214prepareRequestEP15QNetworkRequestRK10Q'
        'ByteArrayS4_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QAbstractOAuth214prepareRequestEP15QNetworkReques'
          'tRK10QByteArrayS4_')
    self.uglySide.call(
        ritual,
        self._addressOf(request), self._valueOf(verb), self._valueOf(body),
    )

  def clearNetworkRequestModifier(self) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::clearNetworkRequestModifier()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#clearNetworkRequestModifier
    """
    #  void QAbstractOAuth2::clearNetworkRequestModifier()
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth227clearNetworkRequestModifierEv',
    )

  def refreshTokensImplementation(self) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::refreshTokensImplementation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#refreshTokensImplementation
    """
    #  void QAbstractOAuth2::refreshTokensImplementation()
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth227refreshTokensImplementationEv',
    )

  def refreshTokens(self) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::refreshTokens()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#refreshTokens
    """
    #  void QAbstractOAuth2::refreshTokens()
    self.uglySide.call('ritual_ZN15QAbstractOAuth213refreshTokensEv')

  @overload(str)
  def scopeChanged(self, scope: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::scopeChanged(const QString &scope)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#scopeChanged

    Parameters
    ----------

    scope : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::scopeChanged(const QString &scope)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth212scopeChangedERK7QString', scope,
    )

  @overload(str)
  def userAgentChanged(self, userAgent: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::userAgentChanged(const QString
    &userAgent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#userAgentChanged

    Parameters
    ----------

    userAgent : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::userAgentChanged(const QString &userAgent)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth216userAgentChangedERK7QString', userAgent,
    )

  @overload(str)
  def responseTypeChanged(self, responseType: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::responseTypeChanged(const QString
    &responseType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#responseTypeChanged

    Parameters
    ----------

    responseType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::responseTypeChanged(const QString &responseType)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth219responseTypeChangedERK7QString',
        responseType,
    )

  @overload(str)
  def clientIdentifierSharedKeyChanged(
      self,
      clientIdentifierSharedKey: str,
  ) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::clientIdentifierSharedKeyChanged(const
    QString &clientIdentifierSharedKey)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html

    Parameters
    ----------

    clientIdentifierSharedKey : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::clientIdentifierSharedKeyChanged(const QString
    #      &clientIdentifierSharedKey)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth232clientIdentifierSharedKeyChangedERK7QS'
        'tring',
        clientIdentifierSharedKey,
    )

  @overload(str)
  def stateChanged(self, state: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::stateChanged(const QString &state)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#stateChanged

    Parameters
    ----------

    state : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::stateChanged(const QString &state)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth212stateChangedERK7QString', state,
    )

  @overload(QDateTime)
  def expirationAtChanged(self, expiration: QDateTime) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::expirationAtChanged(const QDateTime
    &expiration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#expirationAtChanged

    Parameters
    ----------

    expiration : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QAbstractOAuth2::expirationAtChanged(const QDateTime &expiration)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth219expirationAtChangedERK9QDateTime',
        self._valueOf(expiration),
    )

  @overload(str)
  def refreshTokenChanged(self, refreshToken: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::refreshTokenChanged(const QString
    &refreshToken)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#refreshTokenChanged

    Parameters
    ----------

    refreshToken : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::refreshTokenChanged(const QString &refreshToken)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth219refreshTokenChangedERK7QString',
        refreshToken,
    )

  def accessTokenAboutToExpire(self) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::accessTokenAboutToExpire()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#accessTokenAboutToExpire
    """
    #  void QAbstractOAuth2::accessTokenAboutToExpire()
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth224accessTokenAboutToExpireEv',
    )

  @overload(bool)
  def autoRefreshChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::autoRefreshChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#autoRefreshChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstractOAuth2::autoRefreshChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth218autoRefreshChangedEb', enable,
    )

  @overload(NonceMode)
  def nonceModeChanged(self, mode: NonceMode) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::nonceModeChanged(NonceMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#nonceModeChanged

    Parameters
    ----------

    mode : NonceMode
      Passed on as its number.
    """
    #  void QAbstractOAuth2::nonceModeChanged(NonceMode mode)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth216nonceModeChangedENS_9NonceModeE',
        mode.value,
    )

  @overload(str)
  def nonceChanged(self, nonce: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::nonceChanged(const QString &nonce)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#nonceChanged

    Parameters
    ----------

    nonce : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::nonceChanged(const QString &nonce)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth212nonceChangedERK7QString', nonce,
    )

  @overload(str)
  def idTokenChanged(self, idToken: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::idTokenChanged(const QString
    &idToken)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#idTokenChanged

    Parameters
    ----------

    idToken : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2::idTokenChanged(const QString &idToken)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth214idTokenChangedERK7QString', idToken,
    )

  @overload(QUrl)
  def tokenUrlChanged(self, tokenUrl: QUrl) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::tokenUrlChanged(const QUrl &tokenUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#tokenUrlChanged

    Parameters
    ----------

    tokenUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QAbstractOAuth2::tokenUrlChanged(const QUrl &tokenUrl)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth215tokenUrlChangedERK4QUrl',
        self._valueOf(tokenUrl),
    )

  @overload(QSslConfiguration)
  def sslConfigurationChanged(
      self,
      configuration: QSslConfiguration,
  ) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::sslConfigurationChanged(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#sslConfigurationChanged

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QAbstractOAuth2::sslConfigurationChanged(const QSslConfiguration
    #      &configuration)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth223sslConfigurationChangedERK17QSslConfig'
        'uration',
        self._valueOf(configuration),
    )

  @overload(str, str, QUrl)
  def error(self, error: str, errorDescription: str, uri: QUrl) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::error(const QString &error, const
    QString &errorDescription, const QUrl &uri)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#error

    Parameters
    ----------

    error : str
      Passed on as it is: a QString is made of it for the call.

    errorDescription : str
      Passed on as it is: a QString is made of it for the call.

    uri : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QAbstractOAuth2::error(const QString &error, const QString
    #      &errorDescription, const QUrl &uri)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth25errorERK7QStringS2_RK4QUrl',
        error, errorDescription, self._valueOf(uri),
    )

  @overload(str, str, QUrl)
  def serverReportedErrorOccurred(
      self,
      error: str,
      errorDescription: str,
      uri: QUrl,
  ) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::serverReportedErrorOccurred(const
    QString &error, const QString &errorDescription, const QUrl &uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#serverReportedErrorOccurred

    Parameters
    ----------

    error : str
      Passed on as it is: a QString is made of it for the call.

    errorDescription : str
      Passed on as it is: a QString is made of it for the call.

    uri : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QAbstractOAuth2::serverReportedErrorOccurred(const QString
    #      &error, const QString &errorDescription, const QUrl &uri)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth227serverReportedErrorOccurredERK7QString'
        'S2_RK4QUrl',
        error, errorDescription, self._valueOf(uri),
    )

  @overload(QMap[str, QVariant])
  def authorizationCallbackReceived(self, data: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2::authorizationCallbackReceived(const
    QVariantMap &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2.html#authorizationCallbackReceived

    Parameters
    ----------

    data : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QAbstractOAuth2::authorizationCallbackReceived(const QVariantMap
    #      &data)
    self.uglySide.call(
        'ritual_ZN15QAbstractOAuth229authorizationCallbackReceivedERK4QMapI'
        '7QString8QVariantE',
        self._valueOf(data),
    )

  def d_func(self) -> Optional[QAbstractOAuth2Private]:
    """
    Calls Qt's 'QAbstractOAuth2Private *QAbstractOAuth2::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2.html#d_func

    Returns
    -------

    Optional[QAbstractOAuth2Private]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractOAuth2Private *QAbstractOAuth2::d_func()
    address = self.uglySide.call('ritual_ZN15QAbstractOAuth26d_funcEv')
    from . import QAbstractOAuth2Private
    return QAbstractOAuth2Private._cuteAt(address)

  @staticmethod
  def grantedScopeTokens(*__, **_) -> Never:
    """
    Qt's 'QSet<QByteArray> QAbstractOAuth2::grantedScopeTokens() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2.grantedScopeTokens' has no cute function yet. "
        "Qt's 'QSet<QByteArray> QAbstractOAuth2::grantedScopeTokens() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def grantedScopeTokensChanged(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth2::grantedScopeTokensChanged(const
    QSet<QByteArray> &tokens)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2.grantedScopeTokensChanged' has no cute function "
        "yet. Qt's 'void QAbstractOAuth2::grantedScopeTokensChanged(const "
        "QSet<QByteArray> &tokens)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def refreshLeadTime(*__, **_) -> Never:
    """
    Qt's 'std::chrono::seconds QAbstractOAuth2::refreshLeadTime() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2.refreshLeadTime' has no cute function yet. Qt's "
        "'std::chrono::seconds QAbstractOAuth2::refreshLeadTime() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def refreshLeadTimeChanged(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth2::refreshLeadTimeChanged(std::chrono::seconds
    leadTime)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2.refreshLeadTimeChanged' has no cute function yet. "
        "Qt's 'void "
        "QAbstractOAuth2::refreshLeadTimeChanged(std::chrono::seconds "
        "leadTime)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def requestedScopeTokens(*__, **_) -> Never:
    """
    Qt's 'QSet<QByteArray> QAbstractOAuth2::requestedScopeTokens() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2.requestedScopeTokens' has no cute function yet. "
        "Qt's 'QSet<QByteArray> QAbstractOAuth2::requestedScopeTokens() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def requestedScopeTokensChanged(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth2::requestedScopeTokensChanged(const
    QSet<QByteArray> &tokens)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2.requestedScopeTokensChanged' has no cute function "
        "yet. Qt's 'void QAbstractOAuth2::requestedScopeTokensChanged(const "
        "QSet<QByteArray> &tokens)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setNetworkRequestModifier(*__, **_) -> Never:
    """
    Qt's 'QAbstractOAuth2::setNetworkRequestModifier': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2.setNetworkRequestModifier' has no cute function "
        "yet. Qt's 'QAbstractOAuth2::setNetworkRequestModifier': a "
        "template: a pattern and no single function.")

  @staticmethod
  def setNetworkRequestModifierImpl(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth2::setNetworkRequestModifierImpl(const QObject
    *context, QtPrivate::QSlotObjectBase *slot)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2.setNetworkRequestModifierImpl' has no cute "
        "function yet. Qt's 'void "
        "QAbstractOAuth2::setNetworkRequestModifierImpl(const QObject "
        "*context, QtPrivate::QSlotObjectBase *slot)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")

  @staticmethod
  def setRefreshLeadTime(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth2::setRefreshLeadTime(std::chrono::seconds
    leadTime)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2.setRefreshLeadTime' has no cute function yet. "
        "Qt's 'void "
        "QAbstractOAuth2::setRefreshLeadTime(std::chrono::seconds "
        "leadTime)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setRequestedScopeTokens(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth2::setRequestedScopeTokens(const
    QSet<QByteArray> &tokens)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2.setRequestedScopeTokens' has no cute function "
        "yet. Qt's 'void QAbstractOAuth2::setRequestedScopeTokens(const "
        "QSet<QByteArray> &tokens)': takes a type Python has no way to hand "
        "over yet.")
