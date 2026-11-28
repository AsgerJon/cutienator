"""
QLowEnergyService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qlowenergyservice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QBluetoothUuid, QLowEnergyCharacteristic
  from . import QLowEnergyDescriptor, QLowEnergyServicePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothUuid = WAIT['QBluetoothUuid']
  QByteArray = WAIT['QByteArray']
  QLowEnergyCharacteristic = WAIT['QLowEnergyCharacteristic']
  QLowEnergyDescriptor = WAIT['QLowEnergyDescriptor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLowEnergyService(QObject):
  """
  The cute side of Qt's QLowEnergyService: a plain Python object standing in
  front of one C++ QLowEnergyService.

  It is built on the cute 'QObject', as Qt's QLowEnergyService is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLowEnergyService that has a ritual and that Python
  can call so far, 24 names in all: 'metaObject', 'tr', 'includedServices',
  'type', 'state', 'characteristic', 'characteristics', 'serviceUuid',
  'serviceName', 'discoverDetails', 'error', 'contains',
  'readCharacteristic', 'writeCharacteristic', 'readDescriptor',
  'writeDescriptor', 'stateChanged', 'characteristicChanged',
  'characteristicRead', 'characteristicWritten', 'descriptorRead',
  'descriptorWritten', 'errorOccurred', 'd_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLowEnergyService::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QLowEnergyService::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QLowEnergyService::~QLowEnergyService()': the destructor: Python
    never removes a C++ QLowEnergyService.
  - Qt's 'const QLowEnergyServicePrivate *QLowEnergyService::d_func() const':
    takes in Python what 'QLowEnergyServicePrivate
    *QLowEnergyService::d_func()' takes.
  - Qt's 'QLowEnergyService::QLowEnergyService(
    QSharedPointer<QLowEnergyServicePrivate> p, QObject *parent)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QLowEnergyService is created at the first use, not by
    'QLowEnergyService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLowEnergyService.
  - Qt tells when it has removed the C++ QLowEnergyService. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QLowEnergyService that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QLowEnergyService, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DiscoveryMode(CuteNum):
    """
    The enum 'QLowEnergyService::DiscoveryMode' of Qt, with the 2 names Qt
    gives in it.
    """

    FullDiscovery = Kee[int](0)
    SkipValueDiscovery = Kee[int](1)

  class ServiceError(CuteNum):
    """
    The enum 'QLowEnergyService::ServiceError' of Qt, with the 7 names Qt
    gives in it.
    """

    NoError = Kee[int](0)
    OperationError = Kee[int](1)
    CharacteristicWriteError = Kee[int](2)
    DescriptorWriteError = Kee[int](3)
    UnknownError = Kee[int](4)
    CharacteristicReadError = Kee[int](5)
    DescriptorReadError = Kee[int](6)

  class ServiceState(CuteNum):
    """
    The enum 'QLowEnergyService::ServiceState' of Qt, with the 8 names Qt
    gives in it.
    """

    InvalidService = Kee[int](0)
    RemoteService = Kee[int](1)
    RemoteServiceDiscovering = Kee[int](2)
    RemoteServiceDiscovered = Kee[int](3)
    LocalService = Kee[int](4)
    DiscoveryRequired = Kee[int](1)
    DiscoveringService = Kee[int](2)
    ServiceDiscovered = Kee[int](3)

  class ServiceType(CuteFlags):
    """
    The flags enum 'QLowEnergyService::ServiceType' of Qt, with the 2 names
    Qt gives in it. Qt names the type of its combinations
    'QLowEnergyService::ServiceTypes'.
    """

    PrimaryService = 0x1
    IncludedService = 0x2

  ServiceTypes = ServiceType

  class WriteMode(CuteNum):
    """
    The enum 'QLowEnergyService::WriteMode' of Qt, with the 3 names Qt gives
    in it.
    """

    WriteWithResponse = Kee[int](0)
    WriteWithoutResponse = Kee[int](1)
    WriteSigned = Kee[int](2)

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
    Calls Qt's 'QString QLowEnergyService::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservice.html#tr

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
    #  QString QLowEnergyService::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QLowEnergyService2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLowEnergyService'

  #  A C++ QLowEnergyService Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLowEnergyService'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLowEnergyService::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLowEnergyService::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QLowEnergyService10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def includedServices(self) -> QList[QBluetoothUuid]:
    """
    Calls Qt's 'QList<QBluetoothUuid> QLowEnergyService::includedServices()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#includedServices

    Returns
    -------

    QList[QBluetoothUuid]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBluetoothUuid> QLowEnergyService::includedServices() const
    address = self.uglySide.call(
        'ritual_ZNK17QLowEnergyService16includedServicesEv',
    )
    from . import QBluetoothUuid
    return QList[QBluetoothUuid]._cuteOwning(address)

  def type(self) -> ServiceTypes:
    """
    Calls Qt's 'QLowEnergyService::ServiceTypes QLowEnergyService::type()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservice.html#type

    Returns
    -------

    ServiceTypes
      The value standing for the combination Qt gave back.
    """
    #  QLowEnergyService::ServiceTypes QLowEnergyService::type() const
    return QLowEnergyService.ServiceTypes(self.uglySide.call(
        'ritual_ZNK17QLowEnergyService4typeEv',
    ))

  def state(self) -> ServiceState:
    """
    Calls Qt's 'QLowEnergyService::ServiceState QLowEnergyService::state()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservice.html#state

    Returns
    -------

    ServiceState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ServiceState(number)'
      gives.
    """
    #  QLowEnergyService::ServiceState QLowEnergyService::state() const
    return QLowEnergyService.ServiceState(self.uglySide.call(
        'ritual_ZNK17QLowEnergyService5stateEv',
    ))

  @overload(QBluetoothUuid)
  def characteristic(self, uuid: QBluetoothUuid) -> QLowEnergyCharacteristic:
    """
    Calls Qt's 'QLowEnergyCharacteristic
    QLowEnergyService::characteristic(const QBluetoothUuid &uuid) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#characteristic

    Parameters
    ----------

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    Returns
    -------

    QLowEnergyCharacteristic
      A new cute QLowEnergyCharacteristic around the copy Qt gave back.
      Python owns it.
    """
    #  QLowEnergyCharacteristic QLowEnergyService::characteristic(const
    #      QBluetoothUuid &uuid) const
    address = self.uglySide.call(
        'ritual_ZNK17QLowEnergyService14characteristicERK14QBluetoothUuid',
        self._valueOf(uuid),
    )
    from . import QLowEnergyCharacteristic
    return QLowEnergyCharacteristic._cuteOwning(address)

  def characteristics(self) -> QList[QLowEnergyCharacteristic]:
    """
    Calls Qt's 'QList<QLowEnergyCharacteristic>
    QLowEnergyService::characteristics() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#characteristics

    Returns
    -------

    QList[QLowEnergyCharacteristic]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLowEnergyCharacteristic> QLowEnergyService::characteristics()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QLowEnergyService15characteristicsEv',
    )
    from . import QLowEnergyCharacteristic
    return QList[QLowEnergyCharacteristic]._cuteOwning(address)

  def serviceUuid(self) -> QBluetoothUuid:
    """
    Calls Qt's 'QBluetoothUuid QLowEnergyService::serviceUuid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservice.html#serviceUuid

    Returns
    -------

    QBluetoothUuid
      A new cute QBluetoothUuid around the copy Qt gave back. Python owns it.
    """
    #  QBluetoothUuid QLowEnergyService::serviceUuid() const
    address = self.uglySide.call(
        'ritual_ZNK17QLowEnergyService11serviceUuidEv',
    )
    from . import QBluetoothUuid
    return QBluetoothUuid._cuteOwning(address)

  def serviceName(self) -> str:
    """
    Calls Qt's 'QString QLowEnergyService::serviceName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservice.html#serviceName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLowEnergyService::serviceName() const
    return self.uglySide.call('ritual_ZNK17QLowEnergyService11serviceNameEv')

  def error(self) -> ServiceError:
    """
    Calls Qt's 'ServiceError QLowEnergyService::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservice.html#error

    Returns
    -------

    ServiceError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ServiceError(number)'
      gives.
    """
    #  ServiceError QLowEnergyService::error() const
    return QLowEnergyService.ServiceError(self.uglySide.call(
        'ritual_ZNK17QLowEnergyService5errorEv',
    ))

  @overload(QLowEnergyCharacteristic)
  def contains(self, characteristic: QLowEnergyCharacteristic) -> bool:
    """
    Calls Qt's 'bool QLowEnergyService::contains(const
    QLowEnergyCharacteristic &characteristic) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservice.html#contains

    Parameters
    ----------

    characteristic : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.
    """
    #  bool QLowEnergyService::contains(const QLowEnergyCharacteristic
    #      &characteristic) const
    return self.uglySide.call(
        'ritual_ZNK17QLowEnergyService8containsERK24QLowEnergyCharacteristi'
        'c',
        self._valueOf(characteristic),
    )

  @overload(QLowEnergyDescriptor)
  def contains(self, descriptor: QLowEnergyDescriptor) -> bool:
    """
    Calls Qt's 'bool QLowEnergyService::contains(const QLowEnergyDescriptor
    &descriptor) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservice.html#contains

    Parameters
    ----------

    descriptor : QLowEnergyDescriptor
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptor, which
      stays Python's own.
    """
    #  bool QLowEnergyService::contains(const QLowEnergyDescriptor
    #      &descriptor) const
    return self.uglySide.call(
        'ritual_ZNK17QLowEnergyService8containsERK20QLowEnergyDescriptor',
        self._valueOf(descriptor),
    )

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
    Qt's 'QLowEnergyService::QLowEnergyService(
    QSharedPointer<QLowEnergyServicePrivate> p, QObject *parent)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLowEnergyService.__init__' has no cute function yet. Qt's "
        "'QLowEnergyService::QLowEnergyService(QSharedPointer<QLowEnergyServ"
        "icePrivate> p, QObject *parent)': takes a type Python has no way "
        "to hand over yet.")

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
  @overload(DiscoveryMode)
  def discoverDetails(
      self,
      mode: DiscoveryMode = DiscoveryMode.FullDiscovery,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyService::discoverDetails(DiscoveryMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#discoverDetails

    Parameters
    ----------

    mode : DiscoveryMode
      Passed on as its number. May be left out, as in Qt: it is then
      DiscoveryMode.FullDiscovery.
    """
    #  void QLowEnergyService::discoverDetails(DiscoveryMode mode)
    self.uglySide.call(
        'ritual_ZN17QLowEnergyService15discoverDetailsENS_13DiscoveryModeE',
        mode.value,
    )

  @overload(QLowEnergyCharacteristic)
  def readCharacteristic(
      self,
      characteristic: QLowEnergyCharacteristic,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyService::readCharacteristic(const
    QLowEnergyCharacteristic &characteristic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#readCharacteristic

    Parameters
    ----------

    characteristic : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.
    """
    #  void QLowEnergyService::readCharacteristic(const
    #      QLowEnergyCharacteristic &characteristic)
    self.uglySide.call(
        'ritual_ZN17QLowEnergyService18readCharacteristicERK24QLowEnergyCha'
        'racteristic',
        self._valueOf(characteristic),
    )

  @overload(QLowEnergyCharacteristic, QByteArray)
  @overload(QLowEnergyCharacteristic, QByteArray, WriteMode)
  def writeCharacteristic(
      self,
      characteristic: QLowEnergyCharacteristic,
      newValue: QByteArray,
      mode: WriteMode = WriteMode.WriteWithResponse,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyService::writeCharacteristic(const
    QLowEnergyCharacteristic &characteristic, const QByteArray &newValue,
    WriteMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#writeCharacteristic

    Parameters
    ----------

    characteristic : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.

    newValue : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    mode : WriteMode
      Passed on as its number. May be left out, as in Qt: it is then
      WriteMode.WriteWithResponse.
    """
    #  void QLowEnergyService::writeCharacteristic(const
    #      QLowEnergyCharacteristic &characteristic, const QByteArray
    #      &newValue, WriteMode mode)
    self.uglySide.call(
        'ritual_ZN17QLowEnergyService19writeCharacteristicERK24QLowEnergyCh'
        'aracteristicRK10QByteArrayNS_9WriteModeE',
        self._valueOf(characteristic), self._valueOf(newValue), mode.value,
    )

  @overload(QLowEnergyDescriptor)
  def readDescriptor(self, descriptor: QLowEnergyDescriptor) -> None:
    """
    Calls Qt's 'void QLowEnergyService::readDescriptor(const
    QLowEnergyDescriptor &descriptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#readDescriptor

    Parameters
    ----------

    descriptor : QLowEnergyDescriptor
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptor, which
      stays Python's own.
    """
    #  void QLowEnergyService::readDescriptor(const QLowEnergyDescriptor
    #      &descriptor)
    self.uglySide.call(
        'ritual_ZN17QLowEnergyService14readDescriptorERK20QLowEnergyDescrip'
        'tor',
        self._valueOf(descriptor),
    )

  @overload(QLowEnergyDescriptor, QByteArray)
  def writeDescriptor(
      self,
      descriptor: QLowEnergyDescriptor,
      newValue: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyService::writeDescriptor(const
    QLowEnergyDescriptor &descriptor, const QByteArray &newValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#writeDescriptor

    Parameters
    ----------

    descriptor : QLowEnergyDescriptor
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptor, which
      stays Python's own.

    newValue : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyService::writeDescriptor(const QLowEnergyDescriptor
    #      &descriptor, const QByteArray &newValue)
    self.uglySide.call(
        'ritual_ZN17QLowEnergyService15writeDescriptorERK20QLowEnergyDescri'
        'ptorRK10QByteArray',
        self._valueOf(descriptor), self._valueOf(newValue),
    )

  @overload(ServiceState)
  def stateChanged(self, newState: ServiceState) -> None:
    """
    Calls Qt's 'void
    QLowEnergyService::stateChanged(QLowEnergyService::ServiceState
    newState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#stateChanged

    Parameters
    ----------

    newState : ServiceState
      Passed on as its number.
    """
    #  void QLowEnergyService::stateChanged(QLowEnergyService::ServiceState
    #      newState)
    self.uglySide.call(
        'ritual_ZN17QLowEnergyService12stateChangedENS_12ServiceStateE',
        newState.value,
    )

  @overload(QLowEnergyCharacteristic, QByteArray)
  def characteristicChanged(
      self,
      info: QLowEnergyCharacteristic,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyService::characteristicChanged(const
    QLowEnergyCharacteristic &info, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#characteristicChanged

    Parameters
    ----------

    info : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyService::characteristicChanged(const
    #      QLowEnergyCharacteristic &info, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN17QLowEnergyService21characteristicChangedERK24QLowEnergy'
        'CharacteristicRK10QByteArray',
        self._valueOf(info), self._valueOf(value),
    )

  @overload(QLowEnergyCharacteristic, QByteArray)
  def characteristicRead(
      self,
      info: QLowEnergyCharacteristic,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyService::characteristicRead(const
    QLowEnergyCharacteristic &info, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#characteristicRead

    Parameters
    ----------

    info : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyService::characteristicRead(const
    #      QLowEnergyCharacteristic &info, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN17QLowEnergyService18characteristicReadERK24QLowEnergyCha'
        'racteristicRK10QByteArray',
        self._valueOf(info), self._valueOf(value),
    )

  @overload(QLowEnergyCharacteristic, QByteArray)
  def characteristicWritten(
      self,
      info: QLowEnergyCharacteristic,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyService::characteristicWritten(const
    QLowEnergyCharacteristic &info, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#characteristicWritten

    Parameters
    ----------

    info : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyService::characteristicWritten(const
    #      QLowEnergyCharacteristic &info, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN17QLowEnergyService21characteristicWrittenERK24QLowEnergy'
        'CharacteristicRK10QByteArray',
        self._valueOf(info), self._valueOf(value),
    )

  @overload(QLowEnergyDescriptor, QByteArray)
  def descriptorRead(
      self,
      info: QLowEnergyDescriptor,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyService::descriptorRead(const
    QLowEnergyDescriptor &info, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#descriptorRead

    Parameters
    ----------

    info : QLowEnergyDescriptor
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptor, which
      stays Python's own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyService::descriptorRead(const QLowEnergyDescriptor
    #      &info, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN17QLowEnergyService14descriptorReadERK20QLowEnergyDescrip'
        'torRK10QByteArray',
        self._valueOf(info), self._valueOf(value),
    )

  @overload(QLowEnergyDescriptor, QByteArray)
  def descriptorWritten(
      self,
      info: QLowEnergyDescriptor,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyService::descriptorWritten(const
    QLowEnergyDescriptor &info, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#descriptorWritten

    Parameters
    ----------

    info : QLowEnergyDescriptor
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptor, which
      stays Python's own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyService::descriptorWritten(const QLowEnergyDescriptor
    #      &info, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN17QLowEnergyService17descriptorWrittenERK20QLowEnergyDesc'
        'riptorRK10QByteArray',
        self._valueOf(info), self._valueOf(value),
    )

  @overload(ServiceError)
  def errorOccurred(self, error: ServiceError) -> None:
    """
    Calls Qt's 'void
    QLowEnergyService::errorOccurred(QLowEnergyService::ServiceError error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservice.html#errorOccurred

    Parameters
    ----------

    error : ServiceError
      Passed on as its number.
    """
    #  void QLowEnergyService::errorOccurred(QLowEnergyService::ServiceError
    #      error)
    self.uglySide.call(
        'ritual_ZN17QLowEnergyService13errorOccurredENS_12ServiceErrorE',
        error.value,
    )

  def d_func(self) -> Optional[QLowEnergyServicePrivate]:
    """
    Calls Qt's 'QLowEnergyServicePrivate *QLowEnergyService::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservice.html#d_func

    Returns
    -------

    Optional[QLowEnergyServicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLowEnergyServicePrivate *QLowEnergyService::d_func()
    address = self.uglySide.call('ritual_ZN17QLowEnergyService6d_funcEv')
    from . import QLowEnergyServicePrivate
    return QLowEnergyServicePrivate._cuteAt(address)


#  Qt's 'QList<QLowEnergyService *>': the list of QLowEnergyService, which
#  'QList[QLowEnergyService]' gives. It is made here, so that there is one as
#  soon as there can be a QLowEnergyService.
QList.createKind(
    QLowEnergyService, 'address',
    make='ritual_list_make_QLowEnergyService_ptr',
    add='ritual_list_add_QLowEnergyService_ptr',
    size='ritual_list_size_QLowEnergyService_ptr',
    at='ritual_list_at_QLowEnergyService_ptr',
    drop='ritual_list_drop_QLowEnergyService_ptr',
)
