"""
QBluetoothDeviceDiscoveryAgent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qbluetoothdevicediscoveryagent.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QBluetoothDeviceInfo

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QBluetoothAddress
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothAddress = WAIT['QBluetoothAddress']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBluetoothDeviceDiscoveryAgent(QObject):
  """
  The cute side of Qt's QBluetoothDeviceDiscoveryAgent: a plain Python object
  standing in front of one C++ QBluetoothDeviceDiscoveryAgent.

  It is built on the cute 'QObject', as Qt's QBluetoothDeviceDiscoveryAgent
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBluetoothDeviceDiscoveryAgent that has a ritual and
  that Python can call so far, 16 names in all: 'metaObject', 'tr',
  'isActive', 'error', 'errorString', 'discoveredDevices',
  'setLowEnergyDiscoveryTimeout', 'lowEnergyDiscoveryTimeout',
  'supportedDiscoveryMethods', 'start', 'stop', 'deviceDiscovered',
  'deviceUpdated', 'finished', 'errorOccurred', 'canceled'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBluetoothDeviceDiscoveryAgent::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QBluetoothDeviceDiscoveryAgent::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QBluetoothDeviceDiscoveryAgent::~QBluetoothDeviceDiscoveryAgent()':
    the destructor: Python never removes a C++
    QBluetoothDeviceDiscoveryAgent.
  - Qt's 'QBluetoothDeviceDiscoveryAgentPrivate
    *QBluetoothDeviceDiscoveryAgent::d_func()': gives
    'QBluetoothDeviceDiscoveryAgentPrivate', which has no cute class yet.
  - Qt's 'const QBluetoothDeviceDiscoveryAgentPrivate
    *QBluetoothDeviceDiscoveryAgent::d_func() const': gives
    'QBluetoothDeviceDiscoveryAgentPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBluetoothDeviceDiscoveryAgent is created at the first use, not
    by 'QBluetoothDeviceDiscoveryAgent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBluetoothDeviceDiscoveryAgent.
  - Qt tells when it has removed the C++ QBluetoothDeviceDiscoveryAgent.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QBluetoothDeviceDiscoveryAgent, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class DiscoveryMethod(CuteFlags):
    """
    The flags enum 'QBluetoothDeviceDiscoveryAgent::DiscoveryMethod' of Qt,
    with the 3 names Qt gives in it. Qt names the type of its combinations
    'QBluetoothDeviceDiscoveryAgent::DiscoveryMethods'.
    """

    NoMethod = 0x0
    ClassicMethod = 0x1
    LowEnergyMethod = 0x2

  DiscoveryMethods = DiscoveryMethod

  class Error(CuteNum):
    """
    The enum 'QBluetoothDeviceDiscoveryAgent::Error' of Qt, with the 9 names
    Qt gives in it.
    """

    NoError = Kee[int](0)
    InputOutputError = Kee[int](1)
    PoweredOffError = Kee[int](2)
    InvalidBluetoothAdapterError = Kee[int](3)
    UnsupportedPlatformError = Kee[int](4)
    UnsupportedDiscoveryMethod = Kee[int](5)
    LocationServiceTurnedOffError = Kee[int](6)
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
    Calls Qt's 'QString QBluetoothDeviceDiscoveryAgent::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html#tr

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
    #  QString QBluetoothDeviceDiscoveryAgent::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QBluetoothDeviceDiscoveryAgent2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def supportedDiscoveryMethods() -> DiscoveryMethods:
    """
    Calls Qt's 'DiscoveryMethods
    QBluetoothDeviceDiscoveryAgent::supportedDiscoveryMethods()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html

    Returns
    -------

    DiscoveryMethods
      The value standing for the combination Qt gave back.
    """
    #  DiscoveryMethods
    #      QBluetoothDeviceDiscoveryAgent::supportedDiscoveryMethods()
    return QBluetoothDeviceDiscoveryAgent.DiscoveryMethods(Rituals.call(
        'ritual_ZN30QBluetoothDeviceDiscoveryAgent25supportedDiscoveryMetho'
        'dsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothDeviceDiscoveryAgent'

  #  A C++ QBluetoothDeviceDiscoveryAgent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBluetoothDeviceDiscoveryAgent'

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
    *QBluetoothDeviceDiscoveryAgent::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBluetoothDeviceDiscoveryAgent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QBluetoothDeviceDiscoveryAgent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothDeviceDiscoveryAgent::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html#isActive
    """
    #  bool QBluetoothDeviceDiscoveryAgent::isActive() const
    return self.uglySide.call(
        'ritual_ZNK30QBluetoothDeviceDiscoveryAgent8isActiveEv',
    )

  def error(self) -> Error:
    """
    Calls Qt's 'Error QBluetoothDeviceDiscoveryAgent::error() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QBluetoothDeviceDiscoveryAgent::error() const
    return QBluetoothDeviceDiscoveryAgent.Error(self.uglySide.call(
        'ritual_ZNK30QBluetoothDeviceDiscoveryAgent5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QBluetoothDeviceDiscoveryAgent::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothDeviceDiscoveryAgent::errorString() const
    return self.uglySide.call(
        'ritual_ZNK30QBluetoothDeviceDiscoveryAgent11errorStringEv',
    )

  def discoveredDevices(self) -> QList[QBluetoothDeviceInfo]:
    """
    Calls Qt's 'QList<QBluetoothDeviceInfo>
    QBluetoothDeviceDiscoveryAgent::discoveredDevices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html

    Returns
    -------

    QList[QBluetoothDeviceInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBluetoothDeviceInfo>
    #      QBluetoothDeviceDiscoveryAgent::discoveredDevices() const
    address = self.uglySide.call(
        'ritual_ZNK30QBluetoothDeviceDiscoveryAgent17discoveredDevicesEv',
    )
    return QList[QBluetoothDeviceInfo]._cuteOwning(address)

  def lowEnergyDiscoveryTimeout(self) -> int:
    """
    Calls Qt's 'int
    QBluetoothDeviceDiscoveryAgent::lowEnergyDiscoveryTimeout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html
    """
    #  int QBluetoothDeviceDiscoveryAgent::lowEnergyDiscoveryTimeout() const
    return self.uglySide.call(
        'ritual_ZNK30QBluetoothDeviceDiscoveryAgent25lowEnergyDiscoveryTime'
        'outEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLowEnergyDiscoveryTimeout(self, msTimeout: int) -> None:
    """
    Calls Qt's 'void
    QBluetoothDeviceDiscoveryAgent::setLowEnergyDiscoveryTimeout(int
    msTimeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html

    Parameters
    ----------

    msTimeout : int
      Passed on as it is.
    """
    #  void QBluetoothDeviceDiscoveryAgent::setLowEnergyDiscoveryTimeout(int
    #      msTimeout)
    self.uglySide.call(
        'ritual_ZN30QBluetoothDeviceDiscoveryAgent28setLowEnergyDiscoveryTi'
        'meoutEi',
        msTimeout,
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
    'QBluetoothDeviceDiscoveryAgent::QBluetoothDeviceDiscoveryAgent(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBluetoothDeviceDiscoveryAgent::QBluetoothDeviceDiscoveryAgent(QObject
    #      *parent)
    self._noteCreation(QBluetoothDeviceDiscoveryAgent, lambda: Rituals.call(
        'ritual_ZN30QBluetoothDeviceDiscoveryAgentC1EP7QObject',
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
    'QBluetoothDeviceDiscoveryAgent::QBluetoothDeviceDiscoveryAgent(const
    QBluetoothAddress &deviceAdapter, QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html

    Parameters
    ----------

    deviceAdapter : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBluetoothDeviceDiscoveryAgent::QBluetoothDeviceDiscoveryAgent(const
    #      QBluetoothAddress &deviceAdapter, QObject *parent)
    self._noteCreation(QBluetoothDeviceDiscoveryAgent, lambda: Rituals.call(
        'ritual_ZN30QBluetoothDeviceDiscoveryAgentC1ERK17QBluetoothAddressP'
        '7QObject',
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

  @overload()
  def start(self) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceDiscoveryAgent::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html#start
    """
    #  void QBluetoothDeviceDiscoveryAgent::start()
    self.uglySide.call('ritual_ZN30QBluetoothDeviceDiscoveryAgent5startEv')

  @overload(DiscoveryMethods)
  def start(self, method: DiscoveryMethods) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceDiscoveryAgent::start(DiscoveryMethods
    method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html#start

    Parameters
    ----------

    method : DiscoveryMethods
      Passed on as its number.
    """
    #  void QBluetoothDeviceDiscoveryAgent::start(DiscoveryMethods method)
    self.uglySide.call(
        'ritual_ZN30QBluetoothDeviceDiscoveryAgent5startE6QFlagsINS_15Disco'
        'veryMethodEE',
        method.value,
    )

  def stop(self) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceDiscoveryAgent::stop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html#stop
    """
    #  void QBluetoothDeviceDiscoveryAgent::stop()
    self.uglySide.call('ritual_ZN30QBluetoothDeviceDiscoveryAgent4stopEv')

  @overload(QBluetoothDeviceInfo)
  def deviceDiscovered(self, info: QBluetoothDeviceInfo) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceDiscoveryAgent::deviceDiscovered(const
    QBluetoothDeviceInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html

    Parameters
    ----------

    info : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.
    """
    #  void QBluetoothDeviceDiscoveryAgent::deviceDiscovered(const
    #      QBluetoothDeviceInfo &info)
    self.uglySide.call(
        'ritual_ZN30QBluetoothDeviceDiscoveryAgent16deviceDiscoveredERK20QB'
        'luetoothDeviceInfo',
        self._valueOf(info),
    )

  @overload(QBluetoothDeviceInfo, QBluetoothDeviceInfo.Fields)
  def deviceUpdated(
      self,
      info: QBluetoothDeviceInfo,
      updatedFields: QBluetoothDeviceInfo.Fields,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceDiscoveryAgent::deviceUpdated(const
    QBluetoothDeviceInfo &info, QBluetoothDeviceInfo::Fields updatedFields)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html#deviceUpdated

    Parameters
    ----------

    info : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.

    updatedFields : QBluetoothDeviceInfo.Fields
      Passed on as its number.
    """
    #  void QBluetoothDeviceDiscoveryAgent::deviceUpdated(const
    #      QBluetoothDeviceInfo &info, QBluetoothDeviceInfo::Fields
    #      updatedFields)
    self.uglySide.call(
        'ritual_ZN30QBluetoothDeviceDiscoveryAgent13deviceUpdatedERK20QBlue'
        'toothDeviceInfo6QFlagsINS0_5FieldEE',
        self._valueOf(info), updatedFields.value,
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceDiscoveryAgent::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html#finished
    """
    #  void QBluetoothDeviceDiscoveryAgent::finished()
    self.uglySide.call(
        'ritual_ZN30QBluetoothDeviceDiscoveryAgent8finishedEv',
    )

  @overload(Error)
  def errorOccurred(self, error: Error) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceDiscoveryAgent::errorOccurred(
    QBluetoothDeviceDiscoveryAgent::Error error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.
    """
    #  void QBluetoothDeviceDiscoveryAgent::errorOccurred(
    #      QBluetoothDeviceDiscoveryAgent::Error error)
    self.uglySide.call(
        'ritual_ZN30QBluetoothDeviceDiscoveryAgent13errorOccurredENS_5Error'
        'E',
        error.value,
    )

  def canceled(self) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceDiscoveryAgent::canceled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdevicediscoveryagent.html#canceled
    """
    #  void QBluetoothDeviceDiscoveryAgent::canceled()
    self.uglySide.call(
        'ritual_ZN30QBluetoothDeviceDiscoveryAgent8canceledEv',
    )
