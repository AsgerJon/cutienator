"""
QLowEnergyController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qlowenergycontroller.h, Qt 6.12.0. Changes made here are lost.
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
  from . import QBluetoothAddress, QBluetoothDeviceInfo, QBluetoothUuid
  from . import QLowEnergyAdvertisingData, QLowEnergyAdvertisingParameters
  from . import QLowEnergyConnectionParameters, QLowEnergyControllerPrivate
  from . import QLowEnergyService, QLowEnergyServiceData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothAddress = WAIT['QBluetoothAddress']
  QBluetoothDeviceInfo = WAIT['QBluetoothDeviceInfo']
  QBluetoothUuid = WAIT['QBluetoothUuid']
  QLowEnergyAdvertisingData = WAIT['QLowEnergyAdvertisingData']
  QLowEnergyAdvertisingParameters = WAIT['QLowEnergyAdvertisingParameters']
  QLowEnergyConnectionParameters = WAIT['QLowEnergyConnectionParameters']
  QLowEnergyServiceData = WAIT['QLowEnergyServiceData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLowEnergyController(QObject):
  """
  The cute side of Qt's QLowEnergyController: a plain Python object standing
  in front of one C++ QLowEnergyController.

  It is built on the cute 'QObject', as Qt's QLowEnergyController is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLowEnergyController that has a ritual and that
  Python can call so far, 35 names in all: 'metaObject', 'tr',
  'createCentral', 'createPeripheral', 'localAddress', 'remoteAddress',
  'remoteDeviceUuid', 'remoteName', 'state', 'remoteAddressType',
  'setRemoteAddressType', 'connectToDevice', 'disconnectFromDevice',
  'discoverServices', 'services', 'createServiceObject', 'startAdvertising',
  'stopAdvertising', 'addService', 'requestConnectionUpdate', 'error',
  'errorString', 'role', 'mtu', 'readRssi', 'connected', 'disconnected',
  'stateChanged', 'errorOccurred', 'mtuChanged', 'rssiRead',
  'serviceDiscovered', 'discoveryFinished', 'connectionUpdated', 'd_func'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLowEnergyController::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QLowEnergyController::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QLowEnergyController::~QLowEnergyController()': the destructor:
    Python never removes a C++ QLowEnergyController.
  - Qt's 'const QLowEnergyControllerPrivate *QLowEnergyController::d_func()
    const': takes in Python what 'QLowEnergyControllerPrivate
    *QLowEnergyController::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 45 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QLowEnergyController is created at the first use, not by
    'QLowEnergyController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLowEnergyController.
  - Qt tells when it has removed the C++ QLowEnergyController. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QLowEnergyController, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ControllerState(CuteNum):
    """
    The enum 'QLowEnergyController::ControllerState' of Qt, with the 7 names
    Qt gives in it.
    """

    UnconnectedState = Kee[int](0)
    ConnectingState = Kee[int](1)
    ConnectedState = Kee[int](2)
    DiscoveringState = Kee[int](3)
    DiscoveredState = Kee[int](4)
    ClosingState = Kee[int](5)
    AdvertisingState = Kee[int](6)

  class Error(CuteNum):
    """
    The enum 'QLowEnergyController::Error' of Qt, with the 11 names Qt gives
    in it.
    """

    NoError = Kee[int](0)
    UnknownError = Kee[int](1)
    UnknownRemoteDeviceError = Kee[int](2)
    NetworkError = Kee[int](3)
    InvalidBluetoothAdapterError = Kee[int](4)
    ConnectionError = Kee[int](5)
    AdvertisingError = Kee[int](6)
    RemoteHostClosedError = Kee[int](7)
    AuthorizationError = Kee[int](8)
    MissingPermissionsError = Kee[int](9)
    RssiReadError = Kee[int](10)

  class RemoteAddressType(CuteNum):
    """
    The enum 'QLowEnergyController::RemoteAddressType' of Qt, with the 2
    names Qt gives in it.
    """

    PublicAddress = Kee[int](0)
    RandomAddress = Kee[int](1)

  class Role(CuteNum):
    """
    The enum 'QLowEnergyController::Role' of Qt, with the 2 names Qt gives in
    it.
    """

    CentralRole = Kee[int](0)
    PeripheralRole = Kee[int](1)

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
    Calls Qt's 'QString QLowEnergyController::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergycontroller.html#tr

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
    #  QString QLowEnergyController::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QLowEnergyController2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QBluetoothDeviceInfo)
  @overload(QBluetoothDeviceInfo, QObject)
  @overload(QBluetoothDeviceInfo, NoneType)
  def createCentral(
      remoteDevice: QBluetoothDeviceInfo,
      parent: Optional[QObject] = None,
  ) -> Optional[QLowEnergyController]:
    """
    Calls Qt's 'QLowEnergyController
    *QLowEnergyController::createCentral(const QBluetoothDeviceInfo
    &remoteDevice, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#createCentral

    Parameters
    ----------

    remoteDevice : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QLowEnergyController]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLowEnergyController *QLowEnergyController::createCentral(const
    #      QBluetoothDeviceInfo &remoteDevice, QObject *parent)
    address = Rituals.call(
        'ritual_ZN20QLowEnergyController13createCentralERK20QBluetoothDevic'
        'eInfoP7QObject',
        CuteMixin._valueOf(remoteDevice), CuteMixin._addressOf(parent,
        'QObject'),
    )
    return QLowEnergyController._cuteAt(address)

  @staticmethod
  @overload(QBluetoothDeviceInfo, QBluetoothAddress)
  @overload(QBluetoothDeviceInfo, QBluetoothAddress, QObject)
  @overload(QBluetoothDeviceInfo, QBluetoothAddress, NoneType)
  def createCentral(
      remoteDevice: QBluetoothDeviceInfo,
      localDevice: QBluetoothAddress,
      parent: Optional[QObject] = None,
  ) -> Optional[QLowEnergyController]:
    """
    Calls Qt's 'QLowEnergyController
    *QLowEnergyController::createCentral(const QBluetoothDeviceInfo
    &remoteDevice, const QBluetoothAddress &localDevice, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#createCentral

    Parameters
    ----------

    remoteDevice : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.

    localDevice : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QLowEnergyController]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLowEnergyController *QLowEnergyController::createCentral(const
    #      QBluetoothDeviceInfo &remoteDevice, const QBluetoothAddress
    #      &localDevice, QObject *parent)
    address = Rituals.call(
        'ritual_ZN20QLowEnergyController13createCentralERK20QBluetoothDevic'
        'eInfoRK17QBluetoothAddressP7QObject',
        CuteMixin._valueOf(remoteDevice), CuteMixin._valueOf(localDevice),
        CuteMixin._addressOf(parent, 'QObject'),
    )
    return QLowEnergyController._cuteAt(address)

  @staticmethod
  @overload(QBluetoothAddress)
  @overload(QBluetoothAddress, QObject)
  @overload(QBluetoothAddress, NoneType)
  def createPeripheral(
      localDevice: QBluetoothAddress,
      parent: Optional[QObject] = None,
  ) -> Optional[QLowEnergyController]:
    """
    Calls Qt's 'QLowEnergyController
    *QLowEnergyController::createPeripheral(const QBluetoothAddress
    &localDevice, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#createPeripheral

    Parameters
    ----------

    localDevice : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QLowEnergyController]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLowEnergyController *QLowEnergyController::createPeripheral(const
    #      QBluetoothAddress &localDevice, QObject *parent)
    address = Rituals.call(
        'ritual_ZN20QLowEnergyController16createPeripheralERK17QBluetoothAd'
        'dressP7QObject',
        CuteMixin._valueOf(localDevice), CuteMixin._addressOf(parent,
        'QObject'),
    )
    return QLowEnergyController._cuteAt(address)

  @staticmethod
  @overload()
  @overload(QObject)
  @overload(NoneType)
  def createPeripheral(
      parent: Optional[QObject] = None,
  ) -> Optional[QLowEnergyController]:
    """
    Calls Qt's 'QLowEnergyController
    *QLowEnergyController::createPeripheral(QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#createPeripheral

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QLowEnergyController]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLowEnergyController *QLowEnergyController::createPeripheral(QObject
    #      *parent)
    address = Rituals.call(
        'ritual_ZN20QLowEnergyController16createPeripheralEP7QObject',
        CuteMixin._addressOf(parent, 'QObject'),
    )
    return QLowEnergyController._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLowEnergyController'

  #  A C++ QLowEnergyController Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLowEnergyController'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLowEnergyController::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLowEnergyController::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QLowEnergyController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def localAddress(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress QLowEnergyController::localAddress()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#localAddress

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QLowEnergyController::localAddress() const
    address = self.uglySide.call(
        'ritual_ZNK20QLowEnergyController12localAddressEv',
    )
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  def remoteAddress(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress QLowEnergyController::remoteAddress()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#remoteAddress

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QLowEnergyController::remoteAddress() const
    address = self.uglySide.call(
        'ritual_ZNK20QLowEnergyController13remoteAddressEv',
    )
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  def remoteDeviceUuid(self) -> QBluetoothUuid:
    """
    Calls Qt's 'QBluetoothUuid QLowEnergyController::remoteDeviceUuid()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#remoteDeviceUuid

    Returns
    -------

    QBluetoothUuid
      A new cute QBluetoothUuid around the copy Qt gave back. Python owns it.
    """
    #  QBluetoothUuid QLowEnergyController::remoteDeviceUuid() const
    address = self.uglySide.call(
        'ritual_ZNK20QLowEnergyController16remoteDeviceUuidEv',
    )
    from . import QBluetoothUuid
    return QBluetoothUuid._cuteOwning(address)

  def remoteName(self) -> str:
    """
    Calls Qt's 'QString QLowEnergyController::remoteName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#remoteName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLowEnergyController::remoteName() const
    return self.uglySide.call(
        'ritual_ZNK20QLowEnergyController10remoteNameEv',
    )

  def state(self) -> ControllerState:
    """
    Calls Qt's 'ControllerState QLowEnergyController::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergycontroller.html#state

    Returns
    -------

    ControllerState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ControllerState(number)'
      gives.
    """
    #  ControllerState QLowEnergyController::state() const
    return QLowEnergyController.ControllerState(self.uglySide.call(
        'ritual_ZNK20QLowEnergyController5stateEv',
    ))

  def remoteAddressType(self) -> RemoteAddressType:
    """
    Calls Qt's 'RemoteAddressType QLowEnergyController::remoteAddressType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#remoteAddressType

    Returns
    -------

    RemoteAddressType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'RemoteAddressType(number)' gives.
    """
    #  RemoteAddressType QLowEnergyController::remoteAddressType() const
    return QLowEnergyController.RemoteAddressType(self.uglySide.call(
        'ritual_ZNK20QLowEnergyController17remoteAddressTypeEv',
    ))

  def services(self) -> QList[QBluetoothUuid]:
    """
    Calls Qt's 'QList<QBluetoothUuid> QLowEnergyController::services()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergycontroller.html#services

    Returns
    -------

    QList[QBluetoothUuid]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBluetoothUuid> QLowEnergyController::services() const
    address = self.uglySide.call(
        'ritual_ZNK20QLowEnergyController8servicesEv',
    )
    from . import QBluetoothUuid
    return QList[QBluetoothUuid]._cuteOwning(address)

  def error(self) -> Error:
    """
    Calls Qt's 'Error QLowEnergyController::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergycontroller.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QLowEnergyController::error() const
    return QLowEnergyController.Error(self.uglySide.call(
        'ritual_ZNK20QLowEnergyController5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QLowEnergyController::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLowEnergyController::errorString() const
    return self.uglySide.call(
        'ritual_ZNK20QLowEnergyController11errorStringEv',
    )

  def role(self) -> Role:
    """
    Calls Qt's 'Role QLowEnergyController::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergycontroller.html#role

    Returns
    -------

    Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Role(number)' gives.
    """
    #  Role QLowEnergyController::role() const
    return QLowEnergyController.Role(self.uglySide.call(
        'ritual_ZNK20QLowEnergyController4roleEv',
    ))

  def mtu(self) -> int:
    """
    Calls Qt's 'int QLowEnergyController::mtu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergycontroller.html#mtu
    """
    #  int QLowEnergyController::mtu() const
    return self.uglySide.call('ritual_ZNK20QLowEnergyController3mtuEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(RemoteAddressType)
  def setRemoteAddressType(self, type: RemoteAddressType) -> None:
    """
    Calls Qt's 'void
    QLowEnergyController::setRemoteAddressType(RemoteAddressType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#setRemoteAddressType

    Parameters
    ----------

    type : RemoteAddressType
      Passed on as its number.
    """
    #  void QLowEnergyController::setRemoteAddressType(RemoteAddressType
    #      type)
    self.uglySide.call(
        'ritual_ZN20QLowEnergyController20setRemoteAddressTypeENS_17RemoteA'
        'ddressTypeE',
        type.value,
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

  @overload(QBluetoothAddress)
  @overload(QBluetoothAddress, QObject)
  @overload(QBluetoothAddress, NoneType)
  def __init__(
      self,
      localDevice: QBluetoothAddress,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QLowEnergyController::QLowEnergyController(const QBluetoothAddress
    &localDevice, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#QLowEnergyController

    Parameters
    ----------

    localDevice : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLowEnergyController::QLowEnergyController(const QBluetoothAddress
    #      &localDevice, QObject *parent)
    self._noteCreation(QLowEnergyController, lambda: Rituals.call(
        'ritual_ZN20QLowEnergyControllerC1ERK17QBluetoothAddressP7QObject',
        self._valueOf(localDevice), self._addressOf(parent, 'QObject'),
    ))

  @overload(QBluetoothDeviceInfo, QBluetoothAddress)
  @overload(QBluetoothDeviceInfo, QBluetoothAddress, QObject)
  @overload(QBluetoothDeviceInfo, QBluetoothAddress, NoneType)
  def __init__(
      self,
      remoteDevice: QBluetoothDeviceInfo,
      localDevice: QBluetoothAddress,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QLowEnergyController::QLowEnergyController(const QBluetoothDeviceInfo
    &remoteDevice, const QBluetoothAddress &localDevice, QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#QLowEnergyController

    Parameters
    ----------

    remoteDevice : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.

    localDevice : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLowEnergyController::QLowEnergyController(const QBluetoothDeviceInfo
    #      &remoteDevice, const QBluetoothAddress &localDevice, QObject
    #      *parent)
    self._noteCreation(QLowEnergyController, lambda: Rituals.call(
        'ritual_ZN20QLowEnergyControllerC1ERK20QBluetoothDeviceInfoRK17QBlu'
        'etoothAddressP7QObject',
        self._valueOf(remoteDevice), self._valueOf(localDevice),
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

  def connectToDevice(self) -> None:
    """
    Calls Qt's 'void QLowEnergyController::connectToDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#connectToDevice
    """
    #  void QLowEnergyController::connectToDevice()
    self.uglySide.call('ritual_ZN20QLowEnergyController15connectToDeviceEv')

  def disconnectFromDevice(self) -> None:
    """
    Calls Qt's 'void QLowEnergyController::disconnectFromDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#disconnectFromDevice
    """
    #  void QLowEnergyController::disconnectFromDevice()
    self.uglySide.call(
        'ritual_ZN20QLowEnergyController20disconnectFromDeviceEv',
    )

  def discoverServices(self) -> None:
    """
    Calls Qt's 'void QLowEnergyController::discoverServices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#discoverServices
    """
    #  void QLowEnergyController::discoverServices()
    self.uglySide.call('ritual_ZN20QLowEnergyController16discoverServicesEv')

  @overload(QBluetoothUuid)
  @overload(QBluetoothUuid, QObject)
  @overload(QBluetoothUuid, NoneType)
  def createServiceObject(
      self,
      service: QBluetoothUuid,
      parent: Optional[QObject] = None,
  ) -> Optional[QLowEnergyService]:
    """
    Calls Qt's 'QLowEnergyService
    *QLowEnergyController::createServiceObject(const QBluetoothUuid &service,
    QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#createServiceObject

    Parameters
    ----------

    service : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QLowEnergyService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLowEnergyService *QLowEnergyController::createServiceObject(const
    #      QBluetoothUuid &service, QObject *parent)
    address = self.uglySide.call(
        'ritual_ZN20QLowEnergyController19createServiceObjectERK14QBluetoot'
        'hUuidP7QObject',
        self._valueOf(service), self._addressOf(parent, 'QObject'),
    )
    from . import QLowEnergyService
    return QLowEnergyService._cuteAt(address)

  @overload(QLowEnergyAdvertisingParameters, QLowEnergyAdvertisingData)
  @overload(
      QLowEnergyAdvertisingParameters, QLowEnergyAdvertisingData,
      QLowEnergyAdvertisingData,
  )
  def startAdvertising(
      self,
      parameters: QLowEnergyAdvertisingParameters,
      advertisingData: QLowEnergyAdvertisingData,
      scanResponseData: Optional[QLowEnergyAdvertisingData] = None,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyController::startAdvertising(const
    QLowEnergyAdvertisingParameters &parameters, const
    QLowEnergyAdvertisingData &advertisingData, const
    QLowEnergyAdvertisingData &scanResponseData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#startAdvertising

    Parameters
    ----------

    parameters : QLowEnergyAdvertisingParameters
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingParameters,
      which stays Python's own.

    advertisingData : QLowEnergyAdvertisingData
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingData, which
      stays Python's own.

    scanResponseData : Optional[QLowEnergyAdvertisingData]
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingData, which
      stays Python's own. May be left out, as in Qt: a new
      'QLowEnergyAdvertisingData()' is then passed on.
    """
    #  void QLowEnergyController::startAdvertising(const
    #      QLowEnergyAdvertisingParameters &parameters, const
    #      QLowEnergyAdvertisingData &advertisingData, const
    #      QLowEnergyAdvertisingData &scanResponseData)
    if scanResponseData is None:
      from . import QLowEnergyAdvertisingData
      scanResponseData = QLowEnergyAdvertisingData()
    self.uglySide.call(
        'ritual_ZN20QLowEnergyController16startAdvertisingERK31QLowEnergyAd'
        'vertisingParametersRK25QLowEnergyAdvertisingDataS5_',
        self._valueOf(parameters), self._valueOf(advertisingData),
        self._valueOf(scanResponseData),
    )

  def stopAdvertising(self) -> None:
    """
    Calls Qt's 'void QLowEnergyController::stopAdvertising()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#stopAdvertising
    """
    #  void QLowEnergyController::stopAdvertising()
    self.uglySide.call('ritual_ZN20QLowEnergyController15stopAdvertisingEv')

  @overload(QLowEnergyServiceData)
  @overload(QLowEnergyServiceData, QObject)
  @overload(QLowEnergyServiceData, NoneType)
  def addService(
      self,
      service: QLowEnergyServiceData,
      parent: Optional[QObject] = None,
  ) -> Optional[QLowEnergyService]:
    """
    Calls Qt's 'QLowEnergyService *QLowEnergyController::addService(const
    QLowEnergyServiceData &service, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#addService

    Parameters
    ----------

    service : QLowEnergyServiceData
      Passed on as a value: Qt reads the C++ QLowEnergyServiceData, which
      stays Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QLowEnergyService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLowEnergyService *QLowEnergyController::addService(const
    #      QLowEnergyServiceData &service, QObject *parent)
    address = self.uglySide.call(
        'ritual_ZN20QLowEnergyController10addServiceERK21QLowEnergyServiceD'
        'ataP7QObject',
        self._valueOf(service), self._addressOf(parent, 'QObject'),
    )
    from . import QLowEnergyService
    return QLowEnergyService._cuteAt(address)

  @overload(QLowEnergyConnectionParameters)
  def requestConnectionUpdate(
      self,
      parameters: QLowEnergyConnectionParameters,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyController::requestConnectionUpdate(const
    QLowEnergyConnectionParameters &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#requestConnectionUpdate

    Parameters
    ----------

    parameters : QLowEnergyConnectionParameters
      Passed on as a value: Qt reads the C++ QLowEnergyConnectionParameters,
      which stays Python's own.
    """
    #  void QLowEnergyController::requestConnectionUpdate(const
    #      QLowEnergyConnectionParameters &parameters)
    self.uglySide.call(
        'ritual_ZN20QLowEnergyController23requestConnectionUpdateERK30QLowE'
        'nergyConnectionParameters',
        self._valueOf(parameters),
    )

  def readRssi(self) -> None:
    """
    Calls Qt's 'void QLowEnergyController::readRssi()'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergycontroller.html#readRssi
    """
    #  void QLowEnergyController::readRssi()
    self.uglySide.call('ritual_ZN20QLowEnergyController8readRssiEv')

  def connected(self) -> None:
    """
    Calls Qt's 'void QLowEnergyController::connected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#connected
    """
    #  void QLowEnergyController::connected()
    self.uglySide.call('ritual_ZN20QLowEnergyController9connectedEv')

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QLowEnergyController::disconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#disconnected
    """
    #  void QLowEnergyController::disconnected()
    self.uglySide.call('ritual_ZN20QLowEnergyController12disconnectedEv')

  @overload(ControllerState)
  def stateChanged(self, state: ControllerState) -> None:
    """
    Calls Qt's 'void
    QLowEnergyController::stateChanged(QLowEnergyController::ControllerState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#stateChanged

    Parameters
    ----------

    state : ControllerState
      Passed on as its number.
    """
    #  void QLowEnergyController::stateChanged(QLowEnergyController::
    #      ControllerState state)
    self.uglySide.call(
        'ritual_ZN20QLowEnergyController12stateChangedENS_15ControllerState'
        'E',
        state.value,
    )

  @overload(Error)
  def errorOccurred(self, newError: Error) -> None:
    """
    Calls Qt's 'void
    QLowEnergyController::errorOccurred(QLowEnergyController::Error
    newError)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#errorOccurred

    Parameters
    ----------

    newError : Error
      Passed on as its number.
    """
    #  void QLowEnergyController::errorOccurred(QLowEnergyController::Error
    #      newError)
    self.uglySide.call(
        'ritual_ZN20QLowEnergyController13errorOccurredENS_5ErrorE',
        newError.value,
    )

  @overload(int)
  def mtuChanged(self, mtu: int) -> None:
    """
    Calls Qt's 'void QLowEnergyController::mtuChanged(int mtu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#mtuChanged

    Parameters
    ----------

    mtu : int
      Passed on as it is.
    """
    #  void QLowEnergyController::mtuChanged(int mtu)
    self.uglySide.call('ritual_ZN20QLowEnergyController10mtuChangedEi', mtu)

  @overload(int)
  def rssiRead(self, rssi: int) -> None:
    """
    Calls Qt's 'void QLowEnergyController::rssiRead(qint16 rssi)'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergycontroller.html#rssiRead

    Parameters
    ----------

    rssi : int
      Passed on as it is.
    """
    #  void QLowEnergyController::rssiRead(qint16 rssi)
    self.uglySide.call('ritual_ZN20QLowEnergyController8rssiReadEs', rssi)

  @overload(QBluetoothUuid)
  def serviceDiscovered(self, newService: QBluetoothUuid) -> None:
    """
    Calls Qt's 'void QLowEnergyController::serviceDiscovered(const
    QBluetoothUuid &newService)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#serviceDiscovered

    Parameters
    ----------

    newService : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.
    """
    #  void QLowEnergyController::serviceDiscovered(const QBluetoothUuid
    #      &newService)
    self.uglySide.call(
        'ritual_ZN20QLowEnergyController17serviceDiscoveredERK14QBluetoothU'
        'uid',
        self._valueOf(newService),
    )

  def discoveryFinished(self) -> None:
    """
    Calls Qt's 'void QLowEnergyController::discoveryFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#discoveryFinished
    """
    #  void QLowEnergyController::discoveryFinished()
    self.uglySide.call(
        'ritual_ZN20QLowEnergyController17discoveryFinishedEv',
    )

  @overload(QLowEnergyConnectionParameters)
  def connectionUpdated(
      self,
      parameters: QLowEnergyConnectionParameters,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyController::connectionUpdated(const
    QLowEnergyConnectionParameters &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycontroller.html#connectionUpdated

    Parameters
    ----------

    parameters : QLowEnergyConnectionParameters
      Passed on as a value: Qt reads the C++ QLowEnergyConnectionParameters,
      which stays Python's own.
    """
    #  void QLowEnergyController::connectionUpdated(const
    #      QLowEnergyConnectionParameters &parameters)
    self.uglySide.call(
        'ritual_ZN20QLowEnergyController17connectionUpdatedERK30QLowEnergyC'
        'onnectionParameters',
        self._valueOf(parameters),
    )

  def d_func(self) -> Optional[QLowEnergyControllerPrivate]:
    """
    Calls Qt's 'QLowEnergyControllerPrivate *QLowEnergyController::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergycontroller.html#d_func

    Returns
    -------

    Optional[QLowEnergyControllerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLowEnergyControllerPrivate *QLowEnergyController::d_func()
    address = self.uglySide.call('ritual_ZN20QLowEnergyController6d_funcEv')
    from . import QLowEnergyControllerPrivate
    return QLowEnergyControllerPrivate._cuteAt(address)
