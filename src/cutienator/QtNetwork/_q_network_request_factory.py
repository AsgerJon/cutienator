"""
QNetworkRequestFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkrequestfactory.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QNetworkRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QDebug, QUrl, QUrlQuery, QVariant
  from . import QHttpHeaders, QSslConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDebug = WAIT['QDebug']
  QHttpHeaders = WAIT['QHttpHeaders']
  QSslConfiguration = WAIT['QSslConfiguration']
  QUrl = WAIT['QUrl']
  QUrlQuery = WAIT['QUrlQuery']
  QVariant = WAIT['QVariant']


class QNetworkRequestFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkRequestFactory: a plain Python object
  standing in front of one C++ QNetworkRequestFactory.

  C++ hands a QNetworkRequestFactory around as a copy, so every C++
  QNetworkRequestFactory behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNetworkRequestFactory that has a ritual and that
  Python can call so far, 27 names in all: 'baseUrl', 'setBaseUrl',
  'sslConfiguration', 'setSslConfiguration', 'createRequest',
  'setCommonHeaders', 'commonHeaders', 'clearCommonHeaders', 'bearerToken',
  'setBearerToken', 'clearBearerToken', 'userName', 'setUserName',
  'clearUserName', 'password', 'setPassword', 'clearPassword',
  'queryParameters', 'setQueryParameters', 'clearQueryParameters',
  'setPriority', 'priority', 'attribute', 'setAttribute', 'clearAttribute',
  'clearAttributes', '__rlshift__'. It can be made from Python, in 3 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkRequestFactory::~QNetworkRequestFactory()': the destructor:
    Python removes its C++ QNetworkRequestFactory by it, and has no other use
    for it.
  - Qt's
    'QNetworkRequestFactory::QNetworkRequestFactory(QNetworkRequestFactory
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QNetworkRequestFactory &QNetworkRequestFactory::operator=(const
    QNetworkRequestFactory &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QNetworkRequestFactory
    &QNetworkRequestFactory::operator=(QNetworkRequestFactory &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QNetworkRequestFactory::swap(QNetworkRequestFactory &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void
    QNetworkRequestFactory::setTransferTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
  - Qt's 'std::chrono::milliseconds QNetworkRequestFactory::transferTimeout()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QNetworkRequestFactory is created at the first use, not by
    'QNetworkRequestFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkRequestFactory back gives a copy the ritual
    made for Python, in a new cute QNetworkRequestFactory.
  - Each name of Qt's QNetworkRequestFactory that has no cute function yet,
    'setTransferTimeout', 'swap', 'transferTimeout', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkRequestFactory'

  #  Qt's '~QNetworkRequestFactory()'. Naming it makes this a value class:
  #  Python owns every C++ QNetworkRequestFactory behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QNetworkRequestFactoryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def baseUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QNetworkRequestFactory::baseUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#baseUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QNetworkRequestFactory::baseUrl() const
    address = self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory7baseUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QNetworkRequestFactory::sslConfiguration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QNetworkRequestFactory::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory16sslConfigurationEv',
    )
    from . import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  @overload()
  def createRequest(self) -> QNetworkRequest:
    """
    Calls Qt's 'QNetworkRequest QNetworkRequestFactory::createRequest()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#createRequest

    Returns
    -------

    QNetworkRequest
      A new cute QNetworkRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkRequest QNetworkRequestFactory::createRequest() const
    address = self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory13createRequestEv',
    )
    return QNetworkRequest._cuteOwning(address)

  @overload(QUrlQuery)
  def createRequest(self, query: QUrlQuery) -> QNetworkRequest:
    """
    Calls Qt's 'QNetworkRequest QNetworkRequestFactory::createRequest(const
    QUrlQuery &query) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#createRequest

    Parameters
    ----------

    query : QUrlQuery
      Passed on as a value: Qt reads the C++ QUrlQuery, which stays Python's
      own.

    Returns
    -------

    QNetworkRequest
      A new cute QNetworkRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkRequest QNetworkRequestFactory::createRequest(const QUrlQuery
    #      &query) const
    address = self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory13createRequestERK9QUrlQuery',
        self._valueOf(query),
    )
    return QNetworkRequest._cuteOwning(address)

  @overload(str)
  def createRequest(self, path: str) -> QNetworkRequest:
    """
    Calls Qt's 'QNetworkRequest QNetworkRequestFactory::createRequest(const
    QString &path) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#createRequest

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QNetworkRequest
      A new cute QNetworkRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkRequest QNetworkRequestFactory::createRequest(const QString
    #      &path) const
    address = self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory13createRequestERK7QString', path,
    )
    return QNetworkRequest._cuteOwning(address)

  @overload(str, QUrlQuery)
  def createRequest(self, path: str, query: QUrlQuery) -> QNetworkRequest:
    """
    Calls Qt's 'QNetworkRequest QNetworkRequestFactory::createRequest(const
    QString &path, const QUrlQuery &query) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#createRequest

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    query : QUrlQuery
      Passed on as a value: Qt reads the C++ QUrlQuery, which stays Python's
      own.

    Returns
    -------

    QNetworkRequest
      A new cute QNetworkRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkRequest QNetworkRequestFactory::createRequest(const QString
    #      &path, const QUrlQuery &query) const
    address = self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory13createRequestERK7QStringRK9QUr'
        'lQuery',
        path, self._valueOf(query),
    )
    return QNetworkRequest._cuteOwning(address)

  def commonHeaders(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QNetworkRequestFactory::commonHeaders() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#commonHeaders

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QNetworkRequestFactory::commonHeaders() const
    address = self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory13commonHeadersEv',
    )
    from . import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  def bearerToken(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNetworkRequestFactory::bearerToken() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#bearerToken

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNetworkRequestFactory::bearerToken() const
    address = self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory11bearerTokenEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def userName(self) -> str:
    """
    Calls Qt's 'QString QNetworkRequestFactory::userName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#userName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkRequestFactory::userName() const
    return self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory8userNameEv',
    )

  def password(self) -> str:
    """
    Calls Qt's 'QString QNetworkRequestFactory::password() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#password

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkRequestFactory::password() const
    return self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory8passwordEv',
    )

  def queryParameters(self) -> QUrlQuery:
    """
    Calls Qt's 'QUrlQuery QNetworkRequestFactory::queryParameters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#queryParameters

    Returns
    -------

    QUrlQuery
      A new cute QUrlQuery around the copy Qt gave back. Python owns it.
    """
    #  QUrlQuery QNetworkRequestFactory::queryParameters() const
    address = self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory15queryParametersEv',
    )
    from ..QtCore import QUrlQuery
    return QUrlQuery._cuteOwning(address)

  def priority(self) -> QNetworkRequest.Priority:
    """
    Calls Qt's 'QNetworkRequest::Priority QNetworkRequestFactory::priority()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#priority

    Returns
    -------

    QNetworkRequest.Priority
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QNetworkRequest.Priority(number)' gives.
    """
    #  QNetworkRequest::Priority QNetworkRequestFactory::priority() const
    return QNetworkRequest.Priority(self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory8priorityEv',
    ))

  @overload(QNetworkRequest.Attribute)
  def attribute(self, attribute: QNetworkRequest.Attribute) -> QVariant:
    """
    Calls Qt's 'QVariant
    QNetworkRequestFactory::attribute(QNetworkRequest::Attribute attribute)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#attribute

    Parameters
    ----------

    attribute : QNetworkRequest.Attribute
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QNetworkRequestFactory::attribute(QNetworkRequest::Attribute
    #      attribute) const
    address = self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory9attributeEN15QNetworkRequest9At'
        'tributeE',
        attribute.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QNetworkRequest.Attribute, QVariant)
  def attribute(
      self,
      attribute: QNetworkRequest.Attribute,
      defaultValue: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QNetworkRequestFactory::attribute(QNetworkRequest::Attribute attribute,
    const QVariant &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#attribute

    Parameters
    ----------

    attribute : QNetworkRequest.Attribute
      Passed on as its number.

    defaultValue : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QNetworkRequestFactory::attribute(QNetworkRequest::Attribute
    #      attribute, const QVariant &defaultValue) const
    address = self.uglySide.call(
        'ritual_ZNK22QNetworkRequestFactory9attributeEN15QNetworkRequest9At'
        'tributeERK8QVariant',
        attribute.value, self._valueOf(defaultValue),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setBaseUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::setBaseUrl(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#setBaseUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QNetworkRequestFactory::setBaseUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory10setBaseUrlERK4QUrl',
        self._valueOf(url),
    )

  @overload(QSslConfiguration)
  def setSslConfiguration(self, configuration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::setSslConfiguration(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#setSslConfiguration

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QNetworkRequestFactory::setSslConfiguration(const
    #      QSslConfiguration &configuration)
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory19setSslConfigurationERK17QSslCon'
        'figuration',
        self._valueOf(configuration),
    )

  @overload(QHttpHeaders)
  def setCommonHeaders(self, headers: QHttpHeaders) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::setCommonHeaders(const
    QHttpHeaders &headers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#setCommonHeaders

    Parameters
    ----------

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.
    """
    #  void QNetworkRequestFactory::setCommonHeaders(const QHttpHeaders
    #      &headers)
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory16setCommonHeadersERK12QHttpHeade'
        'rs',
        self._valueOf(headers),
    )

  @overload(QByteArray)
  def setBearerToken(self, token: QByteArray) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::setBearerToken(const QByteArray
    &token)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#setBearerToken

    Parameters
    ----------

    token : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNetworkRequestFactory::setBearerToken(const QByteArray &token)
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory14setBearerTokenERK10QByteArray',
        self._valueOf(token),
    )

  @overload(str)
  def setUserName(self, userName: str) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::setUserName(const QString
    &userName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#setUserName

    Parameters
    ----------

    userName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkRequestFactory::setUserName(const QString &userName)
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory11setUserNameERK7QString',
        userName,
    )

  @overload(str)
  def setPassword(self, password: str) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::setPassword(const QString
    &password)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#setPassword

    Parameters
    ----------

    password : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkRequestFactory::setPassword(const QString &password)
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory11setPasswordERK7QString',
        password,
    )

  @overload(QUrlQuery)
  def setQueryParameters(self, query: QUrlQuery) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::setQueryParameters(const
    QUrlQuery &query)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#setQueryParameters

    Parameters
    ----------

    query : QUrlQuery
      Passed on as a value: Qt reads the C++ QUrlQuery, which stays Python's
      own.
    """
    #  void QNetworkRequestFactory::setQueryParameters(const QUrlQuery
    #      &query)
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory18setQueryParametersERK9QUrlQuery',
        self._valueOf(query),
    )

  @overload(QNetworkRequest.Priority)
  def setPriority(self, priority: QNetworkRequest.Priority) -> None:
    """
    Calls Qt's 'void
    QNetworkRequestFactory::setPriority(QNetworkRequest::Priority priority)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#setPriority

    Parameters
    ----------

    priority : QNetworkRequest.Priority
      Passed on as its number.
    """
    #  void QNetworkRequestFactory::setPriority(QNetworkRequest::Priority
    #      priority)
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory11setPriorityEN15QNetworkRequest8'
        'PriorityE',
        priority.value,
    )

  @overload(QNetworkRequest.Attribute, QVariant)
  def setAttribute(
      self,
      attribute: QNetworkRequest.Attribute,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkRequestFactory::setAttribute(QNetworkRequest::Attribute
    attribute, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#setAttribute

    Parameters
    ----------

    attribute : QNetworkRequest.Attribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QNetworkRequestFactory::setAttribute(QNetworkRequest::Attribute
    #      attribute, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory12setAttributeEN15QNetworkRequest'
        '9AttributeERK8QVariant',
        attribute.value, self._valueOf(value),
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
    Calls Qt's 'QDebug operator<<(QDebug debug, const QNetworkRequestFactory
    &reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#operator<<

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
    #  QDebug operator<<(QDebug debug, const QNetworkRequestFactory &reply)
    address = Rituals.call(
        'ritual_Zls6QDebugRK22QNetworkRequestFactory',
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
    Notes what was given, for Qt's
    'QNetworkRequestFactory::QNetworkRequestFactory()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#QNetworkRequestFactory
    """
    #  QNetworkRequestFactory::QNetworkRequestFactory()
    self._noteCreation(QNetworkRequestFactory, lambda: Rituals.call(
        'ritual_ZN22QNetworkRequestFactoryC1Ev',
    ))

  @overload(QUrl)
  def __init__(self, baseUrl: QUrl) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkRequestFactory::QNetworkRequestFactory(const QUrl &baseUrl)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#QNetworkRequestFactory

    Parameters
    ----------

    baseUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QNetworkRequestFactory::QNetworkRequestFactory(const QUrl &baseUrl)
    self._noteCreation(QNetworkRequestFactory, lambda: Rituals.call(
        'ritual_ZN22QNetworkRequestFactoryC1ERK4QUrl',
        self._valueOf(baseUrl),
    ))

  @overload(THIS)
  def __init__(self, other: QNetworkRequestFactory) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkRequestFactory::QNetworkRequestFactory(const
    QNetworkRequestFactory &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#QNetworkRequestFactory

    Parameters
    ----------

    other : QNetworkRequestFactory
      Passed on as a value: Qt reads the C++ QNetworkRequestFactory, which
      stays Python's own.
    """
    #  QNetworkRequestFactory::QNetworkRequestFactory(const
    #      QNetworkRequestFactory &other)
    self._noteCreation(QNetworkRequestFactory, lambda: Rituals.call(
        'ritual_ZN22QNetworkRequestFactoryC1ERKS_', self._valueOf(other),
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

  def clearCommonHeaders(self) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::clearCommonHeaders()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#clearCommonHeaders
    """
    #  void QNetworkRequestFactory::clearCommonHeaders()
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory18clearCommonHeadersEv',
    )

  def clearBearerToken(self) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::clearBearerToken()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#clearBearerToken
    """
    #  void QNetworkRequestFactory::clearBearerToken()
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory16clearBearerTokenEv',
    )

  def clearUserName(self) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::clearUserName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#clearUserName
    """
    #  void QNetworkRequestFactory::clearUserName()
    self.uglySide.call('ritual_ZN22QNetworkRequestFactory13clearUserNameEv')

  def clearPassword(self) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::clearPassword()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#clearPassword
    """
    #  void QNetworkRequestFactory::clearPassword()
    self.uglySide.call('ritual_ZN22QNetworkRequestFactory13clearPasswordEv')

  def clearQueryParameters(self) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::clearQueryParameters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#clearQueryParameters
    """
    #  void QNetworkRequestFactory::clearQueryParameters()
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory20clearQueryParametersEv',
    )

  @overload(QNetworkRequest.Attribute)
  def clearAttribute(self, attribute: QNetworkRequest.Attribute) -> None:
    """
    Calls Qt's 'void
    QNetworkRequestFactory::clearAttribute(QNetworkRequest::Attribute
    attribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#clearAttribute

    Parameters
    ----------

    attribute : QNetworkRequest.Attribute
      Passed on as its number.
    """
    #  void QNetworkRequestFactory::clearAttribute(QNetworkRequest::Attribute
    #      attribute)
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory14clearAttributeEN15QNetworkReque'
        'st9AttributeE',
        attribute.value,
    )

  def clearAttributes(self) -> None:
    """
    Calls Qt's 'void QNetworkRequestFactory::clearAttributes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactory.html#clearAttributes
    """
    #  void QNetworkRequestFactory::clearAttributes()
    self.uglySide.call(
        'ritual_ZN22QNetworkRequestFactory15clearAttributesEv',
    )

  @staticmethod
  def setTransferTimeout(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkRequestFactory::setTransferTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkRequestFactory.setTransferTimeout' has no cute function "
        "yet. Qt's 'void "
        "QNetworkRequestFactory::setTransferTimeout(std::chrono::millisecond"
        "s timeout)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QNetworkRequestFactory::swap(QNetworkRequestFactory &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkRequestFactory.swap' has no cute function yet. Qt's 'void "
        "QNetworkRequestFactory::swap(QNetworkRequestFactory &other)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def transferTimeout(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds QNetworkRequestFactory::transferTimeout()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkRequestFactory.transferTimeout' has no cute function yet. "
        "Qt's 'std::chrono::milliseconds "
        "QNetworkRequestFactory::transferTimeout() const': gives a type "
        "Python has no way to take yet.")
