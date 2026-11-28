"""
QBluetoothDeviceInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qbluetoothdeviceinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QBluetoothAddress, QBluetoothDeviceInfoPrivate
  from . import QBluetoothUuid
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothAddress = WAIT['QBluetoothAddress']
  QBluetoothUuid = WAIT['QBluetoothUuid']
  QByteArray = WAIT['QByteArray']


class QBluetoothDeviceInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBluetoothDeviceInfo: a plain Python object standing
  in front of one C++ QBluetoothDeviceInfo.

  C++ hands a QBluetoothDeviceInfo around as a copy, so every C++
  QBluetoothDeviceInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBluetoothDeviceInfo that has a ritual and that
  Python can call so far, 26 names in all: 'isValid', 'isCached',
  'setCached', '__eq__', '__ne__', 'address', 'name', 'setName',
  'serviceClasses', 'majorDeviceClass', 'minorDeviceClass', 'rssi',
  'setRssi', 'serviceUuids', 'setServiceUuids', 'manufacturerData',
  'setManufacturerData', 'serviceIds', 'serviceData', 'setServiceData',
  'setCoreConfigurations', 'coreConfigurations', 'setDeviceUuid',
  'deviceUuid', 'equals', 'd_func'. It can be made from Python, in 4 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBluetoothDeviceInfo::~QBluetoothDeviceInfo()': the destructor:
    Python removes its C++ QBluetoothDeviceInfo by it, and has no other use
    for it.
  - Qt's 'QBluetoothDeviceInfo &QBluetoothDeviceInfo::operator=(const
    QBluetoothDeviceInfo &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QList<quint16> QBluetoothDeviceInfo::manufacturerIds() const':
    gives a type Python has no way to take yet.
  - Qt's 'QMultiHash<quint16, QByteArray>
    QBluetoothDeviceInfo::manufacturerData() const': gives a type Python has
    no way to take yet.
  - Qt's 'QMultiHash<QBluetoothUuid, QByteArray>
    QBluetoothDeviceInfo::serviceData() const': gives a type Python has no
    way to take yet.
  - Qt's 'const QBluetoothDeviceInfoPrivate *QBluetoothDeviceInfo::d_func()
    const': takes in Python what 'QBluetoothDeviceInfoPrivate
    *QBluetoothDeviceInfo::d_func()' takes.

  What to expect
  --------------

  - The C++ QBluetoothDeviceInfo is created at the first use, not by
    'QBluetoothDeviceInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBluetoothDeviceInfo back gives a copy the ritual
    made for Python, in a new cute QBluetoothDeviceInfo.
  - Each name of Qt's QBluetoothDeviceInfo that has no cute function yet,
    'manufacturerIds', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QBluetoothDeviceInfo, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class CoreConfiguration(CuteFlags):
    """
    The flags enum 'QBluetoothDeviceInfo::CoreConfiguration' of Qt, with the
    4 names Qt gives in it. Qt names the type of its combinations
    'QBluetoothDeviceInfo::CoreConfigurations'.
    """

    UnknownCoreConfiguration = 0x0
    LowEnergyCoreConfiguration = 0x1
    BaseRateCoreConfiguration = 0x2
    BaseRateAndLowEnergyCoreConfiguration = 0x3

  CoreConfigurations = CoreConfiguration

  class Field(CuteFlags, scoped=True):
    """
    The flags enum 'QBluetoothDeviceInfo::Field' of Qt, with the 5 names Qt
    gives in it. Qt names the type of its combinations
    'QBluetoothDeviceInfo::Fields'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    NULL = 0x0
    RSSI = 0x1
    ManufacturerData = 0x2
    ServiceData = 0x4
    All = 0x7fff

  Fields = Field

  class MajorDeviceClass(CuteNum):
    """
    The enum 'QBluetoothDeviceInfo::MajorDeviceClass' of Qt, with the 11
    names Qt gives in it.
    """

    MiscellaneousDevice = Kee[int](0)
    ComputerDevice = Kee[int](1)
    PhoneDevice = Kee[int](2)
    NetworkDevice = Kee[int](3)
    AudioVideoDevice = Kee[int](4)
    PeripheralDevice = Kee[int](5)
    ImagingDevice = Kee[int](6)
    WearableDevice = Kee[int](7)
    ToyDevice = Kee[int](8)
    HealthDevice = Kee[int](9)
    UncategorizedDevice = Kee[int](31)

  class MinorAudioVideoClass(CuteNum):
    """
    The enum 'QBluetoothDeviceInfo::MinorAudioVideoClass' of Qt, with the 17
    names Qt gives in it.
    """

    UncategorizedAudioVideoDevice = Kee[int](0)
    WearableHeadsetDevice = Kee[int](1)
    HandsFreeDevice = Kee[int](2)
    Microphone = Kee[int](4)
    Loudspeaker = Kee[int](5)
    Headphones = Kee[int](6)
    PortableAudioDevice = Kee[int](7)
    CarAudio = Kee[int](8)
    SetTopBox = Kee[int](9)
    HiFiAudioDevice = Kee[int](10)
    Vcr = Kee[int](11)
    VideoCamera = Kee[int](12)
    Camcorder = Kee[int](13)
    VideoMonitor = Kee[int](14)
    VideoDisplayAndLoudspeaker = Kee[int](15)
    VideoConferencing = Kee[int](16)
    GamingDevice = Kee[int](18)

  class MinorComputerClass(CuteNum):
    """
    The enum 'QBluetoothDeviceInfo::MinorComputerClass' of Qt, with the 7
    names Qt gives in it.
    """

    UncategorizedComputer = Kee[int](0)
    DesktopComputer = Kee[int](1)
    ServerComputer = Kee[int](2)
    LaptopComputer = Kee[int](3)
    HandheldClamShellComputer = Kee[int](4)
    HandheldComputer = Kee[int](5)
    WearableComputer = Kee[int](6)

  class MinorHealthClass(CuteNum):
    """
    The enum 'QBluetoothDeviceInfo::MinorHealthClass' of Qt, with the 8 names
    Qt gives in it.
    """

    UncategorizedHealthDevice = Kee[int](0)
    HealthBloodPressureMonitor = Kee[int](1)
    HealthThermometer = Kee[int](2)
    HealthWeightScale = Kee[int](3)
    HealthGlucoseMeter = Kee[int](4)
    HealthPulseOximeter = Kee[int](5)
    HealthDataDisplay = Kee[int](7)
    HealthStepCounter = Kee[int](8)

  class MinorImagingClass(CuteNum):
    """
    The enum 'QBluetoothDeviceInfo::MinorImagingClass' of Qt, with the 5
    names Qt gives in it.
    """

    UncategorizedImagingDevice = Kee[int](0)
    ImageDisplay = Kee[int](4)
    ImageCamera = Kee[int](8)
    ImageScanner = Kee[int](16)
    ImagePrinter = Kee[int](32)

  class MinorMiscellaneousClass(CuteNum):
    """
    The enum 'QBluetoothDeviceInfo::MinorMiscellaneousClass' of Qt, with the
    1 names Qt gives in it.
    """

    UncategorizedMiscellaneous = Kee[int](0)

  class MinorNetworkClass(CuteNum):
    """
    The enum 'QBluetoothDeviceInfo::MinorNetworkClass' of Qt, with the 8
    names Qt gives in it.
    """

    NetworkFullService = Kee[int](0)
    NetworkLoadFactorOne = Kee[int](8)
    NetworkLoadFactorTwo = Kee[int](16)
    NetworkLoadFactorThree = Kee[int](24)
    NetworkLoadFactorFour = Kee[int](32)
    NetworkLoadFactorFive = Kee[int](40)
    NetworkLoadFactorSix = Kee[int](48)
    NetworkNoService = Kee[int](56)

  class MinorPeripheralClass(CuteNum):
    """
    The enum 'QBluetoothDeviceInfo::MinorPeripheralClass' of Qt, with the 10
    names Qt gives in it.
    """

    UncategorizedPeripheral = Kee[int](0)
    KeyboardPeripheral = Kee[int](16)
    PointingDevicePeripheral = Kee[int](32)
    KeyboardWithPointingDevicePeripheral = Kee[int](48)
    JoystickPeripheral = Kee[int](1)
    GamepadPeripheral = Kee[int](2)
    RemoteControlPeripheral = Kee[int](3)
    SensingDevicePeripheral = Kee[int](4)
    DigitizerTabletPeripheral = Kee[int](5)
    CardReaderPeripheral = Kee[int](6)

  class MinorPhoneClass(CuteNum):
    """
    The enum 'QBluetoothDeviceInfo::MinorPhoneClass' of Qt, with the 6 names
    Qt gives in it.
    """

    UncategorizedPhone = Kee[int](0)
    CellularPhone = Kee[int](1)
    CordlessPhone = Kee[int](2)
    SmartPhone = Kee[int](3)
    WiredModemOrVoiceGatewayPhone = Kee[int](4)
    CommonIsdnAccessPhone = Kee[int](5)

  class MinorToyClass(CuteNum):
    """
    The enum 'QBluetoothDeviceInfo::MinorToyClass' of Qt, with the 6 names Qt
    gives in it.
    """

    UncategorizedToy = Kee[int](0)
    ToyRobot = Kee[int](1)
    ToyVehicle = Kee[int](2)
    ToyDoll = Kee[int](3)
    ToyController = Kee[int](4)
    ToyGame = Kee[int](5)

  class MinorWearableClass(CuteNum):
    """
    The enum 'QBluetoothDeviceInfo::MinorWearableClass' of Qt, with the 6
    names Qt gives in it.
    """

    UncategorizedWearableDevice = Kee[int](0)
    WearableWristWatch = Kee[int](1)
    WearablePager = Kee[int](2)
    WearableJacket = Kee[int](3)
    WearableHelmet = Kee[int](4)
    WearableGlasses = Kee[int](5)

  class ServiceClass(CuteFlags):
    """
    The flags enum 'QBluetoothDeviceInfo::ServiceClass' of Qt, with the 10
    names Qt gives in it. Qt names the type of its combinations
    'QBluetoothDeviceInfo::ServiceClasses'.
    """

    NoService = 0x0
    PositioningService = 0x1
    NetworkingService = 0x2
    RenderingService = 0x4
    CapturingService = 0x8
    ObjectTransferService = 0x10
    AudioService = 0x20
    TelephonyService = 0x40
    InformationService = 0x80
    AllServices = 0x7ff

  ServiceClasses = ServiceClass

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(a: QBluetoothDeviceInfo, b: QBluetoothDeviceInfo) -> bool:
    """
    Calls Qt's 'bool QBluetoothDeviceInfo::equals(const QBluetoothDeviceInfo
    &a, const QBluetoothDeviceInfo &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#equals

    Parameters
    ----------

    a : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.

    b : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.
    """
    #  bool QBluetoothDeviceInfo::equals(const QBluetoothDeviceInfo &a, const
    #      QBluetoothDeviceInfo &b)
    return Rituals.call(
        'ritual_ZN20QBluetoothDeviceInfo6equalsERKS_S1_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothDeviceInfo'

  #  Qt's '~QBluetoothDeviceInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QBluetoothDeviceInfo behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QBluetoothDeviceInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothDeviceInfo::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#isValid
    """
    #  bool QBluetoothDeviceInfo::isValid() const
    return self.uglySide.call('ritual_ZNK20QBluetoothDeviceInfo7isValidEv')

  def isCached(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothDeviceInfo::isCached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#isCached
    """
    #  bool QBluetoothDeviceInfo::isCached() const
    return self.uglySide.call('ritual_ZNK20QBluetoothDeviceInfo8isCachedEv')

  def address(self) -> QBluetoothAddress:
    """
    Calls Qt's 'QBluetoothAddress QBluetoothDeviceInfo::address() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#address

    Returns
    -------

    QBluetoothAddress
      A new cute QBluetoothAddress around the copy Qt gave back. Python owns
      it.
    """
    #  QBluetoothAddress QBluetoothDeviceInfo::address() const
    address = self.uglySide.call(
        'ritual_ZNK20QBluetoothDeviceInfo7addressEv',
    )
    from . import QBluetoothAddress
    return QBluetoothAddress._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QBluetoothDeviceInfo::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothDeviceInfo::name() const
    return self.uglySide.call('ritual_ZNK20QBluetoothDeviceInfo4nameEv')

  def serviceClasses(self) -> ServiceClasses:
    """
    Calls Qt's 'ServiceClasses QBluetoothDeviceInfo::serviceClasses() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#serviceClasses

    Returns
    -------

    ServiceClasses
      The value standing for the combination Qt gave back.
    """
    #  ServiceClasses QBluetoothDeviceInfo::serviceClasses() const
    return QBluetoothDeviceInfo.ServiceClasses(self.uglySide.call(
        'ritual_ZNK20QBluetoothDeviceInfo14serviceClassesEv',
    ))

  def majorDeviceClass(self) -> MajorDeviceClass:
    """
    Calls Qt's 'MajorDeviceClass QBluetoothDeviceInfo::majorDeviceClass()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#majorDeviceClass

    Returns
    -------

    MajorDeviceClass
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MajorDeviceClass(number)'
      gives.
    """
    #  MajorDeviceClass QBluetoothDeviceInfo::majorDeviceClass() const
    return QBluetoothDeviceInfo.MajorDeviceClass(self.uglySide.call(
        'ritual_ZNK20QBluetoothDeviceInfo16majorDeviceClassEv',
    ))

  def minorDeviceClass(self) -> int:
    """
    Calls Qt's 'quint8 QBluetoothDeviceInfo::minorDeviceClass() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#minorDeviceClass
    """
    #  quint8 QBluetoothDeviceInfo::minorDeviceClass() const
    return self.uglySide.call(
        'ritual_ZNK20QBluetoothDeviceInfo16minorDeviceClassEv',
    )

  def rssi(self) -> int:
    """
    Calls Qt's 'qint16 QBluetoothDeviceInfo::rssi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#rssi
    """
    #  qint16 QBluetoothDeviceInfo::rssi() const
    return self.uglySide.call('ritual_ZNK20QBluetoothDeviceInfo4rssiEv')

  def serviceUuids(self) -> QList[QBluetoothUuid]:
    """
    Calls Qt's 'QList<QBluetoothUuid> QBluetoothDeviceInfo::serviceUuids()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#serviceUuids

    Returns
    -------

    QList[QBluetoothUuid]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBluetoothUuid> QBluetoothDeviceInfo::serviceUuids() const
    address = self.uglySide.call(
        'ritual_ZNK20QBluetoothDeviceInfo12serviceUuidsEv',
    )
    from . import QBluetoothUuid
    return QList[QBluetoothUuid]._cuteOwning(address)

  @overload(int)
  def manufacturerData(self, manufacturerId: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QBluetoothDeviceInfo::manufacturerData(quint16
    manufacturerId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#manufacturerData

    Parameters
    ----------

    manufacturerId : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QBluetoothDeviceInfo::manufacturerData(quint16
    #      manufacturerId) const
    address = self.uglySide.call(
        'ritual_ZNK20QBluetoothDeviceInfo16manufacturerDataEt',
        manufacturerId,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def serviceIds(self) -> QList[QBluetoothUuid]:
    """
    Calls Qt's 'QList<QBluetoothUuid> QBluetoothDeviceInfo::serviceIds()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#serviceIds

    Returns
    -------

    QList[QBluetoothUuid]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBluetoothUuid> QBluetoothDeviceInfo::serviceIds() const
    address = self.uglySide.call(
        'ritual_ZNK20QBluetoothDeviceInfo10serviceIdsEv',
    )
    from . import QBluetoothUuid
    return QList[QBluetoothUuid]._cuteOwning(address)

  @overload(QBluetoothUuid)
  def serviceData(self, serviceId: QBluetoothUuid) -> QByteArray:
    """
    Calls Qt's 'QByteArray QBluetoothDeviceInfo::serviceData(const
    QBluetoothUuid &serviceId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#serviceData

    Parameters
    ----------

    serviceId : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QBluetoothDeviceInfo::serviceData(const QBluetoothUuid
    #      &serviceId) const
    address = self.uglySide.call(
        'ritual_ZNK20QBluetoothDeviceInfo11serviceDataERK14QBluetoothUuid',
        self._valueOf(serviceId),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def coreConfigurations(self) -> CoreConfigurations:
    """
    Calls Qt's 'QBluetoothDeviceInfo::CoreConfigurations
    QBluetoothDeviceInfo::coreConfigurations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#coreConfigurations

    Returns
    -------

    CoreConfigurations
      The value standing for the combination Qt gave back.
    """
    #  QBluetoothDeviceInfo::CoreConfigurations
    #      QBluetoothDeviceInfo::coreConfigurations() const
    return QBluetoothDeviceInfo.CoreConfigurations(self.uglySide.call(
        'ritual_ZNK20QBluetoothDeviceInfo18coreConfigurationsEv',
    ))

  def deviceUuid(self) -> QBluetoothUuid:
    """
    Calls Qt's 'QBluetoothUuid QBluetoothDeviceInfo::deviceUuid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#deviceUuid

    Returns
    -------

    QBluetoothUuid
      A new cute QBluetoothUuid around the copy Qt gave back. Python owns it.
    """
    #  QBluetoothUuid QBluetoothDeviceInfo::deviceUuid() const
    address = self.uglySide.call(
        'ritual_ZNK20QBluetoothDeviceInfo10deviceUuidEv',
    )
    from . import QBluetoothUuid
    return QBluetoothUuid._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setCached(self, cached: bool) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceInfo::setCached(bool cached)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#setCached

    Parameters
    ----------

    cached : bool
      Passed on as it is.
    """
    #  void QBluetoothDeviceInfo::setCached(bool cached)
    self.uglySide.call('ritual_ZN20QBluetoothDeviceInfo9setCachedEb', cached)

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceInfo::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBluetoothDeviceInfo::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN20QBluetoothDeviceInfo7setNameERK7QString', name,
    )

  @overload(int)
  def setRssi(self, signal: int) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceInfo::setRssi(qint16 signal)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#setRssi

    Parameters
    ----------

    signal : int
      Passed on as it is.
    """
    #  void QBluetoothDeviceInfo::setRssi(qint16 signal)
    self.uglySide.call('ritual_ZN20QBluetoothDeviceInfo7setRssiEs', signal)

  @overload(QList[QBluetoothUuid])
  def setServiceUuids(self, uuids: QList[QBluetoothUuid]) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceInfo::setServiceUuids(const
    QList<QBluetoothUuid> &uuids)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#setServiceUuids

    Parameters
    ----------

    uuids : QList[QBluetoothUuid]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBluetoothDeviceInfo::setServiceUuids(const QList<QBluetoothUuid>
    #      &uuids)
    self.uglySide.call(
        'ritual_ZN20QBluetoothDeviceInfo15setServiceUuidsERK5QListI14QBluet'
        'oothUuidE',
        self._valueOf(uuids),
    )

  @overload(int, QByteArray)
  def setManufacturerData(
      self,
      manufacturerId: int,
      data: QByteArray,
  ) -> bool:
    """
    Calls Qt's 'bool QBluetoothDeviceInfo::setManufacturerData(quint16
    manufacturerId, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#setManufacturerData

    Parameters
    ----------

    manufacturerId : int
      Passed on as it is.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QBluetoothDeviceInfo::setManufacturerData(quint16 manufacturerId,
    #      const QByteArray &data)
    return self.uglySide.call(
        'ritual_ZN20QBluetoothDeviceInfo19setManufacturerDataEtRK10QByteArr'
        'ay',
        manufacturerId, self._valueOf(data),
    )

  @overload(QBluetoothUuid, QByteArray)
  def setServiceData(
      self,
      serviceId: QBluetoothUuid,
      data: QByteArray,
  ) -> bool:
    """
    Calls Qt's 'bool QBluetoothDeviceInfo::setServiceData(const
    QBluetoothUuid &serviceId, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#setServiceData

    Parameters
    ----------

    serviceId : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QBluetoothDeviceInfo::setServiceData(const QBluetoothUuid
    #      &serviceId, const QByteArray &data)
    return self.uglySide.call(
        'ritual_ZN20QBluetoothDeviceInfo14setServiceDataERK14QBluetoothUuid'
        'RK10QByteArray',
        self._valueOf(serviceId), self._valueOf(data),
    )

  @overload(CoreConfigurations)
  def setCoreConfigurations(self, coreConfigs: CoreConfigurations) -> None:
    """
    Calls Qt's 'void
    QBluetoothDeviceInfo::setCoreConfigurations(QBluetoothDeviceInfo::
    CoreConfigurations coreConfigs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#setCoreConfigurations

    Parameters
    ----------

    coreConfigs : CoreConfigurations
      Passed on as its number.
    """
    #  void QBluetoothDeviceInfo::setCoreConfigurations(
    #      QBluetoothDeviceInfo::CoreConfigurations coreConfigs)
    self.uglySide.call(
        'ritual_ZN20QBluetoothDeviceInfo21setCoreConfigurationsE6QFlagsINS_'
        '17CoreConfigurationEE',
        coreConfigs.value,
    )

  @overload(QBluetoothUuid)
  def setDeviceUuid(self, uuid: QBluetoothUuid) -> None:
    """
    Calls Qt's 'void QBluetoothDeviceInfo::setDeviceUuid(const QBluetoothUuid
    &uuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#setDeviceUuid

    Parameters
    ----------

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.
    """
    #  void QBluetoothDeviceInfo::setDeviceUuid(const QBluetoothUuid &uuid)
    self.uglySide.call(
        'ritual_ZN20QBluetoothDeviceInfo13setDeviceUuidERK14QBluetoothUuid',
        self._valueOf(uuid),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QBluetoothDeviceInfo) -> bool:
    """
    Calls Qt's 'bool operator==(const QBluetoothDeviceInfo &a, const
    QBluetoothDeviceInfo &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#operator==

    Parameters
    ----------

    b : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.
    """
    #  bool operator==(const QBluetoothDeviceInfo &a, const
    #      QBluetoothDeviceInfo &b)
    return Rituals.call(
        'ritual_ZeqRK20QBluetoothDeviceInfoS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, b: QBluetoothDeviceInfo) -> bool:
    """
    Calls Qt's 'bool operator!=(const QBluetoothDeviceInfo &a, const
    QBluetoothDeviceInfo &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#operator!=

    Parameters
    ----------

    b : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.
    """
    #  bool operator!=(const QBluetoothDeviceInfo &a, const
    #      QBluetoothDeviceInfo &b)
    return Rituals.call(
        'ritual_ZneRK20QBluetoothDeviceInfoS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    'QBluetoothDeviceInfo::QBluetoothDeviceInfo()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#QBluetoothDeviceInfo
    """
    #  QBluetoothDeviceInfo::QBluetoothDeviceInfo()
    self._noteCreation(QBluetoothDeviceInfo, lambda: Rituals.call(
        'ritual_ZN20QBluetoothDeviceInfoC1Ev',
    ))

  @overload(QBluetoothAddress, str, int)
  def __init__(
      self,
      address: QBluetoothAddress,
      name: str,
      classOfDevice: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothDeviceInfo::QBluetoothDeviceInfo(const QBluetoothAddress
    &address, const QString &name, quint32 classOfDevice)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#QBluetoothDeviceInfo

    Parameters
    ----------

    address : QBluetoothAddress
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call.

    classOfDevice : int
      Passed on as it is.
    """
    #  QBluetoothDeviceInfo::QBluetoothDeviceInfo(const QBluetoothAddress
    #      &address, const QString &name, quint32 classOfDevice)
    self._noteCreation(QBluetoothDeviceInfo, lambda: Rituals.call(
        'ritual_ZN20QBluetoothDeviceInfoC1ERK17QBluetoothAddressRK7QStringj',
        self._valueOf(address), name, classOfDevice,
    ))

  @overload(QBluetoothUuid, str, int)
  def __init__(
      self,
      uuid: QBluetoothUuid,
      name: str,
      classOfDevice: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothDeviceInfo::QBluetoothDeviceInfo(const QBluetoothUuid &uuid,
    const QString &name, quint32 classOfDevice)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#QBluetoothDeviceInfo

    Parameters
    ----------

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call.

    classOfDevice : int
      Passed on as it is.
    """
    #  QBluetoothDeviceInfo::QBluetoothDeviceInfo(const QBluetoothUuid &uuid,
    #      const QString &name, quint32 classOfDevice)
    self._noteCreation(QBluetoothDeviceInfo, lambda: Rituals.call(
        'ritual_ZN20QBluetoothDeviceInfoC1ERK14QBluetoothUuidRK7QStringj',
        self._valueOf(uuid), name, classOfDevice,
    ))

  @overload(THIS)
  def __init__(self, other: QBluetoothDeviceInfo) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothDeviceInfo::QBluetoothDeviceInfo(const QBluetoothDeviceInfo
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#QBluetoothDeviceInfo

    Parameters
    ----------

    other : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.
    """
    #  QBluetoothDeviceInfo::QBluetoothDeviceInfo(const QBluetoothDeviceInfo
    #      &other)
    self._noteCreation(QBluetoothDeviceInfo, lambda: Rituals.call(
        'ritual_ZN20QBluetoothDeviceInfoC1ERKS_', self._valueOf(other),
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

  def d_func(self) -> Optional[QBluetoothDeviceInfoPrivate]:
    """
    Calls Qt's 'QBluetoothDeviceInfoPrivate *QBluetoothDeviceInfo::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothdeviceinfo.html#d_func

    Returns
    -------

    Optional[QBluetoothDeviceInfoPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBluetoothDeviceInfoPrivate *QBluetoothDeviceInfo::d_func()
    address = self.uglySide.call('ritual_ZN20QBluetoothDeviceInfo6d_funcEv')
    from . import QBluetoothDeviceInfoPrivate
    return QBluetoothDeviceInfoPrivate._cuteAt(address)

  @staticmethod
  def manufacturerIds(*__, **_) -> Never:
    """
    Qt's 'QList<quint16> QBluetoothDeviceInfo::manufacturerIds() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QBluetoothDeviceInfo.manufacturerIds' has no cute function yet. "
        "Qt's 'QList<quint16> QBluetoothDeviceInfo::manufacturerIds() "
        "const': gives a type Python has no way to take yet.")


#  Qt's 'QList<QBluetoothDeviceInfo>': the list of QBluetoothDeviceInfo,
#  which 'QList[QBluetoothDeviceInfo]' gives. It is made here, so that there
#  is one as soon as there can be a QBluetoothDeviceInfo.
QList.createKind(
    QBluetoothDeviceInfo, 'value',
    make='ritual_list_make_QBluetoothDeviceInfo',
    add='ritual_list_add_QBluetoothDeviceInfo',
    size='ritual_list_size_QBluetoothDeviceInfo',
    at='ritual_list_at_QBluetoothDeviceInfo',
    drop='ritual_list_drop_QBluetoothDeviceInfo',
)
