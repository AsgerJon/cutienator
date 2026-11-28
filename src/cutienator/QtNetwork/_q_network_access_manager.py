"""
QNetworkAccessManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkaccessmanager.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QNetworkRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QMetaObject
  from . import QAbstractNetworkCache, QAuthenticator, QHstsPolicy
  from . import QHttpMultiPart, QNetworkAccessManagerPrivate
  from . import QNetworkCookieJar, QNetworkProxy, QNetworkProxyFactory
  from . import QNetworkReply, QSslConfiguration, QSslError
  from . import QSslPreSharedKeyAuthenticator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractNetworkCache = WAIT['QAbstractNetworkCache']
  QAuthenticator = WAIT['QAuthenticator']
  QByteArray = WAIT['QByteArray']
  QHstsPolicy = WAIT['QHstsPolicy']
  QHttpMultiPart = WAIT['QHttpMultiPart']
  QIODevice = WAIT['QIODevice']
  QNetworkCookieJar = WAIT['QNetworkCookieJar']
  QNetworkProxy = WAIT['QNetworkProxy']
  QNetworkProxyFactory = WAIT['QNetworkProxyFactory']
  QNetworkReply = WAIT['QNetworkReply']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkAccessManager(QObject):
  """
  The cute side of Qt's QNetworkAccessManager: a plain Python object standing
  in front of one C++ QNetworkAccessManager.

  It is built on the cute 'QObject', as Qt's QNetworkAccessManager is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkAccessManager that has a ritual and that
  Python can call so far, 42 names in all: 'metaObject', 'tr',
  'supportedSchemes', 'clearAccessCache', 'clearConnectionCache', 'proxy',
  'setProxy', 'proxyFactory', 'setProxyFactory', 'cache', 'setCache',
  'cookieJar', 'setCookieJar', 'setStrictTransportSecurityEnabled',
  'isStrictTransportSecurityEnabled', 'enableStrictTransportSecurityStore',
  'isStrictTransportSecurityStoreEnabled', 'addStrictTransportSecurityHosts',
  'strictTransportSecurityHosts', 'head', 'get', 'post', 'put',
  'deleteResource', 'sendCustomRequest', 'connectToHostEncrypted',
  'connectToHost', 'setRedirectPolicy', 'redirectPolicy',
  'autoDeleteReplies', 'setAutoDeleteReplies', 'transferTimeout',
  'setTransferTimeout', 'proxyAuthenticationRequired',
  'authenticationRequired', 'finished', 'encrypted', 'sslErrors',
  'preSharedKeyAuthenticationRequired', 'createRequest',
  'supportedSchemesImplementation', 'd_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkAccessManager::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QNetworkAccessManager::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkAccessManager::~QNetworkAccessManager()': the destructor:
    Python never removes a C++ QNetworkAccessManager.
  - Qt's 'std::chrono::milliseconds
    QNetworkAccessManager::transferTimeoutAsDuration() const': gives a type
    Python has no way to take yet.
  - Qt's 'void
    QNetworkAccessManager::setTransferTimeout(std::chrono::milliseconds
    duration)': takes a type Python has no way to hand over yet.
  - Qt's 'const QNetworkAccessManagerPrivate *QNetworkAccessManager::d_func()
    const': takes in Python what 'QNetworkAccessManagerPrivate
    *QNetworkAccessManager::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 62 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QNetworkAccessManager is created at the first use, not by
    'QNetworkAccessManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkAccessManager.
  - Qt tells when it has removed the C++ QNetworkAccessManager. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNetworkAccessManager that has no cute function yet,
    'transferTimeoutAsDuration', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QNetworkAccessManager, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Operation(CuteNum):
    """
    The enum 'QNetworkAccessManager::Operation' of Qt, with the 7 names Qt
    gives in it.
    """

    HeadOperation = Kee[int](1)
    GetOperation = Kee[int](2)
    PutOperation = Kee[int](3)
    PostOperation = Kee[int](4)
    DeleteOperation = Kee[int](5)
    CustomOperation = Kee[int](6)
    UnknownOperation = Kee[int](0)

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
    Calls Qt's 'QString QNetworkAccessManager::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#tr

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
    #  QString QNetworkAccessManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QNetworkAccessManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkAccessManager'

  #  A C++ QNetworkAccessManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkAccessManager'

  #  The functions Qt calls itself that QNetworkAccessManager is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'supportedSchemes': (
          'QStringList QNetworkAccessManager::supportedSchemes() const',
      ),
  }

  #  The functions Qt calls itself that QNetworkAccessManager is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createRequest': (
          ('_ZN21QNetworkAccessManager13createRequestENS_9OperationERK15QNe'
           'tworkRequestP9QIODevice',
           ('address', 'address', 'QtNetwork:QNetworkReply'),
           (
               ('int', 'enum', 'QtNetwork:QNetworkAccessManager.Operation'),
               ('address', 'value', 'QtNetwork:QNetworkRequest'),
               ('address', 'address', 'QtCore:QIODevice'),
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
    Calls Qt's 'const QMetaObject *QNetworkAccessManager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkAccessManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkAccessManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def supportedSchemes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QNetworkAccessManager::supportedSchemes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#supportedSchemes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QNetworkAccessManager::supportedSchemes() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkAccessManager16supportedSchemesEv',
    )
    return QStringList._cuteOwning(address)

  def proxy(self) -> QNetworkProxy:
    """
    Calls Qt's 'QNetworkProxy QNetworkAccessManager::proxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#proxy

    Returns
    -------

    QNetworkProxy
      A new cute QNetworkProxy around the copy Qt gave back. Python owns it.
    """
    #  QNetworkProxy QNetworkAccessManager::proxy() const
    address = self.uglySide.call('ritual_ZNK21QNetworkAccessManager5proxyEv')
    from . import QNetworkProxy
    return QNetworkProxy._cuteOwning(address)

  def proxyFactory(self) -> Optional[QNetworkProxyFactory]:
    """
    Calls Qt's 'QNetworkProxyFactory *QNetworkAccessManager::proxyFactory()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#proxyFactory

    Returns
    -------

    Optional[QNetworkProxyFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkProxyFactory *QNetworkAccessManager::proxyFactory() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkAccessManager12proxyFactoryEv',
    )
    from . import QNetworkProxyFactory
    return QNetworkProxyFactory._cuteAt(address)

  def cache(self) -> Optional[QAbstractNetworkCache]:
    """
    Calls Qt's 'QAbstractNetworkCache *QNetworkAccessManager::cache() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#cache

    Returns
    -------

    Optional[QAbstractNetworkCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractNetworkCache *QNetworkAccessManager::cache() const
    address = self.uglySide.call('ritual_ZNK21QNetworkAccessManager5cacheEv')
    from . import QAbstractNetworkCache
    return QAbstractNetworkCache._cuteAt(address)

  def cookieJar(self) -> Optional[QNetworkCookieJar]:
    """
    Calls Qt's 'QNetworkCookieJar *QNetworkAccessManager::cookieJar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#cookieJar

    Returns
    -------

    Optional[QNetworkCookieJar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkCookieJar *QNetworkAccessManager::cookieJar() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkAccessManager9cookieJarEv',
    )
    from . import QNetworkCookieJar
    return QNetworkCookieJar._cuteAt(address)

  def isStrictTransportSecurityEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QNetworkAccessManager::isStrictTransportSecurityEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html
    """
    #  bool QNetworkAccessManager::isStrictTransportSecurityEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QNetworkAccessManager32isStrictTransportSecurityEnable'
        'dEv',
    )

  def isStrictTransportSecurityStoreEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QNetworkAccessManager::isStrictTransportSecurityStoreEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html
    """
    #  bool QNetworkAccessManager::isStrictTransportSecurityStoreEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QNetworkAccessManager37isStrictTransportSecurityStoreE'
        'nabledEv',
    )

  def strictTransportSecurityHosts(self) -> QList[QHstsPolicy]:
    """
    Calls Qt's 'QList<QHstsPolicy>
    QNetworkAccessManager::strictTransportSecurityHosts() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html

    Returns
    -------

    QList[QHstsPolicy]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHstsPolicy>
    #      QNetworkAccessManager::strictTransportSecurityHosts() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkAccessManager28strictTransportSecurityHostsEv',
    )
    from . import QHstsPolicy
    return QList[QHstsPolicy]._cuteOwning(address)

  def redirectPolicy(self) -> QNetworkRequest.RedirectPolicy:
    """
    Calls Qt's 'QNetworkRequest::RedirectPolicy
    QNetworkAccessManager::redirectPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#redirectPolicy

    Returns
    -------

    QNetworkRequest.RedirectPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QNetworkRequest.RedirectPolicy(number)' gives.
    """
    #  QNetworkRequest::RedirectPolicy
    #      QNetworkAccessManager::redirectPolicy() const
    return QNetworkRequest.RedirectPolicy(self.uglySide.call(
        'ritual_ZNK21QNetworkAccessManager14redirectPolicyEv',
    ))

  def autoDeleteReplies(self) -> bool:
    """
    Calls Qt's 'bool QNetworkAccessManager::autoDeleteReplies() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#autoDeleteReplies
    """
    #  bool QNetworkAccessManager::autoDeleteReplies() const
    return self.uglySide.call(
        'ritual_ZNK21QNetworkAccessManager17autoDeleteRepliesEv',
    )

  def transferTimeout(self) -> int:
    """
    Calls Qt's 'int QNetworkAccessManager::transferTimeout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#transferTimeout
    """
    #  int QNetworkAccessManager::transferTimeout() const
    return self.uglySide.call(
        'ritual_ZNK21QNetworkAccessManager15transferTimeoutEv',
    )

  def supportedSchemesImplementation(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QNetworkAccessManager::supportedSchemesImplementation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QNetworkAccessManager::supportedSchemesImplementation()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkAccessManager30supportedSchemesImplementationE'
        'v',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNetworkProxy)
  def setProxy(self, proxy: QNetworkProxy) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::setProxy(const QNetworkProxy
    &proxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#setProxy

    Parameters
    ----------

    proxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  void QNetworkAccessManager::setProxy(const QNetworkProxy &proxy)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager8setProxyERK13QNetworkProxy',
        self._valueOf(proxy),
    )

  @overload(QNetworkProxyFactory)
  @overload(NoneType)
  def setProxyFactory(self, factory: Optional[QNetworkProxyFactory]) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessManager::setProxyFactory(QNetworkProxyFactory *factory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#setProxyFactory

    Parameters
    ----------

    factory : Optional[QNetworkProxyFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessManager::setProxyFactory(QNetworkProxyFactory
    #      *factory)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager15setProxyFactoryEP20QNetworkProxy'
        'Factory',
        self._addressOf(factory),
    )

  @overload(QAbstractNetworkCache)
  @overload(NoneType)
  def setCache(self, cache: Optional[QAbstractNetworkCache]) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::setCache(QAbstractNetworkCache
    *cache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#setCache

    Parameters
    ----------

    cache : Optional[QAbstractNetworkCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessManager::setCache(QAbstractNetworkCache *cache)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager8setCacheEP21QAbstractNetworkCache',
        self._addressOf(cache),
    )

  @overload(QNetworkCookieJar)
  @overload(NoneType)
  def setCookieJar(self, cookieJar: Optional[QNetworkCookieJar]) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::setCookieJar(QNetworkCookieJar
    *cookieJar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#setCookieJar

    Parameters
    ----------

    cookieJar : Optional[QNetworkCookieJar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessManager::setCookieJar(QNetworkCookieJar *cookieJar)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager12setCookieJarEP17QNetworkCookieJa'
        'r',
        self._addressOf(cookieJar),
    )

  @overload(bool)
  def setStrictTransportSecurityEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessManager::setStrictTransportSecurityEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QNetworkAccessManager::setStrictTransportSecurityEnabled(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager33setStrictTransportSecurityEnable'
        'dEb',
        enabled,
    )

  @overload(QNetworkRequest.RedirectPolicy)
  def setRedirectPolicy(
      self,
      policy: QNetworkRequest.RedirectPolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessManager::setRedirectPolicy(QNetworkRequest::RedirectPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#setRedirectPolicy

    Parameters
    ----------

    policy : QNetworkRequest.RedirectPolicy
      Passed on as its number.
    """
    #  void QNetworkAccessManager::setRedirectPolicy(QNetworkRequest::
    #      RedirectPolicy policy)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager17setRedirectPolicyEN15QNetworkReq'
        'uest14RedirectPolicyE',
        policy.value,
    )

  @overload(bool)
  def setAutoDeleteReplies(self, autoDelete: bool) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::setAutoDeleteReplies(bool
    autoDelete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#setAutoDeleteReplies

    Parameters
    ----------

    autoDelete : bool
      Passed on as it is.
    """
    #  void QNetworkAccessManager::setAutoDeleteReplies(bool autoDelete)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager20setAutoDeleteRepliesEb',
        autoDelete,
    )

  @overload(int)
  def setTransferTimeout(self, timeout: int) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::setTransferTimeout(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#setTransferTimeout

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void QNetworkAccessManager::setTransferTimeout(int timeout)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager18setTransferTimeoutEi', timeout,
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
    Notes what was given, for Qt's
    'QNetworkAccessManager::QNetworkAccessManager(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#QNetworkAccessManager

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QNetworkAccessManager::QNetworkAccessManager(QObject *parent)
    self._noteCreation(QNetworkAccessManager, lambda: Rituals.call(
        'ritual_ZN21QNetworkAccessManagerC1EP7QObject',
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

  def clearAccessCache(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::clearAccessCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#clearAccessCache
    """
    #  void QNetworkAccessManager::clearAccessCache()
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager16clearAccessCacheEv',
    )

  def clearConnectionCache(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::clearConnectionCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#clearConnectionCache
    """
    #  void QNetworkAccessManager::clearConnectionCache()
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager20clearConnectionCacheEv',
    )

  @overload(bool)
  @overload(bool, str)
  def enableStrictTransportSecurityStore(
      self,
      enabled: bool,
      storeDir: str = '',
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessManager::enableStrictTransportSecurityStore(bool enabled,
    const QString &storeDir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.

    storeDir : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QNetworkAccessManager::enableStrictTransportSecurityStore(bool
    #      enabled, const QString &storeDir)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager34enableStrictTransportSecuritySto'
        'reEbRK7QString',
        enabled, storeDir,
    )

  @overload(QList[QHstsPolicy])
  def addStrictTransportSecurityHosts(
      self,
      knownHosts: QList[QHstsPolicy],
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessManager::addStrictTransportSecurityHosts(const
    QList<QHstsPolicy> &knownHosts)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html

    Parameters
    ----------

    knownHosts : QList[QHstsPolicy]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNetworkAccessManager::addStrictTransportSecurityHosts(const
    #      QList<QHstsPolicy> &knownHosts)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager31addStrictTransportSecurityHostsE'
        'RK5QListI11QHstsPolicyE',
        self._valueOf(knownHosts),
    )

  @overload(QNetworkRequest)
  def head(self, request: QNetworkRequest) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::head(const
    QNetworkRequest &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#head

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::head(const QNetworkRequest
    #      &request)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager4headERK15QNetworkRequest',
        self._valueOf(request),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest)
  def get(self, request: QNetworkRequest) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::get(const
    QNetworkRequest &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#get

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::get(const QNetworkRequest
    #      &request)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager3getERK15QNetworkRequest',
        self._valueOf(request),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QIODevice)
  @overload(QNetworkRequest, NoneType)
  def get(
      self,
      request: QNetworkRequest,
      data: Optional[QIODevice],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::get(const
    QNetworkRequest &request, QIODevice *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#get

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::get(const QNetworkRequest
    #      &request, QIODevice *data)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager3getERK15QNetworkRequestP9QIODevic'
        'e',
        self._valueOf(request), self._addressOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray)
  def get(
      self,
      request: QNetworkRequest,
      data: QByteArray,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::get(const
    QNetworkRequest &request, const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#get

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::get(const QNetworkRequest
    #      &request, const QByteArray &data)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager3getERK15QNetworkRequestRK10QByteA'
        'rray',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QIODevice)
  @overload(QNetworkRequest, NoneType)
  def post(
      self,
      request: QNetworkRequest,
      data: Optional[QIODevice],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::post(const
    QNetworkRequest &request, QIODevice *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#post

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::post(const QNetworkRequest
    #      &request, QIODevice *data)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager4postERK15QNetworkRequestP9QIODevi'
        'ce',
        self._valueOf(request), self._addressOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray)
  def post(
      self,
      request: QNetworkRequest,
      data: QByteArray,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::post(const
    QNetworkRequest &request, const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#post

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::post(const QNetworkRequest
    #      &request, const QByteArray &data)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager4postERK15QNetworkRequestRK10QByte'
        'Array',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest)
  def post(self, request: QNetworkRequest) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::post(const
    QNetworkRequest &request, std::nullptr_t a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#post

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::post(const QNetworkRequest
    #      &request, std::nullptr_t a1)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager4postERK15QNetworkRequestDn',
        self._valueOf(request),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QHttpMultiPart)
  def post(
      self,
      request: QNetworkRequest,
      multiPart: Optional[QHttpMultiPart],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::post(const
    QNetworkRequest &request, QHttpMultiPart *multiPart)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#post

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    multiPart : Optional[QHttpMultiPart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::post(const QNetworkRequest
    #      &request, QHttpMultiPart *multiPart)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager4postERK15QNetworkRequestP14QHttpM'
        'ultiPart',
        self._valueOf(request), self._addressOf(multiPart),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QIODevice)
  @overload(QNetworkRequest, NoneType)
  def put(
      self,
      request: QNetworkRequest,
      data: Optional[QIODevice],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::put(const
    QNetworkRequest &request, QIODevice *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#put

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::put(const QNetworkRequest
    #      &request, QIODevice *data)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager3putERK15QNetworkRequestP9QIODevic'
        'e',
        self._valueOf(request), self._addressOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray)
  def put(
      self,
      request: QNetworkRequest,
      data: QByteArray,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::put(const
    QNetworkRequest &request, const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#put

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::put(const QNetworkRequest
    #      &request, const QByteArray &data)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager3putERK15QNetworkRequestRK10QByteA'
        'rray',
        self._valueOf(request), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest)
  def put(self, request: QNetworkRequest) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::put(const
    QNetworkRequest &request, std::nullptr_t a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#put

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::put(const QNetworkRequest
    #      &request, std::nullptr_t a1)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager3putERK15QNetworkRequestDn',
        self._valueOf(request),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QHttpMultiPart)
  def put(
      self,
      request: QNetworkRequest,
      multiPart: Optional[QHttpMultiPart],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::put(const
    QNetworkRequest &request, QHttpMultiPart *multiPart)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#put

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    multiPart : Optional[QHttpMultiPart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::put(const QNetworkRequest
    #      &request, QHttpMultiPart *multiPart)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager3putERK15QNetworkRequestP14QHttpMu'
        'ltiPart',
        self._valueOf(request), self._addressOf(multiPart),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest)
  def deleteResource(
      self,
      request: QNetworkRequest,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::deleteResource(const
    QNetworkRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#deleteResource

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::deleteResource(const
    #      QNetworkRequest &request)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager14deleteResourceERK15QNetworkReque'
        'st',
        self._valueOf(request),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray)
  @overload(QNetworkRequest, QByteArray, QIODevice)
  @overload(QNetworkRequest, QByteArray, NoneType)
  def sendCustomRequest(
      self,
      request: QNetworkRequest,
      verb: QByteArray,
      data: Optional[QIODevice] = None,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::sendCustomRequest(const
    QNetworkRequest &request, const QByteArray &verb, QIODevice *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#sendCustomRequest

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    verb : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::sendCustomRequest(const
    #      QNetworkRequest &request, const QByteArray &verb, QIODevice *data)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager17sendCustomRequestERK15QNetworkRe'
        'questRK10QByteArrayP9QIODevice',
        self._valueOf(request), self._valueOf(verb), self._addressOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray, QByteArray)
  def sendCustomRequest(
      self,
      request: QNetworkRequest,
      verb: QByteArray,
      data: QByteArray,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::sendCustomRequest(const
    QNetworkRequest &request, const QByteArray &verb, const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#sendCustomRequest

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    verb : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::sendCustomRequest(const
    #      QNetworkRequest &request, const QByteArray &verb, const QByteArray
    #      &data)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager17sendCustomRequestERK15QNetworkRe'
        'questRK10QByteArrayS5_',
        self._valueOf(request), self._valueOf(verb), self._valueOf(data),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QNetworkRequest, QByteArray, QHttpMultiPart)
  def sendCustomRequest(
      self,
      request: QNetworkRequest,
      verb: QByteArray,
      multiPart: Optional[QHttpMultiPart],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::sendCustomRequest(const
    QNetworkRequest &request, const QByteArray &verb, QHttpMultiPart
    *multiPart)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#sendCustomRequest

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    verb : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    multiPart : Optional[QHttpMultiPart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::sendCustomRequest(const
    #      QNetworkRequest &request, const QByteArray &verb, QHttpMultiPart
    #      *multiPart)
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager17sendCustomRequestERK15QNetworkRe'
        'questRK10QByteArrayP14QHttpMultiPart',
        self._valueOf(request), self._valueOf(verb),
        self._addressOf(multiPart),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(str, int, QSslConfiguration)
  def connectToHostEncrypted(
      self,
      hostName: str,
      port: int,
      sslConfiguration: QSslConfiguration,
  ) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::connectToHostEncrypted(const
    QString &hostName, quint16 port, const QSslConfiguration
    &sslConfiguration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#connectToHostEncrypted

    Parameters
    ----------

    hostName : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.

    sslConfiguration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QNetworkAccessManager::connectToHostEncrypted(const QString
    #      &hostName, quint16 port, const QSslConfiguration
    #      &sslConfiguration)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager22connectToHostEncryptedERK7QStrin'
        'gtRK17QSslConfiguration',
        hostName, port, self._valueOf(sslConfiguration),
    )

  @overload(str, int, QSslConfiguration, str)
  def connectToHostEncrypted(
      self,
      hostName: str,
      port: int,
      sslConfiguration: QSslConfiguration,
      peerName: str,
  ) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::connectToHostEncrypted(const
    QString &hostName, quint16 port, const QSslConfiguration
    &sslConfiguration, const QString &peerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#connectToHostEncrypted

    Parameters
    ----------

    hostName : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.

    sslConfiguration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.

    peerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkAccessManager::connectToHostEncrypted(const QString
    #      &hostName, quint16 port, const QSslConfiguration
    #      &sslConfiguration, const QString &peerName)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager22connectToHostEncryptedERK7QStrin'
        'gtRK17QSslConfigurationS2_',
        hostName, port, self._valueOf(sslConfiguration), peerName,
    )

  @overload(str)
  @overload(str, int)
  def connectToHost(self, hostName: str, port: int = 80) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::connectToHost(const QString
    &hostName, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#connectToHost

    Parameters
    ----------

    hostName : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 80.
    """
    #  void QNetworkAccessManager::connectToHost(const QString &hostName,
    #      quint16 port)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager13connectToHostERK7QStringt',
        hostName, port,
    )

  @overload(QNetworkProxy, QAuthenticator)
  @overload(QNetworkProxy, NoneType)
  def proxyAuthenticationRequired(
      self,
      proxy: QNetworkProxy,
      authenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::proxyAuthenticationRequired(const
    QNetworkProxy &proxy, QAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html

    Parameters
    ----------

    proxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessManager::proxyAuthenticationRequired(const
    #      QNetworkProxy &proxy, QAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager27proxyAuthenticationRequiredERK13'
        'QNetworkProxyP14QAuthenticator',
        self._valueOf(proxy), self._addressOf(authenticator),
    )

  @overload(QNetworkReply, QAuthenticator)
  @overload(QNetworkReply, NoneType)
  @overload(NoneType, QAuthenticator)
  @overload(NoneType, NoneType)
  def authenticationRequired(
      self,
      reply: Optional[QNetworkReply],
      authenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessManager::authenticationRequired(QNetworkReply *reply,
    QAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#authenticationRequired

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessManager::authenticationRequired(QNetworkReply
    #      *reply, QAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager22authenticationRequiredEP13QNetwo'
        'rkReplyP14QAuthenticator',
        self._addressOf(reply), self._addressOf(authenticator),
    )

  @overload(QNetworkReply)
  @overload(NoneType)
  def finished(self, reply: Optional[QNetworkReply]) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::finished(QNetworkReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#finished

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessManager::finished(QNetworkReply *reply)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager8finishedEP13QNetworkReply',
        self._addressOf(reply),
    )

  @overload(QNetworkReply)
  @overload(NoneType)
  def encrypted(self, reply: Optional[QNetworkReply]) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::encrypted(QNetworkReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#encrypted

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessManager::encrypted(QNetworkReply *reply)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager9encryptedEP13QNetworkReply',
        self._addressOf(reply),
    )

  @overload(QNetworkReply, QList[QSslError])
  @overload(NoneType, QList[QSslError])
  def sslErrors(
      self,
      reply: Optional[QNetworkReply],
      errors: QList[QSslError],
  ) -> None:
    """
    Calls Qt's 'void QNetworkAccessManager::sslErrors(QNetworkReply *reply,
    const QList<QSslError> &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#sslErrors

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNetworkAccessManager::sslErrors(QNetworkReply *reply, const
    #      QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager9sslErrorsEP13QNetworkReplyRK5QLis'
        'tI9QSslErrorE',
        self._addressOf(reply), self._valueOf(errors),
    )

  @overload(QNetworkReply, QSslPreSharedKeyAuthenticator)
  @overload(QNetworkReply, NoneType)
  @overload(NoneType, QSslPreSharedKeyAuthenticator)
  @overload(NoneType, NoneType)
  def preSharedKeyAuthenticationRequired(
      self,
      reply: Optional[QNetworkReply],
      authenticator: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessManager::preSharedKeyAuthenticationRequired(QNetworkReply
    *reply, QSslPreSharedKeyAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    authenticator : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessManager::preSharedKeyAuthenticationRequired(
    #      QNetworkReply *reply, QSslPreSharedKeyAuthenticator
    #      *authenticator)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessManager34preSharedKeyAuthenticationRequir'
        'edEP13QNetworkReplyP29QSslPreSharedKeyAuthenticator',
        self._addressOf(reply), self._addressOf(authenticator),
    )

  @overload(Operation, QNetworkRequest)
  @overload(Operation, QNetworkRequest, QIODevice)
  @overload(Operation, QNetworkRequest, NoneType)
  def createRequest(
      self,
      op: Operation,
      request: QNetworkRequest,
      outgoingData: Optional[QIODevice] = None,
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QNetworkAccessManager::createRequest(Operation
    op, const QNetworkRequest &request, QIODevice *outgoingData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanager.html#createRequest

    Parameters
    ----------

    op : Operation
      Passed on as its number.

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    outgoingData : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManager::createRequest(Operation op,
    #      const QNetworkRequest &request, QIODevice *outgoingData)
    ritual = (
        'ritual_ZN21QNetworkAccessManager13createRequestENS_9OperationERK15'
        'QNetworkRequestP9QIODevice')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QNetworkAccessManager13createRequestENS_9Operatio'
          'nERK15QNetworkRequestP9QIODevice')
    address = self.uglySide.call(
        ritual,
        op.value, self._valueOf(request), self._addressOf(outgoingData),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  def d_func(self) -> Optional[QNetworkAccessManagerPrivate]:
    """
    Calls Qt's 'QNetworkAccessManagerPrivate
    *QNetworkAccessManager::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessmanager.html#d_func

    Returns
    -------

    Optional[QNetworkAccessManagerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkAccessManagerPrivate *QNetworkAccessManager::d_func()
    address = self.uglySide.call('ritual_ZN21QNetworkAccessManager6d_funcEv')
    from . import QNetworkAccessManagerPrivate
    return QNetworkAccessManagerPrivate._cuteAt(address)

  @staticmethod
  def transferTimeoutAsDuration(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds
    QNetworkAccessManager::transferTimeoutAsDuration() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkAccessManager.transferTimeoutAsDuration' has no cute "
        "function yet. Qt's 'std::chrono::milliseconds "
        "QNetworkAccessManager::transferTimeoutAsDuration() const': gives a "
        "type Python has no way to take yet.")
