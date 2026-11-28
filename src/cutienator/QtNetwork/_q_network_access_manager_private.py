"""
QNetworkAccessManagerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessmanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkAccessManagerPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QThread
  from . import QHttpMultiPart, QNetworkAccessManager, QNetworkProxy
  from . import QNetworkProxyQuery, QNetworkReply, QNetworkRequest, QSslError
  from . import QSslPreSharedKeyAuthenticator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHttpMultiPart = WAIT['QHttpMultiPart']
  QNetworkAccessManager = WAIT['QNetworkAccessManager']
  QNetworkProxyQuery = WAIT['QNetworkProxyQuery']
  QNetworkReply = WAIT['QNetworkReply']
  QNetworkRequest = WAIT['QNetworkRequest']
  QSslError = WAIT['QSslError']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkAccessManagerPrivate(QObjectPrivate):
  """
  The cute side of Qt's QNetworkAccessManagerPrivate: a plain Python object
  standing in front of one C++ QNetworkAccessManagerPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QNetworkAccessManagerPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkAccessManagerPrivate that has a ritual and
  that Python can call so far, 12 names in all: 'createThread',
  'destroyThread', '_q_replyFinished', '_q_replyEncrypted',
  '_q_replySslErrors', '_q_replyPreSharedKeyAuthenticationRequired',
  'postProcess', 'createCookieJar', 'queryProxy', 'prepareMultipart',
  'clearConnectionCache', 'q_func'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkAccessManagerPrivate::~QNetworkAccessManagerPrivate()': the
    destructor: Python never removes a C++ QNetworkAccessManagerPrivate.
  - Qt's 'const QNetworkAccessManager *QNetworkAccessManagerPrivate::q_func()
    const': takes in Python what 'QNetworkAccessManager
    *QNetworkAccessManagerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  11 of the 25 functions Qt declares: 4 cannot be called and cannot be called
  through the meta-object and cannot be copied; 3 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 2
  leans on 'QNetworkAccessAuthenticationManager; 1 leans on 'vtable for
  QNetworkAccessCache', which Qt's source does not mark for use from outside
  Qt and has no code for that could be taken; 1 leans on
  'QNetworkAccessCache.

  What to expect
  --------------

  - The C++ QNetworkAccessManagerPrivate is created at the first use, not by
    'QNetworkAccessManagerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkAccessManagerPrivate.
  - Each name of Qt's QNetworkAccessManagerPrivate that has no cute function
    yet, '__init__', 'authenticationRequired', 'backendSupportedSchemes',
    'cacheCredentials', 'cacheProxyCredentials', 'clearAuthenticationCache',
    'ensureBackendPluginsLoaded', 'fetchCachedCredentials',
    'fetchCachedProxyCredentials', 'findBackend',
    'proxyAuthenticationRequired', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QNetworkAccessManager)
  @overload(NoneType)
  def clearConnectionCache(manager: Optional[QNetworkAccessManager]) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessManagerPrivate::clearConnectionCache(QNetworkAccessManager
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanagerprivate.html

    Parameters
    ----------

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessManagerPrivate::clearConnectionCache(
    #      QNetworkAccessManager *manager)
    Rituals.call(
        'ritual_ZN28QNetworkAccessManagerPrivate20clearConnectionCacheEP21Q'
        'NetworkAccessManager',
        CuteMixin._addressOf(manager),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkAccessManagerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QNetworkAccessManagerPrivate::QNetworkAccessManagerPrivate()':
    leans on 'vtable for QNetworkAccessCache', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkAccessManagerPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QNetworkAccessManagerPrivate::QNetworkAccessManagerPrivate()': "
        "leans on 'vtable for QNetworkAccessCache', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def createThread(self) -> Optional[QThread]:
    """
    Calls Qt's 'QThread *QNetworkAccessManagerPrivate::createThread()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanagerprivate.html#createThread

    Returns
    -------

    Optional[QThread]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThread *QNetworkAccessManagerPrivate::createThread()
    address = self.uglySide.call(
        'ritual_ZN28QNetworkAccessManagerPrivate12createThreadEv',
    )
    from ..QtCore import QThread
    return QThread._cuteAt(address)

  def destroyThread(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessManagerPrivate::destroyThread()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanagerprivate.html#destroyThread
    """
    #  void QNetworkAccessManagerPrivate::destroyThread()
    self.uglySide.call(
        'ritual_ZN28QNetworkAccessManagerPrivate13destroyThreadEv',
    )

  @overload(QNetworkReply)
  @overload(NoneType)
  def _q_replyFinished(self, reply: Optional[QNetworkReply]) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessManagerPrivate::_q_replyFinished(QNetworkReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanagerprivate.html#_q_replyFinished

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessManagerPrivate::_q_replyFinished(QNetworkReply
    #      *reply)
    self.uglySide.call(
        'ritual_ZN28QNetworkAccessManagerPrivate16_q_replyFinishedEP13QNetw'
        'orkReply',
        self._addressOf(reply),
    )

  @overload(QNetworkReply)
  @overload(NoneType)
  def _q_replyEncrypted(self, reply: Optional[QNetworkReply]) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessManagerPrivate::_q_replyEncrypted(QNetworkReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanagerprivate.html

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessManagerPrivate::_q_replyEncrypted(QNetworkReply
    #      *reply)
    self.uglySide.call(
        'ritual_ZN28QNetworkAccessManagerPrivate17_q_replyEncryptedEP13QNet'
        'workReply',
        self._addressOf(reply),
    )

  @overload(QList[QSslError])
  def _q_replySslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QNetworkAccessManagerPrivate::_q_replySslErrors(const
    QList<QSslError> &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanagerprivate.html

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNetworkAccessManagerPrivate::_q_replySslErrors(const
    #      QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN28QNetworkAccessManagerPrivate17_q_replySslErrorsERK5QLis'
        'tI9QSslErrorE',
        self._valueOf(errors),
    )

  @overload(QSslPreSharedKeyAuthenticator)
  @overload(NoneType)
  def _q_replyPreSharedKeyAuthenticationRequired(
      self,
      authenticator: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessManagerPrivate::_q_replyPreSharedKeyAuthenticationRequired(
    QSslPreSharedKeyAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanagerprivate.html

    Parameters
    ----------

    authenticator : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessManagerPrivate::
    #      _q_replyPreSharedKeyAuthenticationRequired(
    #      QSslPreSharedKeyAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN28QNetworkAccessManagerPrivate42_q_replyPreSharedKeyAuthe'
        'nticationRequiredEP29QSslPreSharedKeyAuthenticator',
        self._addressOf(authenticator),
    )

  @overload(QNetworkReply)
  @overload(NoneType)
  def postProcess(
      self,
      reply: Optional[QNetworkReply],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply
    *QNetworkAccessManagerPrivate::postProcess(QNetworkReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanagerprivate.html#postProcess

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QNetworkAccessManagerPrivate::postProcess(QNetworkReply
    #      *reply)
    address = self.uglySide.call(
        'ritual_ZN28QNetworkAccessManagerPrivate11postProcessEP13QNetworkRe'
        'ply',
        self._addressOf(reply),
    )
    from . import QNetworkReply
    return QNetworkReply._cuteAt(address)

  def createCookieJar(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessManagerPrivate::createCookieJar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanagerprivate.html#createCookieJar
    """
    #  void QNetworkAccessManagerPrivate::createCookieJar() const
    self.uglySide.call(
        'ritual_ZNK28QNetworkAccessManagerPrivate15createCookieJarEv',
    )

  @overload(QNetworkProxyQuery)
  def queryProxy(self, query: QNetworkProxyQuery) -> QList[QNetworkProxy]:
    """
    Calls Qt's 'QList<QNetworkProxy>
    QNetworkAccessManagerPrivate::queryProxy(const QNetworkProxyQuery
    &query)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanagerprivate.html#queryProxy

    Parameters
    ----------

    query : QNetworkProxyQuery
      Passed on as a value: Qt reads the C++ QNetworkProxyQuery, which stays
      Python's own.

    Returns
    -------

    QList[QNetworkProxy]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QNetworkProxy> QNetworkAccessManagerPrivate::queryProxy(const
    #      QNetworkProxyQuery &query)
    address = self.uglySide.call(
        'ritual_ZN28QNetworkAccessManagerPrivate10queryProxyERK18QNetworkPr'
        'oxyQuery',
        self._valueOf(query),
    )
    from . import QNetworkProxy
    return QList[QNetworkProxy]._cuteOwning(address)

  @overload(QNetworkRequest, QHttpMultiPart)
  @overload(QNetworkRequest, NoneType)
  def prepareMultipart(
      self,
      request: QNetworkRequest,
      multiPart: Optional[QHttpMultiPart],
  ) -> QNetworkRequest:
    """
    Calls Qt's 'QNetworkRequest
    QNetworkAccessManagerPrivate::prepareMultipart(const QNetworkRequest
    &request, QHttpMultiPart *multiPart)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanagerprivate.html#prepareMultipart

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

    QNetworkRequest
      A new cute QNetworkRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkRequest QNetworkAccessManagerPrivate::prepareMultipart(const
    #      QNetworkRequest &request, QHttpMultiPart *multiPart)
    address = self.uglySide.call(
        'ritual_ZN28QNetworkAccessManagerPrivate16prepareMultipartERK15QNet'
        'workRequestP14QHttpMultiPart',
        self._valueOf(request), self._addressOf(multiPart),
    )
    from . import QNetworkRequest
    return QNetworkRequest._cuteOwning(address)

  def q_func(self) -> Optional[QNetworkAccessManager]:
    """
    Calls Qt's 'QNetworkAccessManager
    *QNetworkAccessManagerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessmanagerprivate.html#q_func

    Returns
    -------

    Optional[QNetworkAccessManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkAccessManager *QNetworkAccessManagerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QNetworkAccessManagerPrivate6q_funcEv',
    )
    from . import QNetworkAccessManager
    return QNetworkAccessManager._cuteAt(address)

  @staticmethod
  def authenticationRequired(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkAccessManagerPrivate::authenticationRequired(QAuthenticator
    *authenticator, QNetworkReply *reply, bool synchronous, QUrl &url, QUrl
    *urlForLastAuthentication, bool allowAuthenticationReuse)': leans on
    'QNetworkAccessAuthenticationManager::cacheCredentials(QUrl const&,
    QAuthenticator const*)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkAccessManagerPrivate.authenticationRequired' has no cute "
        "function yet. Qt's 'void "
        "QNetworkAccessManagerPrivate::authenticationRequired(QAuthenticator"
        " *authenticator, QNetworkReply *reply, bool synchronous, QUrl "
        "&url, QUrl *urlForLastAuthentication, bool "
        "allowAuthenticationReuse)': leans on "
        "'QNetworkAccessAuthenticationManager::cacheCredentials(QUrl "
        "const&, QAuthenticator const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def backendSupportedSchemes(*__, **_) -> Never:
    """
    Qt's 'QStringList QNetworkAccessManagerPrivate::backendSupportedSchemes()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'QNetworkAccessBackendFactoryData'; did you mean
    'QNetworkAccessBackendFactory'?.
    """
    raise NotImplementedError(
        "'QNetworkAccessManagerPrivate.backendSupportedSchemes' has no cute "
        "function yet. Qt's 'QStringList "
        "QNetworkAccessManagerPrivate::backendSupportedSchemes() const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'QNetworkAccessBackendFactoryData'; did you mean "
        "'QNetworkAccessBackendFactory'?.")

  @staticmethod
  def cacheCredentials(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAccessManagerPrivate::cacheCredentials(const QUrl
    &url, const QAuthenticator *auth)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNetworkAccessManagerPrivate.cacheCredentials' has no cute "
        "function yet. Qt's 'void "
        "QNetworkAccessManagerPrivate::cacheCredentials(const QUrl &url, "
        "const QAuthenticator *auth)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def cacheProxyCredentials(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAccessManagerPrivate::cacheProxyCredentials(const
    QNetworkProxy &proxy, const QAuthenticator *auth)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNetworkAccessManagerPrivate.cacheProxyCredentials' has no cute "
        "function yet. Qt's 'void "
        "QNetworkAccessManagerPrivate::cacheProxyCredentials(const "
        "QNetworkProxy &proxy, const QAuthenticator *auth)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def clearAuthenticationCache(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAccessManagerPrivate::clearAuthenticationCache(
    QNetworkAccessManager *manager)': leans on
    'QNetworkAccessCache::clear()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkAccessManagerPrivate.clearAuthenticationCache' has no "
        "cute function yet. Qt's 'void "
        "QNetworkAccessManagerPrivate::clearAuthenticationCache(QNetworkAcce"
        "ssManager *manager)': leans on 'QNetworkAccessCache::clear()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def ensureBackendPluginsLoaded(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAccessManagerPrivate::ensureBackendPluginsLoaded()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'qnabfLoader'.
    """
    raise NotImplementedError(
        "'QNetworkAccessManagerPrivate.ensureBackendPluginsLoaded' has no "
        "cute function yet. Qt's 'void "
        "QNetworkAccessManagerPrivate::ensureBackendPluginsLoaded()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qnabfLoader'.")

  @staticmethod
  def fetchCachedCredentials(*__, **_) -> Never:
    """
    Qt's 'QNetworkAuthenticationCredential
    *QNetworkAccessManagerPrivate::fetchCachedCredentials(const QUrl &url,
    const QAuthenticator *auth)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNetworkAccessManagerPrivate.fetchCachedCredentials' has no cute "
        "function yet. Qt's 'QNetworkAuthenticationCredential "
        "*QNetworkAccessManagerPrivate::fetchCachedCredentials(const QUrl "
        "&url, const QAuthenticator *auth)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def fetchCachedProxyCredentials(*__, **_) -> Never:
    """
    Qt's 'QNetworkAuthenticationCredential
    *QNetworkAccessManagerPrivate::fetchCachedProxyCredentials(const
    QNetworkProxy &proxy, const QAuthenticator *auth)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QNetworkAccessManagerPrivate.fetchCachedProxyCredentials' has no "
        "cute function yet. Qt's 'QNetworkAuthenticationCredential "
        "*QNetworkAccessManagerPrivate::fetchCachedProxyCredentials(const "
        "QNetworkProxy &proxy, const QAuthenticator *auth)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def findBackend(*__, **_) -> Never:
    """
    Qt's 'QNetworkAccessBackend
    *QNetworkAccessManagerPrivate::findBackend(QNetworkAccessManager::
    Operation op, const QNetworkRequest &request)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'factoryData'.
    """
    raise NotImplementedError(
        "'QNetworkAccessManagerPrivate.findBackend' has no cute function "
        "yet. Qt's 'QNetworkAccessBackend "
        "*QNetworkAccessManagerPrivate::findBackend(QNetworkAccessManager::O"
        "peration op, const QNetworkRequest &request)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'factoryData'.")

  @staticmethod
  def proxyAuthenticationRequired(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkAccessManagerPrivate::proxyAuthenticationRequired(const QUrl
    &url, const QNetworkProxy &proxy, bool synchronous, QAuthenticator
    *authenticator, QNetworkProxy *lastProxyAuthentication)': leans on
    'QNetworkAccessAuthenticationManager::cacheProxyCredentials(QNetworkProxy
    const&, QAuthenticator const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkAccessManagerPrivate.proxyAuthenticationRequired' has no "
        "cute function yet. Qt's 'void "
        "QNetworkAccessManagerPrivate::proxyAuthenticationRequired(const "
        "QUrl &url, const QNetworkProxy &proxy, bool synchronous, "
        "QAuthenticator *authenticator, QNetworkProxy "
        "*lastProxyAuthentication)': leans on "
        "'QNetworkAccessAuthenticationManager::cacheProxyCredentials(QNetwor"
        "kProxy const&, QAuthenticator const*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
