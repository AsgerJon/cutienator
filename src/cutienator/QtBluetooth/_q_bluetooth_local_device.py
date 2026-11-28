"""
QBluetoothLocalDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qbluetoothlocaldevice.h, Qt 6.12.0. Changes made here are
#  lost.
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
  from . import QBluetoothAddress, QBluetoothHostInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothAddress = WAIT['QBluetoothAddress']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBluetoothLocalDevice(QObject):
  """
  The cute side of Qt's QBluetoothLocalDevice: a plain Python object standing
  in front of one C++ QBluetoothLocalDevice.

  It is built on the cute 'QObject', as Qt's QBluetoothLocalDevice is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBluetoothLocalDevice that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr', 'isValid',
  'requestPairing', 'pairingStatus', 'setHostMode', 'hostMode',
  'connectedDevices', 'powerOn', 'name', 'address', 'allDevices',
  'hostModeStateChanged', 'deviceConnected', 'deviceDisconnected',
  'pairingFinished', 'errorOccurred'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBluetoothLocalDevice::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QBluetoothLocalDevice::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QBluetoothLocalDevice::~QBluetoothLocalDevice()': the destructor:
    Python never removes a C++ QBluetoothLocalDevice.
  - Qt's 'QBluetoothLocalDevicePrivate *QBluetoothLocalDevice::d_func()':
    gives 'QBluetoothLocalDevicePrivate', which has no cute class yet.
  - Qt's 'const QBluetoothLocalDevicePrivate *QBluetoothLocalDevice::d_func()
    const': gives 'QBluetoothLocalDevicePrivate', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBluetoothLocalDevice is created at the first use, not by
    'QBluetoothLocalDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBluetoothLocalDevice.
  - Qt tells when it has removed the C++ QBluetoothLocalDevice. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QBluetoothLocalDevice, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QBluetoothLocalDevice::Error' of Qt, with the 4 names Qt gives
    in it.
    """

    NoError = Kee[int](0)
    PairingError = Kee[int](1)
    MissingPermissionsError = Kee[int](2)
    UnknownError = Kee[int](100)

  class HostMode(CuteNum):
    """
    The enum 'QBluetoothLocalDevice::HostMode' of Qt, with the 4 names Qt
    gives in it.
    """

    HostPoweredOff = Kee[int](0)
    HostConnectable = Kee[int](1)
    HostDiscoverable = Kee[int](2)
    HostDiscoverableLimitedInquiry = Kee[int](3)

  class Pairing(CuteNum):
    """
    The enum 'QBluetoothLocalDevice::Pairing' of Qt, with the 3 names Qt
    gives in it.
    """

    Unpaired = Kee[int](0)
    Paired = Kee[int](1)
    AuthorizedPaired = Kee[int](2)

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
    Calls Qt's 'QString QBluetoothLocalDevice::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#tr

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
    #  QString QBluetoothLocalDevice::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QBluetoothLocalDevice2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def allDevices() -> QList[QBluetoothHostInfo]:
    """
    Calls Qt's 'QList<QBluetoothHostInfo>
    QBluetoothLocalDevice::allDevices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#allDevices

    Returns
    -------

    QList[QBluetoothHostInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBluetoothHostInfo> QBluetoothLocalDevice::allDevices()
    address = Rituals.call('ritual_ZN21QBluetoothLocalDevice10allDevicesEv')
    from . import QBluetoothHostInfo
    return QList[QBluetoothHostInfo]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothLocalDevice'

  #  A C++ QBluetoothLocalDevice Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBluetoothLocalDevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBluetoothLocalDevice::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBluetoothLocalDevice::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QBluetoothLocalDevice10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothLocalDevice::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#isValid
    """
    #  bool QBluetoothLocalDevice::isValid() const
    return self.uglySide.call('ritual_ZNK21QBluetoothLocalDevice7isValidEv')

  @overload(QBluetoothAddress)
  def pairingStatus(self, address: QBluetoothAddress) -> Pairing:
    """
    Calls Qt's 'Pairing QBluetoothLocalDevice::pairingStatus(const
    QBluetoothAddress &address) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#pairingStatus

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    Returns
    -------

    Pairing
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Pairing(number)' gives.
    """
    #  Pairing QBluetoothLocalDevice::pairingStatus(const QBluetoothAddress
    #      &address) const
    return QBluetoothLocalDevice.Pairing(self.uglySide.call(
        'ritual_ZNK21QBluetoothLocalDevice13pairingStatusERK17QBluetoothAdd'
        'ress',
        self._valueOf(address),
    ))

  def hostMode(self) -> HostMode:
    """
    Calls Qt's 'HostMode QBluetoothLocalDevice::hostMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#hostMode

    Returns
    -------

    HostMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HostMode(number)' gives.
    """
    #  HostMode QBluetoothLocalDevice::hostMode() const
    return QBluetoothLocalDevice.HostMode(self.uglySide.call(
        'ritual_ZNK21QBluetoothLocalDevice8hostModeEv',
    ))

  def connectedDevices(self) -> QList[QBluetoothAddress]:
    """
    Calls Qt's 'QList<QBluetoothAddress>
    QBluetoothLocalDevice::connectedDevices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#connectedDevices

    Returns
    -------

    QList[QBluetoothAddress]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBluetoothAddress> QBluetoothLocalDevice::connectedDevices()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QBluetoothLocalDevice16connectedDevicesEv',
    )
    from . import QBluetoothAddress
    return QList[QBluetoothAddress]._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QBluetoothLocalDevice::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothLocalDevice::name() const
    return self.uglySide.call('ritual_ZNK21QBluetoothLocalDevice4nameEv')

  def address(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress QBluetoothLocalDevice::address() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#address

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QBluetoothLocalDevice::address() const
    address = self.uglySide.call(
        'ritual_ZNK21QBluetoothLocalDevice7addressEv',
    )
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(HostMode)
  def setHostMode(self, mode: HostMode) -> None:
    """
    Calls Qt's 'void
    QBluetoothLocalDevice::setHostMode(QBluetoothLocalDevice::HostMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#setHostMode

    Parameters
    ----------

    mode : HostMode
      Passed on as its number.
    """
    #  void
    #      QBluetoothLocalDevice::setHostMode(QBluetoothLocalDevice::HostMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN21QBluetoothLocalDevice11setHostModeENS_8HostModeE',
        mode.value,
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
    'QBluetoothLocalDevice::QBluetoothLocalDevice(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#QBluetoothLocalDevice

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBluetoothLocalDevice::QBluetoothLocalDevice(QObject *parent)
    self._noteCreation(QBluetoothLocalDevice, lambda: Rituals.call(
        'ritual_ZN21QBluetoothLocalDeviceC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QBluetoothAddress)
  @overload(QBluetoothAddress, QObject)
  @overload(QBluetoothAddress, NoneType)
  def __init__(
      self,
      address: QBluetoothAddress,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothLocalDevice::QBluetoothLocalDevice(const QBluetoothAddress
    &address, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#QBluetoothLocalDevice

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBluetoothLocalDevice::QBluetoothLocalDevice(const QBluetoothAddress
    #      &address, QObject *parent)
    self._noteCreation(QBluetoothLocalDevice, lambda: Rituals.call(
        'ritual_ZN21QBluetoothLocalDeviceC1ERK17QBluetoothAddressP7QObject',
        self._valueOf(address), self._addressOf(parent, 'QObject'),
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

  @overload(QBluetoothAddress, Pairing)
  def requestPairing(
      self,
      address: QBluetoothAddress,
      pairing: Pairing,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothLocalDevice::requestPairing(const
    QBluetoothAddress &address, Pairing pairing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#requestPairing

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    pairing : Pairing
      Passed on as its number.
    """
    #  void QBluetoothLocalDevice::requestPairing(const QBluetoothAddress
    #      &address, Pairing pairing)
    self.uglySide.call(
        'ritual_ZN21QBluetoothLocalDevice14requestPairingERK17QBluetoothAdd'
        'ressNS_7PairingE',
        self._valueOf(address), pairing.value,
    )

  def powerOn(self) -> None:
    """
    Calls Qt's 'void QBluetoothLocalDevice::powerOn()'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#powerOn
    """
    #  void QBluetoothLocalDevice::powerOn()
    self.uglySide.call('ritual_ZN21QBluetoothLocalDevice7powerOnEv')

  @overload(HostMode)
  def hostModeStateChanged(self, state: HostMode) -> None:
    """
    Calls Qt's 'void
    QBluetoothLocalDevice::hostModeStateChanged(QBluetoothLocalDevice::
    HostMode state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#hostModeStateChanged

    Parameters
    ----------

    state : HostMode
      Passed on as its number.
    """
    #  void QBluetoothLocalDevice::hostModeStateChanged(
    #      QBluetoothLocalDevice::HostMode state)
    self.uglySide.call(
        'ritual_ZN21QBluetoothLocalDevice20hostModeStateChangedENS_8HostMod'
        'eE',
        state.value,
    )

  @overload(QBluetoothAddress)
  def deviceConnected(self, address: QBluetoothAddress) -> None:
    """
    Calls Qt's 'void QBluetoothLocalDevice::deviceConnected(const
    QBluetoothAddress &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#deviceConnected

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.
    """
    #  void QBluetoothLocalDevice::deviceConnected(const QBluetoothAddress
    #      &address)
    self.uglySide.call(
        'ritual_ZN21QBluetoothLocalDevice15deviceConnectedERK17QBluetoothAd'
        'dress',
        self._valueOf(address),
    )

  @overload(QBluetoothAddress)
  def deviceDisconnected(self, address: QBluetoothAddress) -> None:
    """
    Calls Qt's 'void QBluetoothLocalDevice::deviceDisconnected(const
    QBluetoothAddress &address)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#deviceDisconnected

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.
    """
    #  void QBluetoothLocalDevice::deviceDisconnected(const QBluetoothAddress
    #      &address)
    self.uglySide.call(
        'ritual_ZN21QBluetoothLocalDevice18deviceDisconnectedERK17QBluetoot'
        'hAddress',
        self._valueOf(address),
    )

  @overload(QBluetoothAddress, Pairing)
  def pairingFinished(
      self,
      address: QBluetoothAddress,
      pairing: Pairing,
  ) -> None:
    """
    Calls Qt's 'void QBluetoothLocalDevice::pairingFinished(const
    QBluetoothAddress &address, QBluetoothLocalDevice::Pairing pairing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#pairingFinished

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    pairing : Pairing
      Passed on as its number.
    """
    #  void QBluetoothLocalDevice::pairingFinished(const QBluetoothAddress
    #      &address, QBluetoothLocalDevice::Pairing pairing)
    self.uglySide.call(
        'ritual_ZN21QBluetoothLocalDevice15pairingFinishedERK17QBluetoothAd'
        'dressNS_7PairingE',
        self._valueOf(address), pairing.value,
    )

  @overload(Error)
  def errorOccurred(self, error: Error) -> None:
    """
    Calls Qt's 'void
    QBluetoothLocalDevice::errorOccurred(QBluetoothLocalDevice::Error
    error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothlocaldevice.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.
    """
    #  void QBluetoothLocalDevice::errorOccurred(QBluetoothLocalDevice::Error
    #      error)
    self.uglySide.call(
        'ritual_ZN21QBluetoothLocalDevice13errorOccurredENS_5ErrorE',
        error.value,
    )
