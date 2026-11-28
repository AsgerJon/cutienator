"""
QBluetoothUuid binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qbluetoothuuid.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QSysInfo, QUuid

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug
  from . import quint128
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QBluetoothUuid(QUuid):
  """
  The cute side of Qt's QBluetoothUuid: a plain Python object standing in
  front of one C++ QBluetoothUuid.

  It is built on the cute 'QUuid', as Qt's QBluetoothUuid is built on Qt's
  QUuid, and has everything that class has.

  C++ hands a QBluetoothUuid around as a copy, so every C++ QBluetoothUuid
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBluetoothUuid that has a ritual and that Python can
  call so far, 9 names in all: '__eq__', '__ne__', '__rlshift__',
  'minimumSize', 'toUInt128', 'serviceClassToString', 'protocolToString',
  'characteristicToString', 'descriptorToString'. It can be made from Python,
  in 8 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBluetoothUuid::QBluetoothUuid(quint32 uuid)': takes in Python what
    'QBluetoothUuid::QBluetoothUuid(quint16 uuid)' takes.
  - Qt's 'QBluetoothUuid::~QBluetoothUuid()': the destructor: Python removes
    its C++ QBluetoothUuid by it, and has no other use for it.
  - Qt's 'QBluetoothUuid &QBluetoothUuid::operator=(const QBluetoothUuid
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'quint16 QBluetoothUuid::toUInt16(bool *ok) const': takes a number
    to change where it is.
  - Qt's 'quint32 QBluetoothUuid::toUInt32(bool *ok) const': takes a number
    to change where it is.

  What has no ritual
  ------------------

  1 of the 23 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QBluetoothUuid is created at the first use, not by
    'QBluetoothUuid(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBluetoothUuid back gives a copy the ritual made for
    Python, in a new cute QBluetoothUuid.
  - Each name of Qt's QBluetoothUuid that has no cute function yet,
    'toUInt16', 'toUInt32', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QBluetoothUuid, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CharacteristicType(CuteNum, scoped=True):
    """
    The enum 'QBluetoothUuid::CharacteristicType' of Qt, with the 137 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    DeviceName = Kee[int](10752)
    Appearance = Kee[int](10753)
    PeripheralPrivacyFlag = Kee[int](10754)
    ReconnectionAddress = Kee[int](10755)
    PeripheralPreferredConnectionParameters = Kee[int](10756)
    ServiceChanged = Kee[int](10757)
    AlertLevel = Kee[int](10758)
    TxPowerLevel = Kee[int](10759)
    DateTime = Kee[int](10760)
    DayOfWeek = Kee[int](10761)
    DayDateTime = Kee[int](10762)
    ExactTime256 = Kee[int](10764)
    DSTOffset = Kee[int](10765)
    TimeZone = Kee[int](10766)
    LocalTimeInformation = Kee[int](10767)
    TimeWithDST = Kee[int](10769)
    TimeAccuracy = Kee[int](10770)
    TimeSource = Kee[int](10771)
    ReferenceTimeInformation = Kee[int](10772)
    TimeUpdateControlPoint = Kee[int](10774)
    TimeUpdateState = Kee[int](10775)
    GlucoseMeasurement = Kee[int](10776)
    BatteryLevel = Kee[int](10777)
    TemperatureMeasurement = Kee[int](10780)
    TemperatureType = Kee[int](10781)
    IntermediateTemperature = Kee[int](10782)
    MeasurementInterval = Kee[int](10785)
    BootKeyboardInputReport = Kee[int](10786)
    SystemID = Kee[int](10787)
    ModelNumberString = Kee[int](10788)
    SerialNumberString = Kee[int](10789)
    FirmwareRevisionString = Kee[int](10790)
    HardwareRevisionString = Kee[int](10791)
    SoftwareRevisionString = Kee[int](10792)
    ManufacturerNameString = Kee[int](10793)
    IEEE1107320601RegulatoryCertificationDataList = Kee[int](10794)
    CurrentTime = Kee[int](10795)
    MagneticDeclination = Kee[int](10796)
    ScanRefresh = Kee[int](10801)
    BootKeyboardOutputReport = Kee[int](10802)
    BootMouseInputReport = Kee[int](10803)
    GlucoseMeasurementContext = Kee[int](10804)
    BloodPressureMeasurement = Kee[int](10805)
    IntermediateCuffPressure = Kee[int](10806)
    HeartRateMeasurement = Kee[int](10807)
    BodySensorLocation = Kee[int](10808)
    HeartRateControlPoint = Kee[int](10809)
    AlertStatus = Kee[int](10815)
    RingerControlPoint = Kee[int](10816)
    RingerSetting = Kee[int](10817)
    AlertCategoryIDBitMask = Kee[int](10818)
    AlertCategoryID = Kee[int](10819)
    AlertNotificationControlPoint = Kee[int](10820)
    UnreadAlertStatus = Kee[int](10821)
    NewAlert = Kee[int](10822)
    SupportedNewAlertCategory = Kee[int](10823)
    SupportedUnreadAlertCategory = Kee[int](10824)
    BloodPressureFeature = Kee[int](10825)
    HIDInformation = Kee[int](10826)
    ReportMap = Kee[int](10827)
    HIDControlPoint = Kee[int](10828)
    Report = Kee[int](10829)
    ProtocolMode = Kee[int](10830)
    ScanIntervalWindow = Kee[int](10831)
    PnPID = Kee[int](10832)
    GlucoseFeature = Kee[int](10833)
    RecordAccessControlPoint = Kee[int](10834)
    RSCMeasurement = Kee[int](10835)
    RSCFeature = Kee[int](10836)
    SCControlPoint = Kee[int](10837)
    CSCMeasurement = Kee[int](10843)
    CSCFeature = Kee[int](10844)
    SensorLocation = Kee[int](10845)
    CyclingPowerMeasurement = Kee[int](10851)
    CyclingPowerVector = Kee[int](10852)
    CyclingPowerFeature = Kee[int](10853)
    CyclingPowerControlPoint = Kee[int](10854)
    LocationAndSpeed = Kee[int](10855)
    Navigation = Kee[int](10856)
    PositionQuality = Kee[int](10857)
    LNFeature = Kee[int](10858)
    LNControlPoint = Kee[int](10859)
    Elevation = Kee[int](10860)
    Pressure = Kee[int](10861)
    Temperature = Kee[int](10862)
    Humidity = Kee[int](10863)
    TrueWindSpeed = Kee[int](10864)
    TrueWindDirection = Kee[int](10865)
    ApparentWindSpeed = Kee[int](10866)
    ApparentWindDirection = Kee[int](10867)
    GustFactor = Kee[int](10868)
    PollenConcentration = Kee[int](10869)
    UVIndex = Kee[int](10870)
    Irradiance = Kee[int](10871)
    Rainfall = Kee[int](10872)
    WindChill = Kee[int](10873)
    HeatIndex = Kee[int](10874)
    DewPoint = Kee[int](10875)
    DescriptorValueChanged = Kee[int](10877)
    AerobicHeartRateLowerLimit = Kee[int](10878)
    AerobicThreshold = Kee[int](10879)
    Age = Kee[int](10880)
    AnaerobicHeartRateLowerLimit = Kee[int](10881)
    AnaerobicHeartRateUpperLimit = Kee[int](10882)
    AnaerobicThreshold = Kee[int](10883)
    AerobicHeartRateUpperLimit = Kee[int](10884)
    DateOfBirth = Kee[int](10885)
    DateOfThresholdAssessment = Kee[int](10886)
    EmailAddress = Kee[int](10887)
    FatBurnHeartRateLowerLimit = Kee[int](10888)
    FatBurnHeartRateUpperLimit = Kee[int](10889)
    FirstName = Kee[int](10890)
    FiveZoneHeartRateLimits = Kee[int](10891)
    Gender = Kee[int](10892)
    HeartRateMax = Kee[int](10893)
    Height = Kee[int](10894)
    HipCircumference = Kee[int](10895)
    LastName = Kee[int](10896)
    MaximumRecommendedHeartRate = Kee[int](10897)
    RestingHeartRate = Kee[int](10898)
    SportTypeForAerobicAnaerobicThresholds = Kee[int](10899)
    ThreeZoneHeartRateLimits = Kee[int](10900)
    TwoZoneHeartRateLimits = Kee[int](10901)
    VO2Max = Kee[int](10902)
    WaistCircumference = Kee[int](10903)
    Weight = Kee[int](10904)
    DatabaseChangeIncrement = Kee[int](10905)
    UserIndex = Kee[int](10906)
    BodyCompositionFeature = Kee[int](10907)
    BodyCompositionMeasurement = Kee[int](10908)
    WeightMeasurement = Kee[int](10909)
    WeightScaleFeature = Kee[int](10910)
    UserControlPoint = Kee[int](10911)
    MagneticFluxDensity2D = Kee[int](10912)
    MagneticFluxDensity3D = Kee[int](10913)
    Language = Kee[int](10914)
    BarometricPressureTrend = Kee[int](10915)

  class DescriptorType(CuteNum, scoped=True):
    """
    The enum 'QBluetoothUuid::DescriptorType' of Qt, with the 13 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    UnknownDescriptorType = Kee[int](0)
    CharacteristicExtendedProperties = Kee[int](10496)
    CharacteristicUserDescription = Kee[int](10497)
    ClientCharacteristicConfiguration = Kee[int](10498)
    ServerCharacteristicConfiguration = Kee[int](10499)
    CharacteristicPresentationFormat = Kee[int](10500)
    CharacteristicAggregateFormat = Kee[int](10501)
    ValidRange = Kee[int](10502)
    ExternalReportReference = Kee[int](10503)
    ReportReference = Kee[int](10504)
    EnvironmentalSensingConfiguration = Kee[int](10507)
    EnvironmentalSensingMeasurement = Kee[int](10508)
    EnvironmentalSensingTriggerSetting = Kee[int](10509)

  class ProtocolUuid(CuteNum, scoped=True):
    """
    The enum 'QBluetoothUuid::ProtocolUuid' of Qt, with the 25 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Sdp = Kee[int](1)
    Udp = Kee[int](2)
    Rfcomm = Kee[int](3)
    Tcp = Kee[int](4)
    TcsBin = Kee[int](5)
    TcsAt = Kee[int](6)
    Att = Kee[int](7)
    Obex = Kee[int](8)
    Ip = Kee[int](9)
    Ftp = Kee[int](10)
    Http = Kee[int](12)
    Wsp = Kee[int](14)
    Bnep = Kee[int](15)
    Upnp = Kee[int](16)
    Hidp = Kee[int](17)
    HardcopyControlChannel = Kee[int](18)
    HardcopyDataChannel = Kee[int](20)
    HardcopyNotification = Kee[int](22)
    Avctp = Kee[int](23)
    Avdtp = Kee[int](25)
    Cmtp = Kee[int](27)
    UdiCPlain = Kee[int](29)
    McapControlChannel = Kee[int](30)
    McapDataChannel = Kee[int](31)
    L2cap = Kee[int](256)

  class ServiceClassUuid(CuteNum, scoped=True):
    """
    The enum 'QBluetoothUuid::ServiceClassUuid' of Qt, with the 91 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    ServiceDiscoveryServer = Kee[int](4096)
    BrowseGroupDescriptor = Kee[int](4097)
    PublicBrowseGroup = Kee[int](4098)
    SerialPort = Kee[int](4353)
    LANAccessUsingPPP = Kee[int](4354)
    DialupNetworking = Kee[int](4355)
    IrMCSync = Kee[int](4356)
    ObexObjectPush = Kee[int](4357)
    OBEXFileTransfer = Kee[int](4358)
    IrMCSyncCommand = Kee[int](4359)
    Headset = Kee[int](4360)
    AudioSource = Kee[int](4362)
    AudioSink = Kee[int](4363)
    AV_RemoteControlTarget = Kee[int](4364)
    AdvancedAudioDistribution = Kee[int](4365)
    AV_RemoteControl = Kee[int](4366)
    AV_RemoteControlController = Kee[int](4367)
    HeadsetAG = Kee[int](4370)
    PANU = Kee[int](4373)
    NAP = Kee[int](4374)
    GN = Kee[int](4375)
    DirectPrinting = Kee[int](4376)
    ReferencePrinting = Kee[int](4377)
    BasicImage = Kee[int](4378)
    ImagingResponder = Kee[int](4379)
    ImagingAutomaticArchive = Kee[int](4380)
    ImagingReferenceObjects = Kee[int](4381)
    Handsfree = Kee[int](4382)
    HandsfreeAudioGateway = Kee[int](4383)
    DirectPrintingReferenceObjectsService = Kee[int](4384)
    ReflectedUI = Kee[int](4385)
    BasicPrinting = Kee[int](4386)
    PrintingStatus = Kee[int](4387)
    HumanInterfaceDeviceService = Kee[int](4388)
    HardcopyCableReplacement = Kee[int](4389)
    HCRPrint = Kee[int](4390)
    HCRScan = Kee[int](4391)
    SIMAccess = Kee[int](4397)
    PhonebookAccessPCE = Kee[int](4398)
    PhonebookAccessPSE = Kee[int](4399)
    PhonebookAccess = Kee[int](4400)
    HeadsetHS = Kee[int](4401)
    MessageAccessServer = Kee[int](4402)
    MessageNotificationServer = Kee[int](4403)
    MessageAccessProfile = Kee[int](4404)
    GNSS = Kee[int](4405)
    GNSSServer = Kee[int](4406)
    Display3D = Kee[int](4407)
    Glasses3D = Kee[int](4408)
    Synchronization3D = Kee[int](4409)
    MPSProfile = Kee[int](4410)
    MPSService = Kee[int](4411)
    PnPInformation = Kee[int](4608)
    GenericNetworking = Kee[int](4609)
    GenericFileTransfer = Kee[int](4610)
    GenericAudio = Kee[int](4611)
    GenericTelephony = Kee[int](4612)
    VideoSource = Kee[int](4867)
    VideoSink = Kee[int](4868)
    VideoDistribution = Kee[int](4869)
    HDP = Kee[int](5120)
    HDPSource = Kee[int](5121)
    HDPSink = Kee[int](5122)
    GenericAccess = Kee[int](6144)
    GenericAttribute = Kee[int](6145)
    ImmediateAlert = Kee[int](6146)
    LinkLoss = Kee[int](6147)
    TxPower = Kee[int](6148)
    CurrentTimeService = Kee[int](6149)
    ReferenceTimeUpdateService = Kee[int](6150)
    NextDSTChangeService = Kee[int](6151)
    Glucose = Kee[int](6152)
    HealthThermometer = Kee[int](6153)
    DeviceInformation = Kee[int](6154)
    HeartRate = Kee[int](6157)
    PhoneAlertStatusService = Kee[int](6158)
    BatteryService = Kee[int](6159)
    BloodPressure = Kee[int](6160)
    AlertNotificationService = Kee[int](6161)
    HumanInterfaceDevice = Kee[int](6162)
    ScanParameters = Kee[int](6163)
    RunningSpeedAndCadence = Kee[int](6164)
    CyclingSpeedAndCadence = Kee[int](6166)
    CyclingPower = Kee[int](6168)
    LocationAndNavigation = Kee[int](6169)
    EnvironmentalSensing = Kee[int](6170)
    BodyComposition = Kee[int](6171)
    UserData = Kee[int](6172)
    WeightScale = Kee[int](6173)
    BondManagement = Kee[int](6174)
    ContinuousGlucoseMonitoring = Kee[int](6175)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(ServiceClassUuid)
  def serviceClassToString(uuid: ServiceClassUuid) -> str:
    """
    Calls Qt's 'QString QBluetoothUuid::serviceClassToString(ServiceClassUuid
    uuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothuuid.html#serviceClassToString

    Parameters
    ----------

    uuid : ServiceClassUuid
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothUuid::serviceClassToString(ServiceClassUuid uuid)
    return Rituals.call(
        'ritual_ZN14QBluetoothUuid20serviceClassToStringENS_16ServiceClassU'
        'uidE',
        uuid.value,
    )

  @staticmethod
  @overload(ProtocolUuid)
  def protocolToString(uuid: ProtocolUuid) -> str:
    """
    Calls Qt's 'QString QBluetoothUuid::protocolToString(ProtocolUuid uuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothuuid.html#protocolToString

    Parameters
    ----------

    uuid : ProtocolUuid
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothUuid::protocolToString(ProtocolUuid uuid)
    return Rituals.call(
        'ritual_ZN14QBluetoothUuid16protocolToStringENS_12ProtocolUuidE',
        uuid.value,
    )

  @staticmethod
  @overload(CharacteristicType)
  def characteristicToString(uuid: CharacteristicType) -> str:
    """
    Calls Qt's 'QString
    QBluetoothUuid::characteristicToString(CharacteristicType uuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothuuid.html#characteristicToString

    Parameters
    ----------

    uuid : CharacteristicType
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothUuid::characteristicToString(CharacteristicType
    #      uuid)
    return Rituals.call(
        'ritual_ZN14QBluetoothUuid22characteristicToStringENS_18Characteris'
        'ticTypeE',
        uuid.value,
    )

  @staticmethod
  @overload(DescriptorType)
  def descriptorToString(uuid: DescriptorType) -> str:
    """
    Calls Qt's 'QString QBluetoothUuid::descriptorToString(DescriptorType
    uuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothuuid.html#descriptorToString

    Parameters
    ----------

    uuid : DescriptorType
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothUuid::descriptorToString(DescriptorType uuid)
    return Rituals.call(
        'ritual_ZN14QBluetoothUuid18descriptorToStringENS_14DescriptorTypeE',
        uuid.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothUuid'

  #  Qt's '~QBluetoothUuid()'. Naming it makes this a value class: Python
  #  owns every C++ QBluetoothUuid behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QBluetoothUuidD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def minimumSize(self) -> int:
    """
    Calls Qt's 'int QBluetoothUuid::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#minimumSize
    """
    #  int QBluetoothUuid::minimumSize() const
    return self.uglySide.call('ritual_ZNK14QBluetoothUuid11minimumSizeEv')

  @overload()
  @overload(QSysInfo.Endian)
  def toUInt128(
      self,
      order: QSysInfo.Endian = QSysInfo.Endian.BigEndian,
  ) -> quint128:
    """
    Calls Qt's 'quint128 QBluetoothUuid::toUInt128(QSysInfo::Endian order)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#toUInt128

    Parameters
    ----------

    order : QSysInfo.Endian
      Passed on as its number. May be left out, as in Qt: it is then
      QSysInfo.Endian.BigEndian.

    Returns
    -------

    quint128
      A new cute quint128 around the copy Qt gave back. Python owns it.
    """
    #  quint128 QBluetoothUuid::toUInt128(QSysInfo::Endian order) const
    address = self.uglySide.call(
        'ritual_ZNK14QBluetoothUuid9toUInt128EN8QSysInfo6EndianE',
        order.value,
    )
    from . import quint128
    return quint128._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QBluetoothUuid) -> bool:
    """
    Calls Qt's 'bool operator==(const QBluetoothUuid &a, const QBluetoothUuid
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#operator==

    Parameters
    ----------

    b : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.
    """
    #  bool operator==(const QBluetoothUuid &a, const QBluetoothUuid &b)
    return Rituals.call(
        'ritual_ZeqRK14QBluetoothUuidS1_',
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
  def __ne__(self, b: QBluetoothUuid) -> bool:
    """
    Calls Qt's 'bool operator!=(const QBluetoothUuid &a, const QBluetoothUuid
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#operator!=

    Parameters
    ----------

    b : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.
    """
    #  bool operator!=(const QBluetoothUuid &a, const QBluetoothUuid &b)
    return Rituals.call(
        'ritual_ZneRK14QBluetoothUuidS1_',
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

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QBluetoothUuid &uuid)'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#operator<<

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
    #  QDebug operator<<(QDebug debug, const QBluetoothUuid &uuid)
    address = Rituals.call(
        'ritual_Zls6QDebugRK14QBluetoothUuid',
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
    Notes what was given, for Qt's 'QBluetoothUuid::QBluetoothUuid()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid
    """
    #  QBluetoothUuid::QBluetoothUuid()
    self._noteCreation(QBluetoothUuid, lambda: Rituals.call(
        'ritual_ZN14QBluetoothUuidC1Ev',
    ))

  @overload(ProtocolUuid)
  def __init__(self, uuid: ProtocolUuid) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothUuid::QBluetoothUuid(ProtocolUuid uuid)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid

    Parameters
    ----------

    uuid : ProtocolUuid
      Passed on as its number.
    """
    #  QBluetoothUuid::QBluetoothUuid(ProtocolUuid uuid)
    self._noteCreation(QBluetoothUuid, lambda: Rituals.call(
        'ritual_ZN14QBluetoothUuidC1ENS_12ProtocolUuidE', uuid.value,
    ))

  @overload(ServiceClassUuid)
  def __init__(self, uuid: ServiceClassUuid) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothUuid::QBluetoothUuid(ServiceClassUuid uuid)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid

    Parameters
    ----------

    uuid : ServiceClassUuid
      Passed on as its number.
    """
    #  QBluetoothUuid::QBluetoothUuid(ServiceClassUuid uuid)
    self._noteCreation(QBluetoothUuid, lambda: Rituals.call(
        'ritual_ZN14QBluetoothUuidC1ENS_16ServiceClassUuidE', uuid.value,
    ))

  @overload(CharacteristicType)
  def __init__(self, uuid: CharacteristicType) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothUuid::QBluetoothUuid(CharacteristicType uuid)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid

    Parameters
    ----------

    uuid : CharacteristicType
      Passed on as its number.
    """
    #  QBluetoothUuid::QBluetoothUuid(CharacteristicType uuid)
    self._noteCreation(QBluetoothUuid, lambda: Rituals.call(
        'ritual_ZN14QBluetoothUuidC1ENS_18CharacteristicTypeE', uuid.value,
    ))

  @overload(DescriptorType)
  def __init__(self, uuid: DescriptorType) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothUuid::QBluetoothUuid(DescriptorType uuid)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid

    Parameters
    ----------

    uuid : DescriptorType
      Passed on as its number.
    """
    #  QBluetoothUuid::QBluetoothUuid(DescriptorType uuid)
    self._noteCreation(QBluetoothUuid, lambda: Rituals.call(
        'ritual_ZN14QBluetoothUuidC1ENS_14DescriptorTypeE', uuid.value,
    ))

  @overload(int)
  def __init__(self, uuid: int) -> None:
    """
    Notes what was given, for Qt's 'QBluetoothUuid::QBluetoothUuid(quint16
    uuid)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid

    Parameters
    ----------

    uuid : int
      Passed on as it is.
    """
    #  QBluetoothUuid::QBluetoothUuid(quint16 uuid)
    self._noteCreation(QBluetoothUuid, lambda: Rituals.call(
        'ritual_ZN14QBluetoothUuidC1Et', uuid,
    ))

  @overload(THIS)
  def __init__(self, uuid: QBluetoothUuid) -> None:
    """
    Notes what was given, for Qt's 'QBluetoothUuid::QBluetoothUuid(const
    QBluetoothUuid &uuid)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid

    Parameters
    ----------

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.
    """
    #  QBluetoothUuid::QBluetoothUuid(const QBluetoothUuid &uuid)
    self._noteCreation(QBluetoothUuid, lambda: Rituals.call(
        'ritual_ZN14QBluetoothUuidC1ERKS_', self._valueOf(uuid),
    ))

  @overload(QUuid)
  def __init__(self, uuid: QUuid) -> None:
    """
    Notes what was given, for Qt's 'QBluetoothUuid::QBluetoothUuid(const
    QUuid &uuid)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothuuid.html#QBluetoothUuid

    Parameters
    ----------

    uuid : QUuid
      Passed on as a value: Qt reads the C++ QUuid, which stays Python's own.
    """
    #  QBluetoothUuid::QBluetoothUuid(const QUuid &uuid)
    self._noteCreation(QBluetoothUuid, lambda: Rituals.call(
        'ritual_ZN14QBluetoothUuidC1ERK5QUuid', self._valueOf(uuid),
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

  @staticmethod
  def toUInt16(*__, **_) -> Never:
    """
    Qt's 'quint16 QBluetoothUuid::toUInt16(bool *ok) const': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QBluetoothUuid.toUInt16' has no cute function yet. Qt's 'quint16 "
        "QBluetoothUuid::toUInt16(bool *ok) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toUInt32(*__, **_) -> Never:
    """
    Qt's 'quint32 QBluetoothUuid::toUInt32(bool *ok) const': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QBluetoothUuid.toUInt32' has no cute function yet. Qt's 'quint32 "
        "QBluetoothUuid::toUInt32(bool *ok) const': takes a number to "
        "change where it is.")


#  Qt's 'QList<QBluetoothUuid>': the list of QBluetoothUuid, which
#  'QList[QBluetoothUuid]' gives. It is made here, so that there is one as
#  soon as there can be a QBluetoothUuid.
QList.createKind(
    QBluetoothUuid, 'value',
    make='ritual_list_make_QBluetoothUuid',
    add='ritual_list_add_QBluetoothUuid',
    size='ritual_list_size_QBluetoothUuid',
    at='ritual_list_at_QBluetoothUuid',
    drop='ritual_list_drop_QBluetoothUuid',
)
