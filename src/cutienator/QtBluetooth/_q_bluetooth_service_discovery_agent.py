"""
QBluetoothServiceDiscoveryAgent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qbluetoothservicediscoveryagent.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QBluetoothAddress, QBluetoothServiceDiscoveryAgentPrivate
  from . import QBluetoothServiceInfo, QBluetoothUuid
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothAddress = WAIT['QBluetoothAddress']
  QBluetoothServiceInfo = WAIT['QBluetoothServiceInfo']
  QBluetoothUuid = WAIT['QBluetoothUuid']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBluetoothServiceDiscoveryAgent(QObject):
  """
  The cute side of Qt's QBluetoothServiceDiscoveryAgent: a plain Python
  object standing in front of one C++ QBluetoothServiceDiscoveryAgent.

  It is built on the cute 'QObject', as Qt's QBluetoothServiceDiscoveryAgent
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBluetoothServiceDiscoveryAgent that has a ritual
  and that Python can call so far, 18 names in all: 'metaObject', 'tr',
  'd_func', 'isActive', 'error', 'errorString', 'discoveredServices',
  'setUuidFilter', 'uuidFilter', 'setRemoteAddress', 'remoteAddress',
  'start', 'stop', 'clear', 'serviceDiscovered', 'finished', 'canceled',
  'errorOccurred'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBluetoothServiceDiscoveryAgent::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QBluetoothServiceDiscoveryAgent::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QBluetoothServiceDiscoveryAgentPrivate
    *QBluetoothServiceDiscoveryAgent::d_func() const': takes in Python what
    'QBluetoothServiceDiscoveryAgentPrivate
    *QBluetoothServiceDiscoveryAgent::d_func()' takes.
  - Qt's
    'QBluetoothServiceDiscoveryAgent::~QBluetoothServiceDiscoveryAgent()':
    the destructor: Python never removes a C++
    QBluetoothServiceDiscoveryAgent.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBluetoothServiceDiscoveryAgent is created at the first use, not
    by 'QBluetoothServiceDiscoveryAgent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBluetoothServiceDiscoveryAgent.
  - Qt tells when it has removed the C++ QBluetoothServiceDiscoveryAgent.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QBluetoothServiceDiscoveryAgent, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class DiscoveryMode(CuteNum):
    """
    The enum 'QBluetoothServiceDiscoveryAgent::DiscoveryMode' of Qt, with the
    2 names Qt gives in it.
    """

    MinimalDiscovery = Kee[int](0)
    FullDiscovery = Kee[int](1)

  class Error(CuteNum):
    """
    The enum 'QBluetoothServiceDiscoveryAgent::Error' of Qt, with the 6 names
    Qt gives in it.
    """

    NoError = Kee[int](0)
    InputOutputError = Kee[int](1)
    PoweredOffError = Kee[int](2)
    InvalidBluetoothAdapterError = Kee[int](3)
    MissingPermissionsError = Kee[int](7)
    UnknownError = Kee[int](100)

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
    Calls Qt's 'QString QBluetoothServiceDiscoveryAgent::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#tr

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
    #  QString QBluetoothServiceDiscoveryAgent::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QBluetoothServiceDiscoveryAgent2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothServiceDiscoveryAgent'

  #  A C++ QBluetoothServiceDiscoveryAgent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBluetoothServiceDiscoveryAgent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QBluetoothServiceDiscoveryAgent::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBluetoothServiceDiscoveryAgent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QBluetoothServiceDiscoveryAgent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothServiceDiscoveryAgent::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#isActive
    """
    #  bool QBluetoothServiceDiscoveryAgent::isActive() const
    return self.uglySide.call(
        'ritual_ZNK31QBluetoothServiceDiscoveryAgent8isActiveEv',
    )

  def error(self) -> Error:
    """
    Calls Qt's 'Error QBluetoothServiceDiscoveryAgent::error() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QBluetoothServiceDiscoveryAgent::error() const
    return QBluetoothServiceDiscoveryAgent.Error(self.uglySide.call(
        'ritual_ZNK31QBluetoothServiceDiscoveryAgent5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QBluetoothServiceDiscoveryAgent::errorString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothServiceDiscoveryAgent::errorString() const
    return self.uglySide.call(
        'ritual_ZNK31QBluetoothServiceDiscoveryAgent11errorStringEv',
    )

  def discoveredServices(self) -> QList[QBluetoothServiceInfo]:
    """
    Calls Qt's 'QList<QBluetoothServiceInfo>
    QBluetoothServiceDiscoveryAgent::discoveredServices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html

    Returns
    -------

    QList[QBluetoothServiceInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBluetoothServiceInfo>
    #      QBluetoothServiceDiscoveryAgent::discoveredServices() const
    address = self.uglySide.call(
        'ritual_ZNK31QBluetoothServiceDiscoveryAgent18discoveredServicesEv',
    )
    from . import QBluetoothServiceInfo
    return QList[QBluetoothServiceInfo]._cuteOwning(address)

  def uuidFilter(self) -> QList[QBluetoothUuid]:
    """
    Calls Qt's 'QList<QBluetoothUuid>
    QBluetoothServiceDiscoveryAgent::uuidFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#uuidFilter

    Returns
    -------

    QList[QBluetoothUuid]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBluetoothUuid> QBluetoothServiceDiscoveryAgent::uuidFilter()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QBluetoothServiceDiscoveryAgent10uuidFilterEv',
    )
    from . import QBluetoothUuid
    return QList[QBluetoothUuid]._cuteOwning(address)

  def remoteAddress(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress
    QBluetoothServiceDiscoveryAgent::remoteAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#remoteAddress

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QBluetoothServiceDiscoveryAgent::remoteAddress()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QBluetoothServiceDiscoveryAgent13remoteAddressEv',
    )
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QBluetoothUuid])
  def setUuidFilter(self, uuids: QList[QBluetoothUuid]) -> None:
    """
    Calls Qt's 'void QBluetoothServiceDiscoveryAgent::setUuidFilter(const
    QList<QBluetoothUuid> &uuids)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#setUuidFilter

    Parameters
    ----------

    uuids : QList[QBluetoothUuid]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBluetoothServiceDiscoveryAgent::setUuidFilter(const
    #      QList<QBluetoothUuid> &uuids)
    self.uglySide.call(
        'ritual_ZN31QBluetoothServiceDiscoveryAgent13setUuidFilterERK5QList'
        'I14QBluetoothUuidE',
        self._valueOf(uuids),
    )

  @overload(QBluetoothUuid)
  def setUuidFilter(self, uuid: QBluetoothUuid) -> None:
    """
    Calls Qt's 'void QBluetoothServiceDiscoveryAgent::setUuidFilter(const
    QBluetoothUuid &uuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#setUuidFilter

    Parameters
    ----------

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.
    """
    #  void QBluetoothServiceDiscoveryAgent::setUuidFilter(const
    #      QBluetoothUuid &uuid)
    self.uglySide.call(
        'ritual_ZN31QBluetoothServiceDiscoveryAgent13setUuidFilterERK14QBlu'
        'etoothUuid',
        self._valueOf(uuid),
    )

  @overload(QBluetoothAddress)
  def setRemoteAddress(self, address: QBluetoothAddress) -> bool:
    """
    Calls Qt's 'bool QBluetoothServiceDiscoveryAgent::setRemoteAddress(const
    QBluetoothAddress &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.
    """
    #  bool QBluetoothServiceDiscoveryAgent::setRemoteAddress(const
    #      QBluetoothAddress &address)
    return self.uglySide.call(
        'ritual_ZN31QBluetoothServiceDiscoveryAgent16setRemoteAddressERK17Q'
        'BluetoothAddress',
        self._valueOf(address),
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
    'QBluetoothServiceDiscoveryAgent::QBluetoothServiceDiscoveryAgent(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBluetoothServiceDiscoveryAgent::QBluetoothServiceDiscoveryAgent(
    #      QObject *parent)
    self._noteCreation(QBluetoothServiceDiscoveryAgent, lambda: Rituals.call(
        'ritual_ZN31QBluetoothServiceDiscoveryAgentC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QBluetoothAddress)
  @overload(QBluetoothAddress, QObject)
  @overload(QBluetoothAddress, NoneType)
  def __init__(
      self,
      deviceAdapter: QBluetoothAddress,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothServiceDiscoveryAgent::QBluetoothServiceDiscoveryAgent(const
    QBluetoothAddress &deviceAdapter, QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html

    Parameters
    ----------

    deviceAdapter : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBluetoothServiceDiscoveryAgent::QBluetoothServiceDiscoveryAgent(const
    #      QBluetoothAddress &deviceAdapter, QObject *parent)
    self._noteCreation(QBluetoothServiceDiscoveryAgent, lambda: Rituals.call(
        'ritual_ZN31QBluetoothServiceDiscoveryAgentC1ERK17QBluetoothAddress'
        'P7QObject',
        self._valueOf(deviceAdapter), self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QBluetoothServiceDiscoveryAgentPrivate]:
    """
    Calls Qt's 'QBluetoothServiceDiscoveryAgentPrivate
    *QBluetoothServiceDiscoveryAgent::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#d_func

    Returns
    -------

    Optional[QBluetoothServiceDiscoveryAgentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBluetoothServiceDiscoveryAgentPrivate
    #      *QBluetoothServiceDiscoveryAgent::d_func()
    address = self.uglySide.call(
        'ritual_ZN31QBluetoothServiceDiscoveryAgent6d_funcEv',
    )
    from . import QBluetoothServiceDiscoveryAgentPrivate
    return QBluetoothServiceDiscoveryAgentPrivate._cuteAt(address)

  @overload()
  @overload(DiscoveryMode)
  def start(
      self,
      mode: DiscoveryMode = DiscoveryMode.MinimalDiscovery,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothServiceDiscoveryAgent::start(DiscoveryMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#start

    Parameters
    ----------

    mode : DiscoveryMode
      Passed on as its number. May be left out, as in Qt: it is then
      DiscoveryMode.MinimalDiscovery.
    """
    #  void QBluetoothServiceDiscoveryAgent::start(DiscoveryMode mode)
    self.uglySide.call(
        'ritual_ZN31QBluetoothServiceDiscoveryAgent5startENS_13DiscoveryMod'
        'eE',
        mode.value,
    )

  def stop(self) -> None:
    """
    Calls Qt's 'void QBluetoothServiceDiscoveryAgent::stop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#stop
    """
    #  void QBluetoothServiceDiscoveryAgent::stop()
    self.uglySide.call('ritual_ZN31QBluetoothServiceDiscoveryAgent4stopEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QBluetoothServiceDiscoveryAgent::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#clear
    """
    #  void QBluetoothServiceDiscoveryAgent::clear()
    self.uglySide.call('ritual_ZN31QBluetoothServiceDiscoveryAgent5clearEv')

  @overload(QBluetoothServiceInfo)
  def serviceDiscovered(self, info: QBluetoothServiceInfo) -> None:
    """
    Calls Qt's 'void QBluetoothServiceDiscoveryAgent::serviceDiscovered(const
    QBluetoothServiceInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html

    Parameters
    ----------

    info : QBluetoothServiceInfo
      Passed on as a value: Qt reads the C++ QBluetoothServiceInfo, which
      stays Python's own.
    """
    #  void QBluetoothServiceDiscoveryAgent::serviceDiscovered(const
    #      QBluetoothServiceInfo &info)
    self.uglySide.call(
        'ritual_ZN31QBluetoothServiceDiscoveryAgent17serviceDiscoveredERK21'
        'QBluetoothServiceInfo',
        self._valueOf(info),
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QBluetoothServiceDiscoveryAgent::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#finished
    """
    #  void QBluetoothServiceDiscoveryAgent::finished()
    self.uglySide.call(
        'ritual_ZN31QBluetoothServiceDiscoveryAgent8finishedEv',
    )

  def canceled(self) -> None:
    """
    Calls Qt's 'void QBluetoothServiceDiscoveryAgent::canceled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#canceled
    """
    #  void QBluetoothServiceDiscoveryAgent::canceled()
    self.uglySide.call(
        'ritual_ZN31QBluetoothServiceDiscoveryAgent8canceledEv',
    )

  @overload(Error)
  def errorOccurred(self, error: Error) -> None:
    """
    Calls Qt's 'void QBluetoothServiceDiscoveryAgent::errorOccurred(
    QBluetoothServiceDiscoveryAgent::Error error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagent.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.
    """
    #  void QBluetoothServiceDiscoveryAgent::errorOccurred(
    #      QBluetoothServiceDiscoveryAgent::Error error)
    self.uglySide.call(
        'ritual_ZN31QBluetoothServiceDiscoveryAgent13errorOccurredENS_5Erro'
        'rE',
        error.value,
    )
