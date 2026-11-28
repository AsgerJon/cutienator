"""
QOpcUaClient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaclient.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QString, QUrl
  from . import QOpcUaAddNodeItem, QOpcUaAddReferenceItem
  from . import QOpcUaApplicationDescription, QOpcUaApplicationIdentity
  from . import QOpcUaAuthenticationInformation, QOpcUaClientImpl
  from . import QOpcUaClientPrivate, QOpcUaConnectionSettings
  from . import QOpcUaDeleteReferenceItem, QOpcUaEndpointDescription
  from . import QOpcUaErrorState, QOpcUaExpandedNodeId
  from . import QOpcUaHistoryReadEventRequest, QOpcUaHistoryReadRawRequest
  from . import QOpcUaHistoryReadResponse, QOpcUaNode, QOpcUaPkiConfiguration
  from . import QOpcUaReadItem, QOpcUaReadResult, QOpcUaWriteItem
  from . import QOpcUaWriteResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaAddNodeItem = WAIT['QOpcUaAddNodeItem']
  QOpcUaAddReferenceItem = WAIT['QOpcUaAddReferenceItem']
  QOpcUaApplicationDescription = WAIT['QOpcUaApplicationDescription']
  QOpcUaApplicationIdentity = WAIT['QOpcUaApplicationIdentity']
  QOpcUaAuthenticationInformation = WAIT['QOpcUaAuthenticationInformation']
  QOpcUaClientImpl = WAIT['QOpcUaClientImpl']
  QOpcUaConnectionSettings = WAIT['QOpcUaConnectionSettings']
  QOpcUaDeleteReferenceItem = WAIT['QOpcUaDeleteReferenceItem']
  QOpcUaEndpointDescription = WAIT['QOpcUaEndpointDescription']
  QOpcUaErrorState = WAIT['QOpcUaErrorState']
  QOpcUaExpandedNodeId = WAIT['QOpcUaExpandedNodeId']
  QOpcUaHistoryReadEventRequest = WAIT['QOpcUaHistoryReadEventRequest']
  QOpcUaHistoryReadRawRequest = WAIT['QOpcUaHistoryReadRawRequest']
  QOpcUaPkiConfiguration = WAIT['QOpcUaPkiConfiguration']
  QOpcUaReadItem = WAIT['QOpcUaReadItem']
  QOpcUaReadResult = WAIT['QOpcUaReadResult']
  QOpcUaWriteItem = WAIT['QOpcUaWriteItem']
  QOpcUaWriteResult = WAIT['QOpcUaWriteResult']
  QString = WAIT['QString']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaClient(QObject):
  """
  The cute side of Qt's QOpcUaClient: a plain Python object standing in front
  of one C++ QOpcUaClient.

  It is built on the cute 'QObject', as Qt's QOpcUaClient is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaClient that has a ritual and that Python can
  call so far, 55 names in all: 'metaObject', 'tr', 'd_func',
  'setApplicationIdentity', 'applicationIdentity', 'setPkiConfiguration',
  'pkiConfiguration', 'connectToEndpoint', 'disconnectFromEndpoint', 'node',
  'updateNamespaceArray', 'namespaceArray', 'requestEndpoints',
  'findServers', 'readNodeAttributes', 'writeNodeAttributes', 'addNode',
  'deleteNode', 'addReference', 'deleteReference', 'endpoint', 'state',
  'error', 'backend', 'setNamespaceAutoupdate',
  'isNamespaceAutoupdateEnabled', 'setNamespaceAutoupdateInterval',
  'namespaceAutoupdateInterval', 'setAuthenticationInformation',
  'authenticationInformation', 'setConnectionSettings', 'connectionSettings',
  'supportedSecurityPolicies', 'readHistoryData', 'readHistoryEvents',
  'registerNodes', 'unregisterNodes', 'connected', 'disconnected',
  'stateChanged', 'errorChanged', 'connectError', 'namespaceArrayUpdated',
  'namespaceArrayChanged', 'endpointsRequestFinished', 'findServersFinished',
  'readNodeAttributesFinished', 'writeNodeAttributesFinished',
  'addNodeFinished', 'deleteNodeFinished', 'addReferenceFinished',
  'deleteReferenceFinished', 'passwordForPrivateKeyRequired',
  'registerNodesFinished', 'unregisterNodesFinished'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpcUaClient::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QOpcUaClient::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QOpcUaClientPrivate *QOpcUaClient::d_func() const': takes in
    Python what 'QOpcUaClientPrivate *QOpcUaClient::d_func()' takes.
  - Qt's 'QOpcUaClient::~QOpcUaClient()': the destructor: Python never
    removes a C++ QOpcUaClient.
  - Qt's 'QString QOpcUaClient::resolveExpandedNodeId(const
    QOpcUaExpandedNodeId &expandedNodeId, bool *ok) const': takes a number to
    change where it is.
  - Qt's 'QOpcUaQualifiedName
    QOpcUaClient::qualifiedNameFromNamespaceUri(const QString &namespaceUri,
    const QString &name, bool *ok) const': takes a number to change where it
    is.
  - Qt's 'QList<QOpcUaUserTokenPolicy::TokenType>
    QOpcUaClient::supportedUserTokenTypes() const': gives a type Python has
    no way to take yet.

  What has no ritual
  ------------------

  4 of the 68 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpcUaClient is created at the first use, not by
    'QOpcUaClient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaClient.
  - Qt tells when it has removed the C++ QOpcUaClient. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QOpcUaClient that has no cute function yet,
    'qualifiedNameFromNamespaceUri', 'resolveExpandedNodeId',
    'supportedUserTokenTypes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaClient, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ClientError(CuteNum):
    """
    The enum 'QOpcUaClient::ClientError' of Qt, with the 12 names Qt gives in
    it.
    """

    NoError = Kee[int](0)
    InvalidUrl = Kee[int](1)
    AccessDenied = Kee[int](2)
    ConnectionError = Kee[int](3)
    UnknownError = Kee[int](4)
    UnsupportedAuthenticationInformation = Kee[int](5)
    InvalidAuthenticationInformation = Kee[int](6)
    InvalidEndpointDescription = Kee[int](7)
    NoMatchingUserIdentityTokenFound = Kee[int](8)
    UnsupportedSecurityPolicy = Kee[int](9)
    InvalidPki = Kee[int](10)
    CertificateUntrusted = Kee[int](11)

  class ClientState(CuteNum):
    """
    The enum 'QOpcUaClient::ClientState' of Qt, with the 4 names Qt gives in
    it.
    """

    Disconnected = Kee[int](0)
    Connecting = Kee[int](1)
    Connected = Kee[int](2)
    Closing = Kee[int](3)

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
    Calls Qt's 'QString QOpcUaClient::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#tr

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
    #  QString QOpcUaClient::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QOpcUaClient2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaClient'

  #  A C++ QOpcUaClient Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpcUaClient'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpcUaClient::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpcUaClient::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QOpcUaClient10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def applicationIdentity(self) -> QOpcUaApplicationIdentity:
    """
    Calls Qt's 'QOpcUaApplicationIdentity QOpcUaClient::applicationIdentity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#applicationIdentity

    Returns
    -------

    QOpcUaApplicationIdentity
      A new cute QOpcUaApplicationIdentity around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaApplicationIdentity QOpcUaClient::applicationIdentity() const
    address = self.uglySide.call(
        'ritual_ZNK12QOpcUaClient19applicationIdentityEv',
    )
    from . import QOpcUaApplicationIdentity
    return QOpcUaApplicationIdentity._cuteOwning(address)

  def pkiConfiguration(self) -> QOpcUaPkiConfiguration:
    """
    Calls Qt's 'QOpcUaPkiConfiguration QOpcUaClient::pkiConfiguration()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#pkiConfiguration

    Returns
    -------

    QOpcUaPkiConfiguration
      A new cute QOpcUaPkiConfiguration around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaPkiConfiguration QOpcUaClient::pkiConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK12QOpcUaClient16pkiConfigurationEv',
    )
    from . import QOpcUaPkiConfiguration
    return QOpcUaPkiConfiguration._cuteOwning(address)

  def namespaceArray(self) -> QStringList:
    """
    Calls Qt's 'QStringList QOpcUaClient::namespaceArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#namespaceArray

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QOpcUaClient::namespaceArray() const
    address = self.uglySide.call(
        'ritual_ZNK12QOpcUaClient14namespaceArrayEv',
    )
    return QStringList._cuteOwning(address)

  def endpoint(self) -> QOpcUaEndpointDescription:
    """
    Calls Qt's 'QOpcUaEndpointDescription QOpcUaClient::endpoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#endpoint

    Returns
    -------

    QOpcUaEndpointDescription
      A new cute QOpcUaEndpointDescription around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaEndpointDescription QOpcUaClient::endpoint() const
    address = self.uglySide.call('ritual_ZNK12QOpcUaClient8endpointEv')
    from . import QOpcUaEndpointDescription
    return QOpcUaEndpointDescription._cuteOwning(address)

  def state(self) -> ClientState:
    """
    Calls Qt's 'ClientState QOpcUaClient::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#state

    Returns
    -------

    ClientState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ClientState(number)'
      gives.
    """
    #  ClientState QOpcUaClient::state() const
    return QOpcUaClient.ClientState(self.uglySide.call(
        'ritual_ZNK12QOpcUaClient5stateEv',
    ))

  def error(self) -> ClientError:
    """
    Calls Qt's 'ClientError QOpcUaClient::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#error

    Returns
    -------

    ClientError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ClientError(number)'
      gives.
    """
    #  ClientError QOpcUaClient::error() const
    return QOpcUaClient.ClientError(self.uglySide.call(
        'ritual_ZNK12QOpcUaClient5errorEv',
    ))

  def backend(self) -> str:
    """
    Calls Qt's 'QString QOpcUaClient::backend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#backend

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaClient::backend() const
    return self.uglySide.call('ritual_ZNK12QOpcUaClient7backendEv')

  def isNamespaceAutoupdateEnabled(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaClient::isNamespaceAutoupdateEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#isNamespaceAutoupdateEnabled
    """
    #  bool QOpcUaClient::isNamespaceAutoupdateEnabled() const
    return self.uglySide.call(
        'ritual_ZNK12QOpcUaClient28isNamespaceAutoupdateEnabledEv',
    )

  def namespaceAutoupdateInterval(self) -> int:
    """
    Calls Qt's 'int QOpcUaClient::namespaceAutoupdateInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#namespaceAutoupdateInterval
    """
    #  int QOpcUaClient::namespaceAutoupdateInterval() const
    return self.uglySide.call(
        'ritual_ZNK12QOpcUaClient27namespaceAutoupdateIntervalEv',
    )

  def authenticationInformation(self) -> QOpcUaAuthenticationInformation:
    """
    Calls Qt's 'const QOpcUaAuthenticationInformation
    &QOpcUaClient::authenticationInformation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#authenticationInformation

    Returns
    -------

    QOpcUaAuthenticationInformation
      A new cute QOpcUaAuthenticationInformation around the copy Qt gave
      back. Python owns it.
    """
    #  const QOpcUaAuthenticationInformation
    #      &QOpcUaClient::authenticationInformation() const
    address = self.uglySide.call(
        'ritual_ZNK12QOpcUaClient25authenticationInformationEv',
    )
    from . import QOpcUaAuthenticationInformation
    return QOpcUaAuthenticationInformation._cuteOwning(address)

  def connectionSettings(self) -> QOpcUaConnectionSettings:
    """
    Calls Qt's 'QOpcUaConnectionSettings QOpcUaClient::connectionSettings()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#connectionSettings

    Returns
    -------

    QOpcUaConnectionSettings
      A new cute QOpcUaConnectionSettings around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaConnectionSettings QOpcUaClient::connectionSettings() const
    address = self.uglySide.call(
        'ritual_ZNK12QOpcUaClient18connectionSettingsEv',
    )
    from . import QOpcUaConnectionSettings
    return QOpcUaConnectionSettings._cuteOwning(address)

  def supportedSecurityPolicies(self) -> QStringList:
    """
    Calls Qt's 'QStringList QOpcUaClient::supportedSecurityPolicies() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#supportedSecurityPolicies

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QOpcUaClient::supportedSecurityPolicies() const
    address = self.uglySide.call(
        'ritual_ZNK12QOpcUaClient25supportedSecurityPoliciesEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpcUaApplicationIdentity)
  def setApplicationIdentity(
      self,
      identity: QOpcUaApplicationIdentity,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClient::setApplicationIdentity(const
    QOpcUaApplicationIdentity &identity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#setApplicationIdentity

    Parameters
    ----------

    identity : QOpcUaApplicationIdentity
      Passed on as a value: Qt reads the C++ QOpcUaApplicationIdentity, which
      stays Python's own.
    """
    #  void QOpcUaClient::setApplicationIdentity(const
    #      QOpcUaApplicationIdentity &identity)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient22setApplicationIdentityERK25QOpcUaApplicat'
        'ionIdentity',
        self._valueOf(identity),
    )

  @overload(QOpcUaPkiConfiguration)
  def setPkiConfiguration(self, config: QOpcUaPkiConfiguration) -> None:
    """
    Calls Qt's 'void QOpcUaClient::setPkiConfiguration(const
    QOpcUaPkiConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#setPkiConfiguration

    Parameters
    ----------

    config : QOpcUaPkiConfiguration
      Passed on as a value: Qt reads the C++ QOpcUaPkiConfiguration, which
      stays Python's own.
    """
    #  void QOpcUaClient::setPkiConfiguration(const QOpcUaPkiConfiguration
    #      &config)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient19setPkiConfigurationERK22QOpcUaPkiConfigur'
        'ation',
        self._valueOf(config),
    )

  @overload(bool)
  def setNamespaceAutoupdate(self, isEnabled: bool) -> None:
    """
    Calls Qt's 'void QOpcUaClient::setNamespaceAutoupdate(bool isEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#setNamespaceAutoupdate

    Parameters
    ----------

    isEnabled : bool
      Passed on as it is.
    """
    #  void QOpcUaClient::setNamespaceAutoupdate(bool isEnabled)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient22setNamespaceAutoupdateEb', isEnabled,
    )

  @overload(int)
  def setNamespaceAutoupdateInterval(self, interval: int) -> None:
    """
    Calls Qt's 'void QOpcUaClient::setNamespaceAutoupdateInterval(int
    interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#setNamespaceAutoupdateInterval

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void QOpcUaClient::setNamespaceAutoupdateInterval(int interval)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient30setNamespaceAutoupdateIntervalEi',
        interval,
    )

  @overload(QOpcUaAuthenticationInformation)
  def setAuthenticationInformation(
      self,
      authenticationInformation: QOpcUaAuthenticationInformation,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClient::setAuthenticationInformation(const
    QOpcUaAuthenticationInformation &authenticationInformation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#setAuthenticationInformation

    Parameters
    ----------

    authenticationInformation : QOpcUaAuthenticationInformation
      Passed on as a value: Qt reads the C++ QOpcUaAuthenticationInformation,
      which stays Python's own.
    """
    #  void QOpcUaClient::setAuthenticationInformation(const
    #      QOpcUaAuthenticationInformation &authenticationInformation)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient28setAuthenticationInformationERK31QOpcUaAu'
        'thenticationInformation',
        self._valueOf(authenticationInformation),
    )

  @overload(QOpcUaConnectionSettings)
  def setConnectionSettings(
      self,
      connectionSettings: QOpcUaConnectionSettings,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClient::setConnectionSettings(const
    QOpcUaConnectionSettings &connectionSettings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#setConnectionSettings

    Parameters
    ----------

    connectionSettings : QOpcUaConnectionSettings
      Passed on as a value: Qt reads the C++ QOpcUaConnectionSettings, which
      stays Python's own.
    """
    #  void QOpcUaClient::setConnectionSettings(const
    #      QOpcUaConnectionSettings &connectionSettings)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient21setConnectionSettingsERK24QOpcUaConnectio'
        'nSettings',
        self._valueOf(connectionSettings),
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

  @overload(QOpcUaClientImpl)
  @overload(NoneType)
  @overload(QOpcUaClientImpl, QObject)
  @overload(QOpcUaClientImpl, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      impl: Optional[QOpcUaClientImpl],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaClient::QOpcUaClient(QOpcUaClientImpl *impl, QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#QOpcUaClient

    Parameters
    ----------

    impl : Optional[QOpcUaClientImpl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpcUaClient::QOpcUaClient(QOpcUaClientImpl *impl, QObject *parent)
    self._noteCreation(QOpcUaClient, lambda: Rituals.call(
        'ritual_ZN12QOpcUaClientC1EP16QOpcUaClientImplP7QObject',
        self._addressOf(impl), self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QOpcUaClientPrivate]:
    """
    Calls Qt's 'QOpcUaClientPrivate *QOpcUaClient::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#d_func

    Returns
    -------

    Optional[QOpcUaClientPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaClientPrivate *QOpcUaClient::d_func()
    address = self.uglySide.call('ritual_ZN12QOpcUaClient6d_funcEv')
    from . import QOpcUaClientPrivate
    return QOpcUaClientPrivate._cuteAt(address)

  @overload(QOpcUaEndpointDescription)
  def connectToEndpoint(self, endpoint: QOpcUaEndpointDescription) -> None:
    """
    Calls Qt's 'void QOpcUaClient::connectToEndpoint(const
    QOpcUaEndpointDescription &endpoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#connectToEndpoint

    Parameters
    ----------

    endpoint : QOpcUaEndpointDescription
      Passed on as a value: Qt reads the C++ QOpcUaEndpointDescription, which
      stays Python's own.
    """
    #  void QOpcUaClient::connectToEndpoint(const QOpcUaEndpointDescription
    #      &endpoint)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient17connectToEndpointERK25QOpcUaEndpointDescr'
        'iption',
        self._valueOf(endpoint),
    )

  def disconnectFromEndpoint(self) -> None:
    """
    Calls Qt's 'void QOpcUaClient::disconnectFromEndpoint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#disconnectFromEndpoint
    """
    #  void QOpcUaClient::disconnectFromEndpoint()
    self.uglySide.call('ritual_ZN12QOpcUaClient22disconnectFromEndpointEv')

  @overload(str)
  def node(self, nodeId: str) -> Optional[QOpcUaNode]:
    """
    Calls Qt's 'QOpcUaNode *QOpcUaClient::node(const QString &nodeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#node

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QOpcUaNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaNode *QOpcUaClient::node(const QString &nodeId)
    address = self.uglySide.call(
        'ritual_ZN12QOpcUaClient4nodeERK7QString', nodeId,
    )
    from . import QOpcUaNode
    return QOpcUaNode._cuteAt(address)

  @overload(QOpcUaExpandedNodeId)
  def node(
      self,
      expandedNodeId: QOpcUaExpandedNodeId,
  ) -> Optional[QOpcUaNode]:
    """
    Calls Qt's 'QOpcUaNode *QOpcUaClient::node(const QOpcUaExpandedNodeId
    &expandedNodeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#node

    Parameters
    ----------

    expandedNodeId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.

    Returns
    -------

    Optional[QOpcUaNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaNode *QOpcUaClient::node(const QOpcUaExpandedNodeId
    #      &expandedNodeId)
    address = self.uglySide.call(
        'ritual_ZN12QOpcUaClient4nodeERK20QOpcUaExpandedNodeId',
        self._valueOf(expandedNodeId),
    )
    from . import QOpcUaNode
    return QOpcUaNode._cuteAt(address)

  def updateNamespaceArray(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaClient::updateNamespaceArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#updateNamespaceArray
    """
    #  bool QOpcUaClient::updateNamespaceArray()
    return self.uglySide.call(
        'ritual_ZN12QOpcUaClient20updateNamespaceArrayEv',
    )

  @overload(QUrl)
  def requestEndpoints(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QOpcUaClient::requestEndpoints(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#requestEndpoints

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QOpcUaClient::requestEndpoints(const QUrl &url)
    return self.uglySide.call(
        'ritual_ZN12QOpcUaClient16requestEndpointsERK4QUrl',
        self._valueOf(url),
    )

  @overload(QUrl, QStringList, QStringList)
  def findServers(
      self,
      url: QUrl,
      localeIds: QStringList,
      serverUris: QStringList,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaClient::findServers(const QUrl &url, const
    QStringList &localeIds, const QStringList &serverUris)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#findServers

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    localeIds : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serverUris : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QOpcUaClient::findServers(const QUrl &url, const QStringList
    #      &localeIds, const QStringList &serverUris)
    return self.uglySide.call(
        'ritual_ZN12QOpcUaClient11findServersERK4QUrlRK5QListI7QStringES7_',
        self._valueOf(url), self._valueOf(localeIds),
        self._valueOf(serverUris),
    )

  @overload(QList[QOpcUaReadItem])
  def readNodeAttributes(self, nodesToRead: QList[QOpcUaReadItem]) -> bool:
    """
    Calls Qt's 'bool QOpcUaClient::readNodeAttributes(const
    QList<QOpcUaReadItem> &nodesToRead)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#readNodeAttributes

    Parameters
    ----------

    nodesToRead : QList[QOpcUaReadItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QOpcUaClient::readNodeAttributes(const QList<QOpcUaReadItem>
    #      &nodesToRead)
    return self.uglySide.call(
        'ritual_ZN12QOpcUaClient18readNodeAttributesERK5QListI14QOpcUaReadI'
        'temE',
        self._valueOf(nodesToRead),
    )

  @overload(QList[QOpcUaWriteItem])
  def writeNodeAttributes(
      self,
      nodesToWrite: QList[QOpcUaWriteItem],
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaClient::writeNodeAttributes(const
    QList<QOpcUaWriteItem> &nodesToWrite)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#writeNodeAttributes

    Parameters
    ----------

    nodesToWrite : QList[QOpcUaWriteItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QOpcUaClient::writeNodeAttributes(const QList<QOpcUaWriteItem>
    #      &nodesToWrite)
    return self.uglySide.call(
        'ritual_ZN12QOpcUaClient19writeNodeAttributesERK5QListI15QOpcUaWrit'
        'eItemE',
        self._valueOf(nodesToWrite),
    )

  @overload(QOpcUaAddNodeItem)
  def addNode(self, nodeToAdd: QOpcUaAddNodeItem) -> bool:
    """
    Calls Qt's 'bool QOpcUaClient::addNode(const QOpcUaAddNodeItem
    &nodeToAdd)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#addNode

    Parameters
    ----------

    nodeToAdd : QOpcUaAddNodeItem
      Passed on as a value: Qt reads the C++ QOpcUaAddNodeItem, which stays
      Python's own.
    """
    #  bool QOpcUaClient::addNode(const QOpcUaAddNodeItem &nodeToAdd)
    return self.uglySide.call(
        'ritual_ZN12QOpcUaClient7addNodeERK17QOpcUaAddNodeItem',
        self._valueOf(nodeToAdd),
    )

  @overload(str)
  @overload(str, bool)
  def deleteNode(
      self,
      nodeId: str,
      deleteTargetReferences: bool = True,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaClient::deleteNode(const QString &nodeId, bool
    deleteTargetReferences)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#deleteNode

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.

    deleteTargetReferences : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  bool QOpcUaClient::deleteNode(const QString &nodeId, bool
    #      deleteTargetReferences)
    return self.uglySide.call(
        'ritual_ZN12QOpcUaClient10deleteNodeERK7QStringb',
        nodeId, deleteTargetReferences,
    )

  @overload(QOpcUaAddReferenceItem)
  def addReference(self, referenceToAdd: QOpcUaAddReferenceItem) -> bool:
    """
    Calls Qt's 'bool QOpcUaClient::addReference(const QOpcUaAddReferenceItem
    &referenceToAdd)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#addReference

    Parameters
    ----------

    referenceToAdd : QOpcUaAddReferenceItem
      Passed on as a value: Qt reads the C++ QOpcUaAddReferenceItem, which
      stays Python's own.
    """
    #  bool QOpcUaClient::addReference(const QOpcUaAddReferenceItem
    #      &referenceToAdd)
    return self.uglySide.call(
        'ritual_ZN12QOpcUaClient12addReferenceERK22QOpcUaAddReferenceItem',
        self._valueOf(referenceToAdd),
    )

  @overload(QOpcUaDeleteReferenceItem)
  def deleteReference(
      self,
      referenceToDelete: QOpcUaDeleteReferenceItem,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaClient::deleteReference(const
    QOpcUaDeleteReferenceItem &referenceToDelete)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#deleteReference

    Parameters
    ----------

    referenceToDelete : QOpcUaDeleteReferenceItem
      Passed on as a value: Qt reads the C++ QOpcUaDeleteReferenceItem, which
      stays Python's own.
    """
    #  bool QOpcUaClient::deleteReference(const QOpcUaDeleteReferenceItem
    #      &referenceToDelete)
    return self.uglySide.call(
        'ritual_ZN12QOpcUaClient15deleteReferenceERK25QOpcUaDeleteReference'
        'Item',
        self._valueOf(referenceToDelete),
    )

  @overload(QOpcUaHistoryReadRawRequest)
  def readHistoryData(
      self,
      request: QOpcUaHistoryReadRawRequest,
  ) -> Optional[QOpcUaHistoryReadResponse]:
    """
    Calls Qt's 'QOpcUaHistoryReadResponse
    *QOpcUaClient::readHistoryData(const QOpcUaHistoryReadRawRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#readHistoryData

    Parameters
    ----------

    request : QOpcUaHistoryReadRawRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadRawRequest,
      which stays Python's own.

    Returns
    -------

    Optional[QOpcUaHistoryReadResponse]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaHistoryReadResponse *QOpcUaClient::readHistoryData(const
    #      QOpcUaHistoryReadRawRequest &request)
    address = self.uglySide.call(
        'ritual_ZN12QOpcUaClient15readHistoryDataERK27QOpcUaHistoryReadRawR'
        'equest',
        self._valueOf(request),
    )
    from . import QOpcUaHistoryReadResponse
    return QOpcUaHistoryReadResponse._cuteAt(address)

  @overload(QOpcUaHistoryReadEventRequest)
  def readHistoryEvents(
      self,
      request: QOpcUaHistoryReadEventRequest,
  ) -> Optional[QOpcUaHistoryReadResponse]:
    """
    Calls Qt's 'QOpcUaHistoryReadResponse
    *QOpcUaClient::readHistoryEvents(const QOpcUaHistoryReadEventRequest
    &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#readHistoryEvents

    Parameters
    ----------

    request : QOpcUaHistoryReadEventRequest
      Passed on as a value: Qt reads the C++ QOpcUaHistoryReadEventRequest,
      which stays Python's own.

    Returns
    -------

    Optional[QOpcUaHistoryReadResponse]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpcUaHistoryReadResponse *QOpcUaClient::readHistoryEvents(const
    #      QOpcUaHistoryReadEventRequest &request)
    address = self.uglySide.call(
        'ritual_ZN12QOpcUaClient17readHistoryEventsERK29QOpcUaHistoryReadEv'
        'entRequest',
        self._valueOf(request),
    )
    from . import QOpcUaHistoryReadResponse
    return QOpcUaHistoryReadResponse._cuteAt(address)

  @overload(QStringList)
  def registerNodes(self, nodesToRegister: QStringList) -> bool:
    """
    Calls Qt's 'bool QOpcUaClient::registerNodes(const QStringList
    &nodesToRegister)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#registerNodes

    Parameters
    ----------

    nodesToRegister : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QOpcUaClient::registerNodes(const QStringList &nodesToRegister)
    return self.uglySide.call(
        'ritual_ZN12QOpcUaClient13registerNodesERK5QListI7QStringE',
        self._valueOf(nodesToRegister),
    )

  @overload(QStringList)
  def unregisterNodes(self, nodesToUnregister: QStringList) -> bool:
    """
    Calls Qt's 'bool QOpcUaClient::unregisterNodes(const QStringList
    &nodesToUnregister)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#unregisterNodes

    Parameters
    ----------

    nodesToUnregister : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QOpcUaClient::unregisterNodes(const QStringList
    #      &nodesToUnregister)
    return self.uglySide.call(
        'ritual_ZN12QOpcUaClient15unregisterNodesERK5QListI7QStringE',
        self._valueOf(nodesToUnregister),
    )

  def connected(self) -> None:
    """
    Calls Qt's 'void QOpcUaClient::connected()'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#connected
    """
    #  void QOpcUaClient::connected()
    self.uglySide.call('ritual_ZN12QOpcUaClient9connectedEv')

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QOpcUaClient::disconnected()'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#disconnected
    """
    #  void QOpcUaClient::disconnected()
    self.uglySide.call('ritual_ZN12QOpcUaClient12disconnectedEv')

  @overload(ClientState)
  def stateChanged(self, state: ClientState) -> None:
    """
    Calls Qt's 'void QOpcUaClient::stateChanged(QOpcUaClient::ClientState
    state)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#stateChanged

    Parameters
    ----------

    state : ClientState
      Passed on as its number.
    """
    #  void QOpcUaClient::stateChanged(QOpcUaClient::ClientState state)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient12stateChangedENS_11ClientStateE',
        state.value,
    )

  @overload(ClientError)
  def errorChanged(self, error: ClientError) -> None:
    """
    Calls Qt's 'void QOpcUaClient::errorChanged(QOpcUaClient::ClientError
    error)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#errorChanged

    Parameters
    ----------

    error : ClientError
      Passed on as its number.
    """
    #  void QOpcUaClient::errorChanged(QOpcUaClient::ClientError error)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient12errorChangedENS_11ClientErrorE',
        error.value,
    )

  @overload(QOpcUaErrorState)
  @overload(NoneType)
  def connectError(self, errorState: Optional[QOpcUaErrorState]) -> None:
    """
    Calls Qt's 'void QOpcUaClient::connectError(QOpcUaErrorState
    *errorState)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#connectError

    Parameters
    ----------

    errorState : Optional[QOpcUaErrorState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpcUaClient::connectError(QOpcUaErrorState *errorState)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient12connectErrorEP16QOpcUaErrorState',
        self._addressOf(errorState),
    )

  @overload(QStringList)
  def namespaceArrayUpdated(self, namespaces: QStringList) -> None:
    """
    Calls Qt's 'void QOpcUaClient::namespaceArrayUpdated(QStringList
    namespaces)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#namespaceArrayUpdated

    Parameters
    ----------

    namespaces : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaClient::namespaceArrayUpdated(QStringList namespaces)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient21namespaceArrayUpdatedE5QListI7QStringE',
        self._valueOf(namespaces),
    )

  @overload(QStringList)
  def namespaceArrayChanged(self, namespaces: QStringList) -> None:
    """
    Calls Qt's 'void QOpcUaClient::namespaceArrayChanged(QStringList
    namespaces)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#namespaceArrayChanged

    Parameters
    ----------

    namespaces : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaClient::namespaceArrayChanged(QStringList namespaces)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient21namespaceArrayChangedE5QListI7QStringE',
        self._valueOf(namespaces),
    )

  @overload(QList[QOpcUaEndpointDescription], QOpcUa.UaStatusCode, QUrl)
  def endpointsRequestFinished(
      self,
      endpoints: QList[QOpcUaEndpointDescription],
      statusCode: QOpcUa.UaStatusCode,
      requestUrl: QUrl,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaClient::endpointsRequestFinished(QList<QOpcUaEndpointDescription>
    endpoints, QOpcUa::UaStatusCode statusCode, QUrl requestUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#endpointsRequestFinished

    Parameters
    ----------

    endpoints : QList[QOpcUaEndpointDescription]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.

    requestUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOpcUaClient::endpointsRequestFinished(
    #      QList<QOpcUaEndpointDescription> endpoints, QOpcUa::UaStatusCode
    #      statusCode, QUrl requestUrl)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient24endpointsRequestFinishedE5QListI25QOpcUaE'
        'ndpointDescriptionEN6QOpcUa12UaStatusCodeE4QUrl',
        self._valueOf(endpoints), statusCode.value,
        self._valueOf(requestUrl),
    )

  @overload(QList[QOpcUaApplicationDescription], QOpcUa.UaStatusCode, QUrl)
  def findServersFinished(
      self,
      servers: QList[QOpcUaApplicationDescription],
      statusCode: QOpcUa.UaStatusCode,
      requestUrl: QUrl,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaClient::findServersFinished(QList<QOpcUaApplicationDescription>
    servers, QOpcUa::UaStatusCode statusCode, QUrl requestUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#findServersFinished

    Parameters
    ----------

    servers : QList[QOpcUaApplicationDescription]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.

    requestUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOpcUaClient::findServersFinished(
    #      QList<QOpcUaApplicationDescription> servers, QOpcUa::UaStatusCode
    #      statusCode, QUrl requestUrl)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient19findServersFinishedE5QListI28QOpcUaApplic'
        'ationDescriptionEN6QOpcUa12UaStatusCodeE4QUrl',
        self._valueOf(servers), statusCode.value, self._valueOf(requestUrl),
    )

  @overload(QList[QOpcUaReadResult], QOpcUa.UaStatusCode)
  def readNodeAttributesFinished(
      self,
      results: QList[QOpcUaReadResult],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaClient::readNodeAttributesFinished(QList<QOpcUaReadResult> results,
    QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#readNodeAttributesFinished

    Parameters
    ----------

    results : QList[QOpcUaReadResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClient::readNodeAttributesFinished(QList<QOpcUaReadResult>
    #      results, QOpcUa::UaStatusCode serviceResult)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient26readNodeAttributesFinishedE5QListI16QOpcU'
        'aReadResultEN6QOpcUa12UaStatusCodeE',
        self._valueOf(results), serviceResult.value,
    )

  @overload(QList[QOpcUaWriteResult], QOpcUa.UaStatusCode)
  def writeNodeAttributesFinished(
      self,
      results: QList[QOpcUaWriteResult],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaClient::writeNodeAttributesFinished(QList<QOpcUaWriteResult>
    results, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#writeNodeAttributesFinished

    Parameters
    ----------

    results : QList[QOpcUaWriteResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void
    #      QOpcUaClient::writeNodeAttributesFinished(QList<QOpcUaWriteResult>
    #      results, QOpcUa::UaStatusCode serviceResult)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient27writeNodeAttributesFinishedE5QListI17QOpc'
        'UaWriteResultEN6QOpcUa12UaStatusCodeE',
        self._valueOf(results), serviceResult.value,
    )

  @overload(QOpcUaExpandedNodeId, str, QOpcUa.UaStatusCode)
  def addNodeFinished(
      self,
      requestedNodeId: QOpcUaExpandedNodeId,
      assignedNodeId: str,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClient::addNodeFinished(QOpcUaExpandedNodeId
    requestedNodeId, QString assignedNodeId, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclient.html#addNodeFinished

    Parameters
    ----------

    requestedNodeId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.

    assignedNodeId : str
      Passed on as it is: a QString is made of it for the call.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClient::addNodeFinished(QOpcUaExpandedNodeId
    #      requestedNodeId, QString assignedNodeId, QOpcUa::UaStatusCode
    #      statusCode)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient15addNodeFinishedE20QOpcUaExpandedNodeId7QS'
        'tringN6QOpcUa12UaStatusCodeE',
        self._valueOf(requestedNodeId), assignedNodeId, statusCode.value,
    )

  @overload(str, QOpcUa.UaStatusCode)
  def deleteNodeFinished(
      self,
      nodeId: str,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClient::deleteNodeFinished(QString nodeId,
    QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#deleteNodeFinished

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClient::deleteNodeFinished(QString nodeId,
    #      QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient18deleteNodeFinishedE7QStringN6QOpcUa12UaSt'
        'atusCodeE',
        nodeId, statusCode.value,
    )

  @overload(str, str, QOpcUaExpandedNodeId, bool, QOpcUa.UaStatusCode)
  def addReferenceFinished(
      self,
      sourceNodeId: str,
      referenceTypeId: str,
      targetNodeId: QOpcUaExpandedNodeId,
      isForwardReference: bool,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClient::addReferenceFinished(QString sourceNodeId,
    QString referenceTypeId, QOpcUaExpandedNodeId targetNodeId, bool
    isForwardReference, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#addReferenceFinished

    Parameters
    ----------

    sourceNodeId : str
      Passed on as it is: a QString is made of it for the call.

    referenceTypeId : str
      Passed on as it is: a QString is made of it for the call.

    targetNodeId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.

    isForwardReference : bool
      Passed on as it is.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClient::addReferenceFinished(QString sourceNodeId, QString
    #      referenceTypeId, QOpcUaExpandedNodeId targetNodeId, bool
    #      isForwardReference, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient20addReferenceFinishedE7QStringS0_20QOpcUaE'
        'xpandedNodeIdbN6QOpcUa12UaStatusCodeE',
        sourceNodeId, referenceTypeId, self._valueOf(targetNodeId),
        isForwardReference, statusCode.value,
    )

  @overload(str, str, QOpcUaExpandedNodeId, bool, QOpcUa.UaStatusCode)
  def deleteReferenceFinished(
      self,
      sourceNodeId: str,
      referenceTypeId: str,
      targetNodeId: QOpcUaExpandedNodeId,
      isForwardReference: bool,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClient::deleteReferenceFinished(QString
    sourceNodeId, QString referenceTypeId, QOpcUaExpandedNodeId targetNodeId,
    bool isForwardReference, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#deleteReferenceFinished

    Parameters
    ----------

    sourceNodeId : str
      Passed on as it is: a QString is made of it for the call.

    referenceTypeId : str
      Passed on as it is: a QString is made of it for the call.

    targetNodeId : QOpcUaExpandedNodeId
      Passed on as a value: Qt reads the C++ QOpcUaExpandedNodeId, which
      stays Python's own.

    isForwardReference : bool
      Passed on as it is.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClient::deleteReferenceFinished(QString sourceNodeId,
    #      QString referenceTypeId, QOpcUaExpandedNodeId targetNodeId, bool
    #      isForwardReference, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient23deleteReferenceFinishedE7QStringS0_20QOpc'
        'UaExpandedNodeIdbN6QOpcUa12UaStatusCodeE',
        sourceNodeId, referenceTypeId, self._valueOf(targetNodeId),
        isForwardReference, statusCode.value,
    )

  @overload(str, QString, bool)
  @overload(str, NoneType, bool)
  def passwordForPrivateKeyRequired(
      self,
      keyFilePath: str,
      password: Optional[QString],
      previousTryWasInvalid: bool,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClient::passwordForPrivateKeyRequired(QString
    keyFilePath, QString *password, bool previousTryWasInvalid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#passwordForPrivateKeyRequired

    Parameters
    ----------

    keyFilePath : str
      Passed on as it is: a QString is made of it for the call.

    password : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    previousTryWasInvalid : bool
      Passed on as it is.
    """
    #  void QOpcUaClient::passwordForPrivateKeyRequired(QString keyFilePath,
    #      QString *password, bool previousTryWasInvalid)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient29passwordForPrivateKeyRequiredE7QStringPS0'
        '_b',
        keyFilePath, self._addressOf(password), previousTryWasInvalid,
    )

  @overload(QStringList, QStringList, QOpcUa.UaStatusCode)
  def registerNodesFinished(
      self,
      nodesToRegister: QStringList,
      registeredNodeIds: QStringList,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClient::registerNodesFinished(const QStringList
    &nodesToRegister, const QStringList &registeredNodeIds,
    QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#registerNodesFinished

    Parameters
    ----------

    nodesToRegister : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    registeredNodeIds : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClient::registerNodesFinished(const QStringList
    #      &nodesToRegister, const QStringList &registeredNodeIds,
    #      QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient21registerNodesFinishedERK5QListI7QStringES'
        '4_N6QOpcUa12UaStatusCodeE',
        self._valueOf(nodesToRegister), self._valueOf(registeredNodeIds),
        statusCode.value,
    )

  @overload(QStringList, QOpcUa.UaStatusCode)
  def unregisterNodesFinished(
      self,
      nodesToUnregister: QStringList,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClient::unregisterNodesFinished(const QStringList
    &nodesToUnregister, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclient.html#unregisterNodesFinished

    Parameters
    ----------

    nodesToUnregister : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClient::unregisterNodesFinished(const QStringList
    #      &nodesToUnregister, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN12QOpcUaClient23unregisterNodesFinishedERK5QListI7QString'
        'EN6QOpcUa12UaStatusCodeE',
        self._valueOf(nodesToUnregister), statusCode.value,
    )

  @staticmethod
  def qualifiedNameFromNamespaceUri(*__, **_) -> Never:
    """
    Qt's 'QOpcUaQualifiedName
    QOpcUaClient::qualifiedNameFromNamespaceUri(const QString &namespaceUri,
    const QString &name, bool *ok) const': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QOpcUaClient.qualifiedNameFromNamespaceUri' has no cute function "
        "yet. Qt's 'QOpcUaQualifiedName "
        "QOpcUaClient::qualifiedNameFromNamespaceUri(const QString "
        "&namespaceUri, const QString &name, bool *ok) const': takes a "
        "number to change where it is.")

  @staticmethod
  def resolveExpandedNodeId(*__, **_) -> Never:
    """
    Qt's 'QString QOpcUaClient::resolveExpandedNodeId(const
    QOpcUaExpandedNodeId &expandedNodeId, bool *ok) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QOpcUaClient.resolveExpandedNodeId' has no cute function yet. "
        "Qt's 'QString QOpcUaClient::resolveExpandedNodeId(const "
        "QOpcUaExpandedNodeId &expandedNodeId, bool *ok) const': takes a "
        "number to change where it is.")

  @staticmethod
  def supportedUserTokenTypes(*__, **_) -> Never:
    """
    Qt's 'QList<QOpcUaUserTokenPolicy::TokenType>
    QOpcUaClient::supportedUserTokenTypes() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaClient.supportedUserTokenTypes' has no cute function yet. "
        "Qt's 'QList<QOpcUaUserTokenPolicy::TokenType> "
        "QOpcUaClient::supportedUserTokenTypes() const': gives a type "
        "Python has no way to take yet.")
