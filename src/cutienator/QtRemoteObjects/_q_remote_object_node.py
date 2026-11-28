"""
QRemoteObjectNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qremoteobjectnode.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QtRemoteObjects

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QMetaObject, QTimerEvent, QUrl
  from ..QtCore import QVariant
  from . import QRemoteObjectAbstractPersistedStore
  from . import QRemoteObjectDynamicReplica, QRemoteObjectNodePrivate
  from . import QRemoteObjectRegistry, QRemoteObjectReplica
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']
  QRemoteObjectAbstractPersistedStore = WAIT['QRemoteObjectAbstractPersistedStore']
  QRemoteObjectReplica = WAIT['QRemoteObjectReplica']
  QTimerEvent = WAIT['QTimerEvent']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectNode(QObject):
  """
  The cute side of Qt's QRemoteObjectNode: a plain Python object standing in
  front of one C++ QRemoteObjectNode.

  It is built on the cute 'QObject', as Qt's QRemoteObjectNode is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectNode that has a ritual and that Python
  can call so far, 25 names in all: 'metaObject', 'tr', 'connectToNode',
  'addClientSideConnection', 'setName', 'instances', 'acquireDynamic',
  'registryUrl', 'setRegistryUrl', 'waitForRegistry', 'registry',
  'persistedStore', 'setPersistedStore', 'lastError', 'heartbeatInterval',
  'setHeartbeatInterval', 'registryUrlChanged', 'persistedStoreChanged',
  'error', 'heartbeatIntervalChanged', 'timerEvent', 'initializeReplica',
  'persistProperties', 'retrieveProperties', 'd_func'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRemoteObjectNode::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QRemoteObjectNode::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QRemoteObjectNode::~QRemoteObjectNode()': the destructor: Python
    never removes a C++ QRemoteObjectNode.
  - Qt's 'QAbstractItemModelReplica *QRemoteObjectNode::acquireModel(const
    QString &name, QtRemoteObjects::InitialAction action, const QList<int>
    &rolesHint)': takes a type Python has no way to hand over yet.
  - Qt's 'void QRemoteObjectNode::registerExternalSchema(const QString
    &schema, RemoteObjectSchemaHandler handler)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QRemoteObjectNode::remoteObjectAdded(const
    QRemoteObjectSourceLocation &a0)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QRemoteObjectNode::remoteObjectRemoved(const
    QRemoteObjectSourceLocation &a0)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QRemoteObjectNode::QRemoteObjectNode(QRemoteObjectNodePrivate &a0,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QRemoteObjectNodePrivate *QRemoteObjectNode::d_func() const':
    takes in Python what 'QRemoteObjectNodePrivate
    *QRemoteObjectNode::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 40 functions Qt declares: 2 not a gap; 2 a template.

  What to expect
  --------------

  - The C++ QRemoteObjectNode is created at the first use, not by
    'QRemoteObjectNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectNode.
  - Qt tells when it has removed the C++ QRemoteObjectNode. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QRemoteObjectNode that has no cute function yet,
    'acquire', 'acquireModel', 'registerExternalSchema', 'remoteObjectAdded',
    'remoteObjectRemoved', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRemoteObjectNode, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ErrorCode(CuteNum):
    """
    The enum 'QRemoteObjectNode::ErrorCode' of Qt, with the 13 names Qt gives
    in it.
    """

    NoError = Kee[int](0)
    RegistryNotAcquired = Kee[int](1)
    RegistryAlreadyHosted = Kee[int](2)
    NodeIsNoServer = Kee[int](3)
    ServerAlreadyCreated = Kee[int](4)
    UnintendedRegistryHosting = Kee[int](5)
    OperationNotValidOnClientNode = Kee[int](6)
    SourceNotRegistered = Kee[int](7)
    MissingObjectName = Kee[int](8)
    HostUrlInvalid = Kee[int](9)
    ProtocolMismatch = Kee[int](10)
    ListenFailed = Kee[int](11)
    SocketAccessError = Kee[int](12)

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
    Calls Qt's 'QString QRemoteObjectNode::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectnode.html#tr

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
    #  QString QRemoteObjectNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QRemoteObjectNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectNode'

  #  A C++ QRemoteObjectNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectNode'

  #  The functions Qt calls itself that QRemoteObjectNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setName': (
          ('_ZN17QRemoteObjectNode7setNameERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setRegistryUrl': (
          ('_ZN17QRemoteObjectNode14setRegistryUrlERK4QUrl',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
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
    Calls Qt's 'const QMetaObject *QRemoteObjectNode::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRemoteObjectNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QRemoteObjectNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str)
  def instances(self, typeName: str) -> QStringList:
    """
    Calls Qt's 'QStringList QRemoteObjectNode::instances(QStringView
    typeName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectnode.html#instances

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QRemoteObjectNode::instances(QStringView typeName) const
    address = self.uglySide.call(
        'ritual_ZNK17QRemoteObjectNode9instancesE11QStringView', typeName,
    )
    return QStringList._cuteOwning(address)

  def registryUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QRemoteObjectNode::registryUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectnode.html#registryUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QRemoteObjectNode::registryUrl() const
    address = self.uglySide.call(
        'ritual_ZNK17QRemoteObjectNode11registryUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def registry(self) -> Optional[QRemoteObjectRegistry]:
    """
    Calls Qt's 'const QRemoteObjectRegistry *QRemoteObjectNode::registry()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectnode.html#registry

    Returns
    -------

    Optional[QRemoteObjectRegistry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRemoteObjectRegistry *QRemoteObjectNode::registry() const
    address = self.uglySide.call('ritual_ZNK17QRemoteObjectNode8registryEv')
    from . import QRemoteObjectRegistry
    return QRemoteObjectRegistry._cuteAt(address)

  def persistedStore(self) -> Optional[QRemoteObjectAbstractPersistedStore]:
    """
    Calls Qt's 'QRemoteObjectAbstractPersistedStore
    *QRemoteObjectNode::persistedStore() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#persistedStore

    Returns
    -------

    Optional[QRemoteObjectAbstractPersistedStore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectAbstractPersistedStore
    #      *QRemoteObjectNode::persistedStore() const
    address = self.uglySide.call(
        'ritual_ZNK17QRemoteObjectNode14persistedStoreEv',
    )
    from . import QRemoteObjectAbstractPersistedStore
    return QRemoteObjectAbstractPersistedStore._cuteAt(address)

  def lastError(self) -> ErrorCode:
    """
    Calls Qt's 'ErrorCode QRemoteObjectNode::lastError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectnode.html#lastError

    Returns
    -------

    ErrorCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ErrorCode(number)' gives.
    """
    #  ErrorCode QRemoteObjectNode::lastError() const
    return QRemoteObjectNode.ErrorCode(self.uglySide.call(
        'ritual_ZNK17QRemoteObjectNode9lastErrorEv',
    ))

  def heartbeatInterval(self) -> int:
    """
    Calls Qt's 'int QRemoteObjectNode::heartbeatInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#heartbeatInterval
    """
    #  int QRemoteObjectNode::heartbeatInterval() const
    return self.uglySide.call(
        'ritual_ZNK17QRemoteObjectNode17heartbeatIntervalEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QRemoteObjectNode::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectnode.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QRemoteObjectNode::setName(const QString &name)
    ritual = 'ritual_ZN17QRemoteObjectNode7setNameERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QRemoteObjectNode7setNameERK7QString'
    self.uglySide.call(ritual, name)

  @overload(QUrl)
  def setRegistryUrl(self, registryAddress: QUrl) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectNode::setRegistryUrl(const QUrl
    &registryAddress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#setRegistryUrl

    Parameters
    ----------

    registryAddress : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QRemoteObjectNode::setRegistryUrl(const QUrl &registryAddress)
    ritual = 'ritual_ZN17QRemoteObjectNode14setRegistryUrlERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QRemoteObjectNode14setRegistryUrlERK4QUrl'
    return self.uglySide.call(ritual, self._valueOf(registryAddress))

  @overload(QRemoteObjectAbstractPersistedStore)
  @overload(NoneType)
  def setPersistedStore(
      self,
      persistedStore: Optional[QRemoteObjectAbstractPersistedStore],
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectNode::setPersistedStore(QRemoteObjectAbstractPersistedStore
    *persistedStore)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#setPersistedStore

    Parameters
    ----------

    persistedStore : Optional[QRemoteObjectAbstractPersistedStore]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectNode::setPersistedStore(
    #      QRemoteObjectAbstractPersistedStore *persistedStore)
    self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode17setPersistedStoreEP35QRemoteObjectAb'
        'stractPersistedStore',
        self._addressOf(persistedStore),
    )

  @overload(int)
  def setHeartbeatInterval(self, interval: int) -> None:
    """
    Calls Qt's 'void QRemoteObjectNode::setHeartbeatInterval(int interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#setHeartbeatInterval

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void QRemoteObjectNode::setHeartbeatInterval(int interval)
    self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode20setHeartbeatIntervalEi', interval,
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
    'QRemoteObjectNode::QRemoteObjectNode(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#QRemoteObjectNode

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRemoteObjectNode::QRemoteObjectNode(QObject *parent)
    self._noteCreation(QRemoteObjectNode, lambda: Rituals.call(
        'ritual_ZN17QRemoteObjectNodeC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QUrl)
  @overload(QUrl, QObject)
  @overload(QUrl, NoneType)
  def __init__(
      self,
      registryAddress: QUrl,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectNode::QRemoteObjectNode(const QUrl &registryAddress,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#QRemoteObjectNode

    Parameters
    ----------

    registryAddress : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRemoteObjectNode::QRemoteObjectNode(const QUrl &registryAddress,
    #      QObject *parent)
    self._noteCreation(QRemoteObjectNode, lambda: Rituals.call(
        'ritual_ZN17QRemoteObjectNodeC1ERK4QUrlP7QObject',
        self._valueOf(registryAddress), self._addressOf(parent, 'QObject'),
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

  @overload(QUrl)
  def connectToNode(self, address: QUrl) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectNode::connectToNode(const QUrl &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#connectToNode

    Parameters
    ----------

    address : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QRemoteObjectNode::connectToNode(const QUrl &address)
    return self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode13connectToNodeERK4QUrl',
        self._valueOf(address),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def addClientSideConnection(self, ioDevice: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QRemoteObjectNode::addClientSideConnection(QIODevice
    *ioDevice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#addClientSideConnection

    Parameters
    ----------

    ioDevice : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectNode::addClientSideConnection(QIODevice *ioDevice)
    self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode23addClientSideConnectionEP9QIODevice',
        self._addressOf(ioDevice),
    )

  @overload(str)
  def acquireDynamic(
      self,
      name: str,
  ) -> Optional[QRemoteObjectDynamicReplica]:
    """
    Calls Qt's 'QRemoteObjectDynamicReplica
    *QRemoteObjectNode::acquireDynamic(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#acquireDynamic

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QRemoteObjectDynamicReplica]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectDynamicReplica *QRemoteObjectNode::acquireDynamic(const
    #      QString &name)
    address = self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode14acquireDynamicERK7QString', name,
    )
    from . import QRemoteObjectDynamicReplica
    return QRemoteObjectDynamicReplica._cuteAt(address)

  @overload()
  @overload(int)
  def waitForRegistry(self, timeout: int = 30000) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectNode::waitForRegistry(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#waitForRegistry

    Parameters
    ----------

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QRemoteObjectNode::waitForRegistry(int timeout)
    return self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode15waitForRegistryEi', timeout,
    )

  @overload(QUrl)
  def registryUrlChanged(self, registryUrl: QUrl) -> None:
    """
    Calls Qt's 'void QRemoteObjectNode::registryUrlChanged(const QUrl
    &registryUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#registryUrlChanged

    Parameters
    ----------

    registryUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QRemoteObjectNode::registryUrlChanged(const QUrl &registryUrl)
    self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode18registryUrlChangedERK4QUrl',
        self._valueOf(registryUrl),
    )

  @overload(QRemoteObjectAbstractPersistedStore)
  @overload(NoneType)
  def persistedStoreChanged(
      self,
      persistedStore: Optional[QRemoteObjectAbstractPersistedStore],
  ) -> None:
    """
    Calls Qt's 'void QRemoteObjectNode::persistedStoreChanged(
    QRemoteObjectAbstractPersistedStore *persistedStore)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#persistedStoreChanged

    Parameters
    ----------

    persistedStore : Optional[QRemoteObjectAbstractPersistedStore]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectNode::persistedStoreChanged(
    #      QRemoteObjectAbstractPersistedStore *persistedStore)
    self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode21persistedStoreChangedEP35QRemoteObje'
        'ctAbstractPersistedStore',
        self._addressOf(persistedStore),
    )

  @overload(ErrorCode)
  def error(self, errorCode: ErrorCode) -> None:
    """
    Calls Qt's 'void QRemoteObjectNode::error(QRemoteObjectNode::ErrorCode
    errorCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectnode.html#error

    Parameters
    ----------

    errorCode : ErrorCode
      Passed on as its number.
    """
    #  void QRemoteObjectNode::error(QRemoteObjectNode::ErrorCode errorCode)
    self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode5errorENS_9ErrorCodeE', errorCode.value,
    )

  @overload(int)
  def heartbeatIntervalChanged(self, heartbeatInterval: int) -> None:
    """
    Calls Qt's 'void QRemoteObjectNode::heartbeatIntervalChanged(int
    heartbeatInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#heartbeatIntervalChanged

    Parameters
    ----------

    heartbeatInterval : int
      Passed on as it is.
    """
    #  void QRemoteObjectNode::heartbeatIntervalChanged(int
    #      heartbeatInterval)
    self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode24heartbeatIntervalChangedEi',
        heartbeatInterval,
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QRemoteObjectNode::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectnode.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectNode::timerEvent(QTimerEvent *a0)
    ritual = 'ritual_ZN17QRemoteObjectNode10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QRemoteObjectNode10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QRemoteObjectReplica)
  @overload(NoneType)
  @overload(QRemoteObjectReplica, str)
  @overload(NoneType, str)
  def initializeReplica(
      self,
      instance: Optional[QRemoteObjectReplica],
      name: str = '',
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectNode::initializeReplica(QRemoteObjectReplica *instance,
    const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#initializeReplica

    Parameters
    ----------

    instance : Optional[QRemoteObjectReplica]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QRemoteObjectNode::initializeReplica(QRemoteObjectReplica
    #      *instance, const QString &name)
    self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode17initializeReplicaEP20QRemoteObjectRe'
        'plicaRK7QString',
        self._addressOf(instance), name,
    )

  @overload(str, QByteArray, QList[QVariant])
  def persistProperties(
      self,
      repName: str,
      repSig: QByteArray,
      props: QList[QVariant],
  ) -> None:
    """
    Calls Qt's 'void QRemoteObjectNode::persistProperties(const QString
    &repName, const QByteArray &repSig, const QVariantList &props)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#persistProperties

    Parameters
    ----------

    repName : str
      Passed on as it is: a QString is made of it for the call.

    repSig : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    props : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QRemoteObjectNode::persistProperties(const QString &repName,
    #      const QByteArray &repSig, const QVariantList &props)
    self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode17persistPropertiesERK7QStringRK10QByt'
        'eArrayRK5QListI8QVariantE',
        repName, self._valueOf(repSig), self._valueOf(props),
    )

  @overload(str, QByteArray)
  def retrieveProperties(
      self,
      repName: str,
      repSig: QByteArray,
  ) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QRemoteObjectNode::retrieveProperties(const
    QString &repName, const QByteArray &repSig)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectnode.html#retrieveProperties

    Parameters
    ----------

    repName : str
      Passed on as it is: a QString is made of it for the call.

    repSig : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QRemoteObjectNode::retrieveProperties(const QString
    #      &repName, const QByteArray &repSig)
    address = self.uglySide.call(
        'ritual_ZN17QRemoteObjectNode18retrievePropertiesERK7QStringRK10QBy'
        'teArray',
        repName, self._valueOf(repSig),
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  def d_func(self) -> Optional[QRemoteObjectNodePrivate]:
    """
    Calls Qt's 'QRemoteObjectNodePrivate *QRemoteObjectNode::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qremoteobjectnode.html#d_func

    Returns
    -------

    Optional[QRemoteObjectNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectNodePrivate *QRemoteObjectNode::d_func()
    address = self.uglySide.call('ritual_ZN17QRemoteObjectNode6d_funcEv')
    from . import QRemoteObjectNodePrivate
    return QRemoteObjectNodePrivate._cuteAt(address)

  @staticmethod
  def acquire(*__, **_) -> Never:
    """
    Qt's 'QRemoteObjectNode::acquire': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QRemoteObjectNode.acquire' has no cute function yet. Qt's "
        "'QRemoteObjectNode::acquire': a template: a pattern and no single "
        "function.")

  @staticmethod
  def acquireModel(*__, **_) -> Never:
    """
    Qt's 'QAbstractItemModelReplica *QRemoteObjectNode::acquireModel(const
    QString &name, QtRemoteObjects::InitialAction action, const QList<int>
    &rolesHint)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectNode.acquireModel' has no cute function yet. Qt's "
        "'QAbstractItemModelReplica *QRemoteObjectNode::acquireModel(const "
        "QString &name, QtRemoteObjects::InitialAction action, const "
        "QList<int> &rolesHint)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def registerExternalSchema(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectNode::registerExternalSchema(const QString
    &schema, RemoteObjectSchemaHandler handler)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectNode.registerExternalSchema' has no cute function "
        "yet. Qt's 'void QRemoteObjectNode::registerExternalSchema(const "
        "QString &schema, RemoteObjectSchemaHandler handler)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def remoteObjectAdded(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectNode::remoteObjectAdded(const
    QRemoteObjectSourceLocation &a0)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectNode.remoteObjectAdded' has no cute function yet. "
        "Qt's 'void QRemoteObjectNode::remoteObjectAdded(const "
        "QRemoteObjectSourceLocation &a0)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def remoteObjectRemoved(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectNode::remoteObjectRemoved(const
    QRemoteObjectSourceLocation &a0)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QRemoteObjectNode.remoteObjectRemoved' has no cute function yet. "
        "Qt's 'void QRemoteObjectNode::remoteObjectRemoved(const "
        "QRemoteObjectSourceLocation &a0)': takes a type Python has no way "
        "to hand over yet.")
