"""
QOpcUaClientImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/6.12.0/QtOpcUa/private/qopcuaclientimpl_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QOpcUaClientImpl to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QOpcUa, QOpcUaClient, QOpcUaMonitoringParameters

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QString, QUrl, QVariant
  from . import QOpcUaAddNodeItem, QOpcUaAddReferenceItem
  from . import QOpcUaApplicationDescription, QOpcUaBackend
  from . import QOpcUaBrowsePathTarget, QOpcUaConnectionSettings
  from . import QOpcUaDeleteReferenceItem, QOpcUaEndpointDescription
  from . import QOpcUaErrorState, QOpcUaExpandedNodeId
  from . import QOpcUaHistoryReadEventRequest, QOpcUaHistoryReadRawRequest
  from . import QOpcUaHistoryReadResponse, QOpcUaNode, QOpcUaReadItem
  from . import QOpcUaReadResult, QOpcUaReferenceDescription
  from . import QOpcUaRelativePathElement, QOpcUaWriteItem, QOpcUaWriteResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaAddNodeItem = WAIT['QOpcUaAddNodeItem']
  QOpcUaAddReferenceItem = WAIT['QOpcUaAddReferenceItem']
  QOpcUaApplicationDescription = WAIT['QOpcUaApplicationDescription']
  QOpcUaBackend = WAIT['QOpcUaBackend']
  QOpcUaBrowsePathTarget = WAIT['QOpcUaBrowsePathTarget']
  QOpcUaConnectionSettings = WAIT['QOpcUaConnectionSettings']
  QOpcUaDeleteReferenceItem = WAIT['QOpcUaDeleteReferenceItem']
  QOpcUaEndpointDescription = WAIT['QOpcUaEndpointDescription']
  QOpcUaErrorState = WAIT['QOpcUaErrorState']
  QOpcUaExpandedNodeId = WAIT['QOpcUaExpandedNodeId']
  QOpcUaHistoryReadEventRequest = WAIT['QOpcUaHistoryReadEventRequest']
  QOpcUaHistoryReadRawRequest = WAIT['QOpcUaHistoryReadRawRequest']
  QOpcUaReadItem = WAIT['QOpcUaReadItem']
  QOpcUaReadResult = WAIT['QOpcUaReadResult']
  QOpcUaReferenceDescription = WAIT['QOpcUaReferenceDescription']
  QOpcUaRelativePathElement = WAIT['QOpcUaRelativePathElement']
  QOpcUaWriteItem = WAIT['QOpcUaWriteItem']
  QOpcUaWriteResult = WAIT['QOpcUaWriteResult']
  QString = WAIT['QString']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaClientImpl(QObject):
  """
  The cute side of Qt's QOpcUaClientImpl: a plain Python object standing in
  front of one C++ QOpcUaClientImpl.

  It is built on the cute 'QObject', as Qt's QOpcUaClientImpl is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpcUaClientImpl that has a ritual and that Python
  can call so far, 45 names in all: 'metaObject', 'tr', 'connectToEndpoint',
  'disconnectFromEndpoint', 'node', 'backend', 'requestEndpoints',
  'findServers', 'readNodeAttributes', 'writeNodeAttributes',
  'readHistoryData', 'readHistoryEvents', 'addNode', 'deleteNode',
  'addReference', 'deleteReference', 'connectBackendWithClient',
  'supportedSecurityPolicies', 'registerNodes', 'unregisterNodes',
  'handleAttributesRead', 'handleAttributeWritten',
  'handleDataChangeOccurred', 'handleMonitoringEnableDisable',
  'handleMonitoringStatusChanged', 'handleMethodCallFinished',
  'handleBrowseFinished', 'handleResolveBrowsePathFinished',
  'handleNewEvent', 'connected', 'disconnected', 'stateAndOrErrorChanged',
  'endpointsRequestFinished', 'findServersFinished',
  'readNodeAttributesFinished', 'writeNodeAttributesFinished',
  'addNodeFinished', 'deleteNodeFinished', 'addReferenceFinished',
  'deleteReferenceFinished', 'connectError', 'passwordForPrivateKeyRequired',
  'registerNodesFinished', 'unregisterNodesFinished',
  'connectionSettingsChanged'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpcUaClientImpl::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QOpcUaClientImpl::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QOpcUaClientImpl::~QOpcUaClientImpl()': the destructor: Python
    never removes a C++ QOpcUaClientImpl.
  - Qt's 'bool QOpcUaClientImpl::registerNode(QPointer<QOpcUaNodeImpl> obj)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QOpcUaClientImpl::unregisterNode(QPointer<QOpcUaNodeImpl>
    obj)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<QOpcUaUserTokenPolicy::TokenType>
    QOpcUaClientImpl::supportedUserTokenTypes() const': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  5 of the 56 functions Qt declares: 2 not a gap; 2 forbidden; 1 the class is
  abstract, so C++ cannot make one, and the C++ class of ours does not fill
  in every function it leaves open.

  What to expect
  --------------

  - The C++ QOpcUaClientImpl is created at the first use, not by
    'QOpcUaClientImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpcUaClientImpl.
  - Qt tells when it has removed the C++ QOpcUaClientImpl. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QOpcUaClientImpl that has no cute function yet,
    '__init__', 'registerNode', 'supportedUserTokenTypes', 'unregisterNode',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

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
    Calls Qt's 'QString QOpcUaClientImpl::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclientimpl.html#tr

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
    #  QString QOpcUaClientImpl::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QOpcUaClientImpl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaClientImpl'

  #  A C++ QOpcUaClientImpl Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpcUaClientImpl'

  #  The functions Qt calls itself that QOpcUaClientImpl is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'findServers': (
          'bool QOpcUaClientImpl::findServers(const QUrl &, const '
          'QStringList &, const QStringList &)',
      ),
      'readNodeAttributes': (
          'bool QOpcUaClientImpl::readNodeAttributes(const '
          'QList<QOpcUaReadItem> &)',
      ),
      'writeNodeAttributes': (
          'bool QOpcUaClientImpl::writeNodeAttributes(const '
          'QList<QOpcUaWriteItem> &)',
      ),
      'supportedSecurityPolicies': (
          'QStringList QOpcUaClientImpl::supportedSecurityPolicies() const',
      ),
      'supportedUserTokenTypes': (
          'QList<QOpcUaUserTokenPolicy::TokenType> '
          'QOpcUaClientImpl::supportedUserTokenTypes() const',
      ),
      'registerNodes': (
          'bool QOpcUaClientImpl::registerNodes(const QStringList &)',
      ),
      'unregisterNodes': (
          'bool QOpcUaClientImpl::unregisterNodes(const QStringList &)',
      ),
  }

  #  The functions Qt calls itself that QOpcUaClientImpl is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'connectToEndpoint': (
          ('_ZN16QOpcUaClientImpl17connectToEndpointERK25QOpcUaEndpointDesc'
           'ription',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtOpcUa:QOpcUaEndpointDescription'),
           )),
      ),
      'disconnectFromEndpoint': (
          ('_ZN16QOpcUaClientImpl22disconnectFromEndpointEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'node': (
          ('_ZN16QOpcUaClientImpl4nodeERK7QString',
           ('address', 'address', 'QtOpcUa:QOpcUaNode'),
           (
               ('address', 'text', ''),
           )),
      ),
      'backend': (
          ('_ZNK16QOpcUaClientImpl7backendEv',
           ('address', 'text', ''),
           ()),
      ),
      'requestEndpoints': (
          ('_ZN16QOpcUaClientImpl16requestEndpointsERK4QUrl',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'readHistoryData': (
          ('_ZN16QOpcUaClientImpl15readHistoryDataERK27QOpcUaHistoryReadRaw'
           'Request',
           ('address', 'address', 'QtOpcUa:QOpcUaHistoryReadResponse'),
           (
               ('address', 'value', 'QtOpcUa:QOpcUaHistoryReadRawRequest'),
           )),
      ),
      'readHistoryEvents': (
          ('_ZN16QOpcUaClientImpl17readHistoryEventsERK29QOpcUaHistoryReadE'
           'ventRequest',
           ('address', 'address', 'QtOpcUa:QOpcUaHistoryReadResponse'),
           (
               ('address', 'value', 'QtOpcUa:QOpcUaHistoryReadEventRequest'),
           )),
      ),
      'addNode': (
          ('_ZN16QOpcUaClientImpl7addNodeERK17QOpcUaAddNodeItem',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtOpcUa:QOpcUaAddNodeItem'),
           )),
      ),
      'deleteNode': (
          ('_ZN16QOpcUaClientImpl10deleteNodeERK7QStringb',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('bool', 'number', ''),
           )),
      ),
      'addReference': (
          ('_ZN16QOpcUaClientImpl12addReferenceERK22QOpcUaAddReferenceItem',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtOpcUa:QOpcUaAddReferenceItem'),
           )),
      ),
      'deleteReference': (
          ('_ZN16QOpcUaClientImpl15deleteReferenceERK25QOpcUaDeleteReferenc'
           'eItem',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtOpcUa:QOpcUaDeleteReferenceItem'),
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
    Calls Qt's 'const QMetaObject *QOpcUaClientImpl::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclientimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpcUaClientImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QOpcUaClientImpl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def backend(self) -> str:
    """
    Calls Qt's 'QString QOpcUaClientImpl::backend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclientimpl.html#backend

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaClientImpl::backend() const
    return self.uglySide.call('ritual_ZNK16QOpcUaClientImpl7backendEv')

  def supportedSecurityPolicies(self) -> QStringList:
    """
    Calls Qt's 'QStringList QOpcUaClientImpl::supportedSecurityPolicies()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#supportedSecurityPolicies

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QOpcUaClientImpl::supportedSecurityPolicies() const
    address = self.uglySide.call(
        'ritual_ZNK16QOpcUaClientImpl25supportedSecurityPoliciesEv',
    )
    return QStringList._cuteOwning(address)

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
    Qt's 'QOpcUaClientImpl::QOpcUaClientImpl(QObject *parent)': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QOpcUaClientImpl.__init__' has no cute function yet. Qt's "
        "'QOpcUaClientImpl::QOpcUaClientImpl(QObject *parent)': the class "
        "is abstract, so C++ cannot make one, and the C++ class of ours "
        "does not fill in every function it leaves open.")

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

  @overload(QOpcUaEndpointDescription)
  def connectToEndpoint(self, endpoint: QOpcUaEndpointDescription) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::connectToEndpoint(const
    QOpcUaEndpointDescription &endpoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#connectToEndpoint

    Parameters
    ----------

    endpoint : QOpcUaEndpointDescription
      Passed on as a value: Qt reads the C++ QOpcUaEndpointDescription, which
      stays Python's own.
    """
    #  void QOpcUaClientImpl::connectToEndpoint(const
    #      QOpcUaEndpointDescription &endpoint)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl17connectToEndpointERK25QOpcUaEndpointD'
        'escription',
        self._valueOf(endpoint),
    )

  def disconnectFromEndpoint(self) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::disconnectFromEndpoint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#disconnectFromEndpoint
    """
    #  void QOpcUaClientImpl::disconnectFromEndpoint()
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl22disconnectFromEndpointEv',
    )

  @overload(str)
  def node(self, nodeId: str) -> Optional[QOpcUaNode]:
    """
    Calls Qt's 'QOpcUaNode *QOpcUaClientImpl::node(const QString &nodeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclientimpl.html#node

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
    #  QOpcUaNode *QOpcUaClientImpl::node(const QString &nodeId)
    address = self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl4nodeERK7QString', nodeId,
    )
    from . import QOpcUaNode
    return QOpcUaNode._cuteAt(address)

  @overload(QUrl)
  def requestEndpoints(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QOpcUaClientImpl::requestEndpoints(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#requestEndpoints

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QOpcUaClientImpl::requestEndpoints(const QUrl &url)
    return self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl16requestEndpointsERK4QUrl',
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
    Calls Qt's 'bool QOpcUaClientImpl::findServers(const QUrl &url, const
    QStringList &localeIds, const QStringList &serverUris)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclientimpl.html#findServers

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
    #  bool QOpcUaClientImpl::findServers(const QUrl &url, const QStringList
    #      &localeIds, const QStringList &serverUris)
    return self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl11findServersERK4QUrlRK5QListI7QStringE'
        'S7_',
        self._valueOf(url), self._valueOf(localeIds),
        self._valueOf(serverUris),
    )

  @overload(QList[QOpcUaReadItem])
  def readNodeAttributes(self, nodesToRead: QList[QOpcUaReadItem]) -> bool:
    """
    Calls Qt's 'bool QOpcUaClientImpl::readNodeAttributes(const
    QList<QOpcUaReadItem> &nodesToRead)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#readNodeAttributes

    Parameters
    ----------

    nodesToRead : QList[QOpcUaReadItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QOpcUaClientImpl::readNodeAttributes(const QList<QOpcUaReadItem>
    #      &nodesToRead)
    return self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl18readNodeAttributesERK5QListI14QOpcUaR'
        'eadItemE',
        self._valueOf(nodesToRead),
    )

  @overload(QList[QOpcUaWriteItem])
  def writeNodeAttributes(
      self,
      nodesToWrite: QList[QOpcUaWriteItem],
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaClientImpl::writeNodeAttributes(const
    QList<QOpcUaWriteItem> &nodesToWrite)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#writeNodeAttributes

    Parameters
    ----------

    nodesToWrite : QList[QOpcUaWriteItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QOpcUaClientImpl::writeNodeAttributes(const
    #      QList<QOpcUaWriteItem> &nodesToWrite)
    return self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl19writeNodeAttributesERK5QListI15QOpcUa'
        'WriteItemE',
        self._valueOf(nodesToWrite),
    )

  @overload(QOpcUaHistoryReadRawRequest)
  def readHistoryData(
      self,
      request: QOpcUaHistoryReadRawRequest,
  ) -> Optional[QOpcUaHistoryReadResponse]:
    """
    Calls Qt's 'QOpcUaHistoryReadResponse
    *QOpcUaClientImpl::readHistoryData(const QOpcUaHistoryReadRawRequest
    &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#readHistoryData

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
    #  QOpcUaHistoryReadResponse *QOpcUaClientImpl::readHistoryData(const
    #      QOpcUaHistoryReadRawRequest &request)
    address = self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl15readHistoryDataERK27QOpcUaHistoryRead'
        'RawRequest',
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
    *QOpcUaClientImpl::readHistoryEvents(const QOpcUaHistoryReadEventRequest
    &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#readHistoryEvents

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
    #  QOpcUaHistoryReadResponse *QOpcUaClientImpl::readHistoryEvents(const
    #      QOpcUaHistoryReadEventRequest &request)
    address = self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl17readHistoryEventsERK29QOpcUaHistoryRe'
        'adEventRequest',
        self._valueOf(request),
    )
    from . import QOpcUaHistoryReadResponse
    return QOpcUaHistoryReadResponse._cuteAt(address)

  @overload(QOpcUaAddNodeItem)
  def addNode(self, nodeToAdd: QOpcUaAddNodeItem) -> bool:
    """
    Calls Qt's 'bool QOpcUaClientImpl::addNode(const QOpcUaAddNodeItem
    &nodeToAdd)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclientimpl.html#addNode

    Parameters
    ----------

    nodeToAdd : QOpcUaAddNodeItem
      Passed on as a value: Qt reads the C++ QOpcUaAddNodeItem, which stays
      Python's own.
    """
    #  bool QOpcUaClientImpl::addNode(const QOpcUaAddNodeItem &nodeToAdd)
    return self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl7addNodeERK17QOpcUaAddNodeItem',
        self._valueOf(nodeToAdd),
    )

  @overload(str, bool)
  def deleteNode(self, nodeId: str, deleteTargetReferences: bool) -> bool:
    """
    Calls Qt's 'bool QOpcUaClientImpl::deleteNode(const QString &nodeId, bool
    deleteTargetReferences)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclientimpl.html#deleteNode

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.

    deleteTargetReferences : bool
      Passed on as it is.
    """
    #  bool QOpcUaClientImpl::deleteNode(const QString &nodeId, bool
    #      deleteTargetReferences)
    return self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl10deleteNodeERK7QStringb',
        nodeId, deleteTargetReferences,
    )

  @overload(QOpcUaAddReferenceItem)
  def addReference(self, referenceToAdd: QOpcUaAddReferenceItem) -> bool:
    """
    Calls Qt's 'bool QOpcUaClientImpl::addReference(const
    QOpcUaAddReferenceItem &referenceToAdd)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclientimpl.html#addReference

    Parameters
    ----------

    referenceToAdd : QOpcUaAddReferenceItem
      Passed on as a value: Qt reads the C++ QOpcUaAddReferenceItem, which
      stays Python's own.
    """
    #  bool QOpcUaClientImpl::addReference(const QOpcUaAddReferenceItem
    #      &referenceToAdd)
    return self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl12addReferenceERK22QOpcUaAddReferenceIt'
        'em',
        self._valueOf(referenceToAdd),
    )

  @overload(QOpcUaDeleteReferenceItem)
  def deleteReference(
      self,
      referenceToDelete: QOpcUaDeleteReferenceItem,
  ) -> bool:
    """
    Calls Qt's 'bool QOpcUaClientImpl::deleteReference(const
    QOpcUaDeleteReferenceItem &referenceToDelete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#deleteReference

    Parameters
    ----------

    referenceToDelete : QOpcUaDeleteReferenceItem
      Passed on as a value: Qt reads the C++ QOpcUaDeleteReferenceItem, which
      stays Python's own.
    """
    #  bool QOpcUaClientImpl::deleteReference(const QOpcUaDeleteReferenceItem
    #      &referenceToDelete)
    return self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl15deleteReferenceERK25QOpcUaDeleteRefer'
        'enceItem',
        self._valueOf(referenceToDelete),
    )

  @overload(QOpcUaBackend)
  @overload(NoneType)
  def connectBackendWithClient(
      self,
      backend: Optional[QOpcUaBackend],
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::connectBackendWithClient(QOpcUaBackend
    *backend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#connectBackendWithClient

    Parameters
    ----------

    backend : Optional[QOpcUaBackend]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpcUaClientImpl::connectBackendWithClient(QOpcUaBackend
    #      *backend)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl24connectBackendWithClientEP13QOpcUaBac'
        'kend',
        self._addressOf(backend),
    )

  @overload(QStringList)
  def registerNodes(self, nodesToRegister: QStringList) -> bool:
    """
    Calls Qt's 'bool QOpcUaClientImpl::registerNodes(const QStringList
    &nodesToRegister)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#registerNodes

    Parameters
    ----------

    nodesToRegister : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QOpcUaClientImpl::registerNodes(const QStringList
    #      &nodesToRegister)
    return self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl13registerNodesERK5QListI7QStringE',
        self._valueOf(nodesToRegister),
    )

  @overload(QStringList)
  def unregisterNodes(self, nodesToUnregister: QStringList) -> bool:
    """
    Calls Qt's 'bool QOpcUaClientImpl::unregisterNodes(const QStringList
    &nodesToUnregister)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#unregisterNodes

    Parameters
    ----------

    nodesToUnregister : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QOpcUaClientImpl::unregisterNodes(const QStringList
    #      &nodesToUnregister)
    return self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl15unregisterNodesERK5QListI7QStringE',
        self._valueOf(nodesToUnregister),
    )

  @overload(int, QList[QOpcUaReadResult], QOpcUa.UaStatusCode)
  def handleAttributesRead(
      self,
      handle: int,
      attr: QList[QOpcUaReadResult],
      serviceResult: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::handleAttributesRead(quint64 handle,
    QList<QOpcUaReadResult> attr, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#handleAttributesRead

    Parameters
    ----------

    handle : int
      Passed on as it is.

    attr : QList[QOpcUaReadResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClientImpl::handleAttributesRead(quint64 handle,
    #      QList<QOpcUaReadResult> attr, QOpcUa::UaStatusCode serviceResult)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl20handleAttributesReadEy5QListI16QOpcUa'
        'ReadResultEN6QOpcUa12UaStatusCodeE',
        handle, self._valueOf(attr), serviceResult.value,
    )

  @overload(int, QOpcUa.NodeAttribute, QVariant, QOpcUa.UaStatusCode)
  def handleAttributeWritten(
      self,
      handle: int,
      attr: QOpcUa.NodeAttribute,
      value: QVariant,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::handleAttributeWritten(quint64 handle,
    QOpcUa::NodeAttribute attr, const QVariant &value, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#handleAttributeWritten

    Parameters
    ----------

    handle : int
      Passed on as it is.

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClientImpl::handleAttributeWritten(quint64 handle,
    #      QOpcUa::NodeAttribute attr, const QVariant &value,
    #      QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl22handleAttributeWrittenEyN6QOpcUa13Nod'
        'eAttributeERK8QVariantNS0_12UaStatusCodeE',
        handle, attr.value, self._valueOf(value), statusCode.value,
    )

  @overload(int, QOpcUaReadResult)
  def handleDataChangeOccurred(
      self,
      handle: int,
      value: QOpcUaReadResult,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::handleDataChangeOccurred(quint64
    handle, const QOpcUaReadResult &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#handleDataChangeOccurred

    Parameters
    ----------

    handle : int
      Passed on as it is.

    value : QOpcUaReadResult
      Passed on as a value: Qt reads the C++ QOpcUaReadResult, which stays
      Python's own.
    """
    #  void QOpcUaClientImpl::handleDataChangeOccurred(quint64 handle, const
    #      QOpcUaReadResult &value)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl24handleDataChangeOccurredEyRK16QOpcUaR'
        'eadResult',
        handle, self._valueOf(value),
    )

  @overload(int, QOpcUa.NodeAttribute, bool, QOpcUaMonitoringParameters)
  def handleMonitoringEnableDisable(
      self,
      handle: int,
      attr: QOpcUa.NodeAttribute,
      subscribe: bool,
      status: QOpcUaMonitoringParameters,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::handleMonitoringEnableDisable(quint64
    handle, QOpcUa::NodeAttribute attr, bool subscribe,
    QOpcUaMonitoringParameters status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html

    Parameters
    ----------

    handle : int
      Passed on as it is.

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    subscribe : bool
      Passed on as it is.

    status : QOpcUaMonitoringParameters
      Passed on as a value: Qt reads the C++ QOpcUaMonitoringParameters,
      which stays Python's own.
    """
    #  void QOpcUaClientImpl::handleMonitoringEnableDisable(quint64 handle,
    #      QOpcUa::NodeAttribute attr, bool subscribe,
    #      QOpcUaMonitoringParameters status)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl29handleMonitoringEnableDisableEyN6QOpc'
        'Ua13NodeAttributeEb26QOpcUaMonitoringParameters',
        handle, attr.value, subscribe, self._valueOf(status),
    )

  @overload(
      int, QOpcUa.NodeAttribute, QOpcUaMonitoringParameters.Parameters,
      QOpcUaMonitoringParameters,
  )
  def handleMonitoringStatusChanged(
      self,
      handle: int,
      attr: QOpcUa.NodeAttribute,
      items: QOpcUaMonitoringParameters.Parameters,
      param: QOpcUaMonitoringParameters,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::handleMonitoringStatusChanged(quint64
    handle, QOpcUa::NodeAttribute attr,
    QOpcUaMonitoringParameters::Parameters items, QOpcUaMonitoringParameters
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html

    Parameters
    ----------

    handle : int
      Passed on as it is.

    attr : QOpcUa.NodeAttribute
      Passed on as its number.

    items : QOpcUaMonitoringParameters.Parameters
      Passed on as its number.

    param : QOpcUaMonitoringParameters
      Passed on as a value: Qt reads the C++ QOpcUaMonitoringParameters,
      which stays Python's own.
    """
    #  void QOpcUaClientImpl::handleMonitoringStatusChanged(quint64 handle,
    #      QOpcUa::NodeAttribute attr, QOpcUaMonitoringParameters::Parameters
    #      items, QOpcUaMonitoringParameters param)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl29handleMonitoringStatusChangedEyN6QOpc'
        'Ua13NodeAttributeE6QFlagsIN26QOpcUaMonitoringParameters9ParameterE'
        'ES3_',
        handle, attr.value, items.value, self._valueOf(param),
    )

  @overload(int, str, QVariant, QOpcUa.UaStatusCode)
  def handleMethodCallFinished(
      self,
      handle: int,
      methodNodeId: str,
      result: QVariant,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::handleMethodCallFinished(quint64
    handle, QString methodNodeId, QVariant result, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#handleMethodCallFinished

    Parameters
    ----------

    handle : int
      Passed on as it is.

    methodNodeId : str
      Passed on as it is: a QString is made of it for the call.

    result : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClientImpl::handleMethodCallFinished(quint64 handle,
    #      QString methodNodeId, QVariant result, QOpcUa::UaStatusCode
    #      statusCode)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl24handleMethodCallFinishedEy7QString8QV'
        'ariantN6QOpcUa12UaStatusCodeE',
        handle, methodNodeId, self._valueOf(result), statusCode.value,
    )

  @overload(int, QList[QOpcUaReferenceDescription], QOpcUa.UaStatusCode)
  def handleBrowseFinished(
      self,
      handle: int,
      children: QList[QOpcUaReferenceDescription],
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::handleBrowseFinished(quint64 handle,
    const QList<QOpcUaReferenceDescription> &children, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#handleBrowseFinished

    Parameters
    ----------

    handle : int
      Passed on as it is.

    children : QList[QOpcUaReferenceDescription]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClientImpl::handleBrowseFinished(quint64 handle, const
    #      QList<QOpcUaReferenceDescription> &children, QOpcUa::UaStatusCode
    #      statusCode)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl20handleBrowseFinishedEyRK5QListI26QOpc'
        'UaReferenceDescriptionEN6QOpcUa12UaStatusCodeE',
        handle, self._valueOf(children), statusCode.value,
    )

  @overload(
      int, QList[QOpcUaBrowsePathTarget], QList[QOpcUaRelativePathElement],
      QOpcUa.UaStatusCode,
  )
  def handleResolveBrowsePathFinished(
      self,
      handle: int,
      targets: QList[QOpcUaBrowsePathTarget],
      path: QList[QOpcUaRelativePathElement],
      status: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaClientImpl::handleResolveBrowsePathFinished(quint64 handle,
    QList<QOpcUaBrowsePathTarget> targets, QList<QOpcUaRelativePathElement>
    path, QOpcUa::UaStatusCode status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html

    Parameters
    ----------

    handle : int
      Passed on as it is.

    targets : QList[QOpcUaBrowsePathTarget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    path : QList[QOpcUaRelativePathElement]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    status : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClientImpl::handleResolveBrowsePathFinished(quint64 handle,
    #      QList<QOpcUaBrowsePathTarget> targets,
    #      QList<QOpcUaRelativePathElement> path, QOpcUa::UaStatusCode
    #      status)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl31handleResolveBrowsePathFinishedEy5QLi'
        'stI22QOpcUaBrowsePathTargetES0_I25QOpcUaRelativePathElementEN6QOpc'
        'Ua12UaStatusCodeE',
        handle, self._valueOf(targets), self._valueOf(path), status.value,
    )

  @overload(int, QList[QVariant])
  def handleNewEvent(
      self,
      handle: int,
      eventFields: QList[QVariant],
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::handleNewEvent(quint64 handle,
    QVariantList eventFields)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#handleNewEvent

    Parameters
    ----------

    handle : int
      Passed on as it is.

    eventFields : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaClientImpl::handleNewEvent(quint64 handle, QVariantList
    #      eventFields)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl14handleNewEventEy5QListI8QVariantE',
        handle, self._valueOf(eventFields),
    )

  def connected(self) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::connected()'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclientimpl.html#connected
    """
    #  void QOpcUaClientImpl::connected()
    self.uglySide.call('ritual_ZN16QOpcUaClientImpl9connectedEv')

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::disconnected()'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclientimpl.html#disconnected
    """
    #  void QOpcUaClientImpl::disconnected()
    self.uglySide.call('ritual_ZN16QOpcUaClientImpl12disconnectedEv')

  @overload(QOpcUaClient.ClientState, QOpcUaClient.ClientError)
  def stateAndOrErrorChanged(
      self,
      state: QOpcUaClient.ClientState,
      error: QOpcUaClient.ClientError,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaClientImpl::stateAndOrErrorChanged(QOpcUaClient::ClientState state,
    QOpcUaClient::ClientError error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#stateAndOrErrorChanged

    Parameters
    ----------

    state : QOpcUaClient.ClientState
      Passed on as its number.

    error : QOpcUaClient.ClientError
      Passed on as its number.
    """
    #  void
    #      QOpcUaClientImpl::stateAndOrErrorChanged(QOpcUaClient::ClientState
    #      state, QOpcUaClient::ClientError error)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl22stateAndOrErrorChangedEN12QOpcUaClien'
        't11ClientStateENS0_11ClientErrorE',
        state.value, error.value,
    )

  @overload(QList[QOpcUaEndpointDescription], QOpcUa.UaStatusCode, QUrl)
  def endpointsRequestFinished(
      self,
      endpoints: QList[QOpcUaEndpointDescription],
      statusCode: QOpcUa.UaStatusCode,
      requestUrl: QUrl,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::endpointsRequestFinished(
    QList<QOpcUaEndpointDescription> endpoints, QOpcUa::UaStatusCode
    statusCode, QUrl requestUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#endpointsRequestFinished

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
    #  void QOpcUaClientImpl::endpointsRequestFinished(
    #      QList<QOpcUaEndpointDescription> endpoints, QOpcUa::UaStatusCode
    #      statusCode, QUrl requestUrl)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl24endpointsRequestFinishedE5QListI25QOp'
        'cUaEndpointDescriptionEN6QOpcUa12UaStatusCodeE4QUrl',
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
    QOpcUaClientImpl::findServersFinished(QList<QOpcUaApplicationDescription>
    servers, QOpcUa::UaStatusCode statusCode, QUrl requestUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#findServersFinished

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
    #  void QOpcUaClientImpl::findServersFinished(
    #      QList<QOpcUaApplicationDescription> servers, QOpcUa::UaStatusCode
    #      statusCode, QUrl requestUrl)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl19findServersFinishedE5QListI28QOpcUaAp'
        'plicationDescriptionEN6QOpcUa12UaStatusCodeE4QUrl',
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
    QOpcUaClientImpl::readNodeAttributesFinished(QList<QOpcUaReadResult>
    results, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#readNodeAttributesFinished

    Parameters
    ----------

    results : QList[QOpcUaReadResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClientImpl::readNodeAttributesFinished(
    #      QList<QOpcUaReadResult> results, QOpcUa::UaStatusCode
    #      serviceResult)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl26readNodeAttributesFinishedE5QListI16Q'
        'OpcUaReadResultEN6QOpcUa12UaStatusCodeE',
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
    QOpcUaClientImpl::writeNodeAttributesFinished(QList<QOpcUaWriteResult>
    results, QOpcUa::UaStatusCode serviceResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#writeNodeAttributesFinished

    Parameters
    ----------

    results : QList[QOpcUaWriteResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    serviceResult : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClientImpl::writeNodeAttributesFinished(
    #      QList<QOpcUaWriteResult> results, QOpcUa::UaStatusCode
    #      serviceResult)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl27writeNodeAttributesFinishedE5QListI17'
        'QOpcUaWriteResultEN6QOpcUa12UaStatusCodeE',
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
    Calls Qt's 'void QOpcUaClientImpl::addNodeFinished(QOpcUaExpandedNodeId
    requestedNodeId, QString assignedNodeId, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#addNodeFinished

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
    #  void QOpcUaClientImpl::addNodeFinished(QOpcUaExpandedNodeId
    #      requestedNodeId, QString assignedNodeId, QOpcUa::UaStatusCode
    #      statusCode)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl15addNodeFinishedE20QOpcUaExpandedNodeI'
        'd7QStringN6QOpcUa12UaStatusCodeE',
        self._valueOf(requestedNodeId), assignedNodeId, statusCode.value,
    )

  @overload(str, QOpcUa.UaStatusCode)
  def deleteNodeFinished(
      self,
      nodeId: str,
      statusCode: QOpcUa.UaStatusCode,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::deleteNodeFinished(QString nodeId,
    QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#deleteNodeFinished

    Parameters
    ----------

    nodeId : str
      Passed on as it is: a QString is made of it for the call.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClientImpl::deleteNodeFinished(QString nodeId,
    #      QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl18deleteNodeFinishedE7QStringN6QOpcUa12'
        'UaStatusCodeE',
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
    Calls Qt's 'void QOpcUaClientImpl::addReferenceFinished(QString
    sourceNodeId, QString referenceTypeId, QOpcUaExpandedNodeId targetNodeId,
    bool isForwardReference, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#addReferenceFinished

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
    #  void QOpcUaClientImpl::addReferenceFinished(QString sourceNodeId,
    #      QString referenceTypeId, QOpcUaExpandedNodeId targetNodeId, bool
    #      isForwardReference, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl20addReferenceFinishedE7QStringS0_20QOp'
        'cUaExpandedNodeIdbN6QOpcUa12UaStatusCodeE',
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
    Calls Qt's 'void QOpcUaClientImpl::deleteReferenceFinished(QString
    sourceNodeId, QString referenceTypeId, QOpcUaExpandedNodeId targetNodeId,
    bool isForwardReference, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#deleteReferenceFinished

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
    #  void QOpcUaClientImpl::deleteReferenceFinished(QString sourceNodeId,
    #      QString referenceTypeId, QOpcUaExpandedNodeId targetNodeId, bool
    #      isForwardReference, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl23deleteReferenceFinishedE7QStringS0_20'
        'QOpcUaExpandedNodeIdbN6QOpcUa12UaStatusCodeE',
        sourceNodeId, referenceTypeId, self._valueOf(targetNodeId),
        isForwardReference, statusCode.value,
    )

  @overload(QOpcUaErrorState)
  @overload(NoneType)
  def connectError(self, errorState: Optional[QOpcUaErrorState]) -> None:
    """
    Calls Qt's 'void QOpcUaClientImpl::connectError(QOpcUaErrorState
    *errorState)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaclientimpl.html#connectError

    Parameters
    ----------

    errorState : Optional[QOpcUaErrorState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpcUaClientImpl::connectError(QOpcUaErrorState *errorState)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl12connectErrorEP16QOpcUaErrorState',
        self._addressOf(errorState),
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
    Calls Qt's 'void QOpcUaClientImpl::passwordForPrivateKeyRequired(const
    QString keyFilePath, QString *password, bool previousTryWasInvalid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html

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
    #  void QOpcUaClientImpl::passwordForPrivateKeyRequired(const QString
    #      keyFilePath, QString *password, bool previousTryWasInvalid)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl29passwordForPrivateKeyRequiredE7QStrin'
        'gPS0_b',
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
    Calls Qt's 'void QOpcUaClientImpl::registerNodesFinished(QStringList
    nodesToRegister, QStringList registeredNodeIds, QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#registerNodesFinished

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
    #  void QOpcUaClientImpl::registerNodesFinished(QStringList
    #      nodesToRegister, QStringList registeredNodeIds,
    #      QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl21registerNodesFinishedE5QListI7QString'
        'ES2_N6QOpcUa12UaStatusCodeE',
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
    Calls Qt's 'void QOpcUaClientImpl::unregisterNodesFinished(QStringList
    nodesToUnregister, QOpcUa::UaStatusCode statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#unregisterNodesFinished

    Parameters
    ----------

    nodesToUnregister : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaClientImpl::unregisterNodesFinished(QStringList
    #      nodesToUnregister, QOpcUa::UaStatusCode statusCode)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl23unregisterNodesFinishedE5QListI7QStri'
        'ngEN6QOpcUa12UaStatusCodeE',
        self._valueOf(nodesToUnregister), statusCode.value,
    )

  @overload(QOpcUaConnectionSettings)
  def connectionSettingsChanged(
      self,
      settings: QOpcUaConnectionSettings,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaClientImpl::connectionSettingsChanged(QOpcUaConnectionSettings
    settings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaclientimpl.html#connectionSettingsChanged

    Parameters
    ----------

    settings : QOpcUaConnectionSettings
      Passed on as a value: Qt reads the C++ QOpcUaConnectionSettings, which
      stays Python's own.
    """
    #  void QOpcUaClientImpl::connectionSettingsChanged(
    #      QOpcUaConnectionSettings settings)
    self.uglySide.call(
        'ritual_ZN16QOpcUaClientImpl25connectionSettingsChangedE24QOpcUaCon'
        'nectionSettings',
        self._valueOf(settings),
    )

  @staticmethod
  def registerNode(*__, **_) -> Never:
    """
    Qt's 'bool QOpcUaClientImpl::registerNode(QPointer<QOpcUaNodeImpl> obj)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaClientImpl.registerNode' has no cute function yet. Qt's "
        "'bool QOpcUaClientImpl::registerNode(QPointer<QOpcUaNodeImpl> "
        "obj)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def supportedUserTokenTypes(*__, **_) -> Never:
    """
    Qt's 'QList<QOpcUaUserTokenPolicy::TokenType>
    QOpcUaClientImpl::supportedUserTokenTypes() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaClientImpl.supportedUserTokenTypes' has no cute function "
        "yet. Qt's 'QList<QOpcUaUserTokenPolicy::TokenType> "
        "QOpcUaClientImpl::supportedUserTokenTypes() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def unregisterNode(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaClientImpl::unregisterNode(QPointer<QOpcUaNodeImpl>
    obj)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaClientImpl.unregisterNode' has no cute function yet. Qt's "
        "'void QOpcUaClientImpl::unregisterNode(QPointer<QOpcUaNodeImpl> "
        "obj)': takes a type Python has no way to hand over yet.")
