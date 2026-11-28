"""
QLowEnergyServiceData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qlowenergyservicedata.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QBluetoothUuid, QLowEnergyCharacteristicData
  from . import QLowEnergyService
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothUuid = WAIT['QBluetoothUuid']
  QLowEnergyCharacteristicData = WAIT['QLowEnergyCharacteristicData']
  QLowEnergyService = WAIT['QLowEnergyService']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLowEnergyServiceData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLowEnergyServiceData: a plain Python object standing
  in front of one C++ QLowEnergyServiceData.

  C++ hands a QLowEnergyServiceData around as a copy, so every C++
  QLowEnergyServiceData behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLowEnergyServiceData that has a ritual and that
  Python can call so far, 14 names in all: '__eq__', '__ne__', 'type',
  'setType', 'uuid', 'setUuid', 'includedServices', 'setIncludedServices',
  'addIncludedService', 'characteristics', 'setCharacteristics',
  'addCharacteristic', 'isValid', 'equals'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLowEnergyServiceData::~QLowEnergyServiceData()': the destructor:
    Python removes its C++ QLowEnergyServiceData by it, and has no other use
    for it.
  - Qt's 'QLowEnergyServiceData &QLowEnergyServiceData::operator=(const
    QLowEnergyServiceData &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'void QLowEnergyServiceData::swap(QLowEnergyServiceData &other)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QLowEnergyServiceData is created at the first use, not by
    'QLowEnergyServiceData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLowEnergyServiceData back gives a copy the ritual
    made for Python, in a new cute QLowEnergyServiceData.
  - Each name of Qt's QLowEnergyServiceData that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QLowEnergyServiceData, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ServiceType(CuteNum):
    """
    The enum 'QLowEnergyServiceData::ServiceType' of Qt, with the 2 names Qt
    gives in it.
    """

    ServiceTypePrimary = Kee[int](10240)
    ServiceTypeSecondary = Kee[int](10241)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(a: QLowEnergyServiceData, b: QLowEnergyServiceData) -> bool:
    """
    Calls Qt's 'bool QLowEnergyServiceData::equals(const
    QLowEnergyServiceData &a, const QLowEnergyServiceData &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservicedata.html#equals

    Parameters
    ----------

    a : QLowEnergyServiceData
      Passed on as a value: Qt reads the C++ QLowEnergyServiceData, which
      stays Python's own.

    b : QLowEnergyServiceData
      Passed on as a value: Qt reads the C++ QLowEnergyServiceData, which
      stays Python's own.
    """
    #  bool QLowEnergyServiceData::equals(const QLowEnergyServiceData &a,
    #      const QLowEnergyServiceData &b)
    return Rituals.call(
        'ritual_ZN21QLowEnergyServiceData6equalsERKS_S1_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLowEnergyServiceData'

  #  Qt's '~QLowEnergyServiceData()'. Naming it makes this a value class:
  #  Python owns every C++ QLowEnergyServiceData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QLowEnergyServiceDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> ServiceType:
    """
    Calls Qt's 'ServiceType QLowEnergyServiceData::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservicedata.html#type

    Returns
    -------

    ServiceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ServiceType(number)'
      gives.
    """
    #  ServiceType QLowEnergyServiceData::type() const
    return QLowEnergyServiceData.ServiceType(self.uglySide.call(
        'ritual_ZNK21QLowEnergyServiceData4typeEv',
    ))

  def uuid(self) -> QBluetoothUuid:
    """
    Calls Qt's 'QBluetoothUuid QLowEnergyServiceData::uuid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservicedata.html#uuid

    Returns
    -------

    QBluetoothUuid
      A new cute QBluetoothUuid around the copy Qt gave back. Python owns it.
    """
    #  QBluetoothUuid QLowEnergyServiceData::uuid() const
    address = self.uglySide.call('ritual_ZNK21QLowEnergyServiceData4uuidEv')
    from . import QBluetoothUuid
    return QBluetoothUuid._cuteOwning(address)

  def includedServices(self) -> QList[QLowEnergyService]:
    """
    Calls Qt's 'QList<QLowEnergyService *>
    QLowEnergyServiceData::includedServices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservicedata.html#includedServices

    Returns
    -------

    QList[QLowEnergyService]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLowEnergyService *> QLowEnergyServiceData::includedServices()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QLowEnergyServiceData16includedServicesEv',
    )
    from . import QLowEnergyService
    return QList[QLowEnergyService]._cuteOwning(address)

  def characteristics(self) -> QList[QLowEnergyCharacteristicData]:
    """
    Calls Qt's 'QList<QLowEnergyCharacteristicData>
    QLowEnergyServiceData::characteristics() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservicedata.html#characteristics

    Returns
    -------

    QList[QLowEnergyCharacteristicData]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLowEnergyCharacteristicData>
    #      QLowEnergyServiceData::characteristics() const
    address = self.uglySide.call(
        'ritual_ZNK21QLowEnergyServiceData15characteristicsEv',
    )
    from . import QLowEnergyCharacteristicData
    return QList[QLowEnergyCharacteristicData]._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QLowEnergyServiceData::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservicedata.html#isValid
    """
    #  bool QLowEnergyServiceData::isValid() const
    return self.uglySide.call('ritual_ZNK21QLowEnergyServiceData7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ServiceType)
  def setType(self, type: ServiceType) -> None:
    """
    Calls Qt's 'void QLowEnergyServiceData::setType(ServiceType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservicedata.html#setType

    Parameters
    ----------

    type : ServiceType
      Passed on as its number.
    """
    #  void QLowEnergyServiceData::setType(ServiceType type)
    self.uglySide.call(
        'ritual_ZN21QLowEnergyServiceData7setTypeENS_11ServiceTypeE',
        type.value,
    )

  @overload(QBluetoothUuid)
  def setUuid(self, uuid: QBluetoothUuid) -> None:
    """
    Calls Qt's 'void QLowEnergyServiceData::setUuid(const QBluetoothUuid
    &uuid)'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergyservicedata.html#setUuid

    Parameters
    ----------

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.
    """
    #  void QLowEnergyServiceData::setUuid(const QBluetoothUuid &uuid)
    self.uglySide.call(
        'ritual_ZN21QLowEnergyServiceData7setUuidERK14QBluetoothUuid',
        self._valueOf(uuid),
    )

  @overload(QList[QLowEnergyService])
  def setIncludedServices(self, services: QList[QLowEnergyService]) -> None:
    """
    Calls Qt's 'void QLowEnergyServiceData::setIncludedServices(const
    QList<QLowEnergyService *> &services)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservicedata.html#setIncludedServices

    Parameters
    ----------

    services : QList[QLowEnergyService]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QLowEnergyServiceData::setIncludedServices(const
    #      QList<QLowEnergyService *> &services)
    self.uglySide.call(
        'ritual_ZN21QLowEnergyServiceData19setIncludedServicesERK5QListIP17'
        'QLowEnergyServiceE',
        self._valueOf(services),
    )

  @overload(QList[QLowEnergyCharacteristicData])
  def setCharacteristics(
      self,
      characteristics: QList[QLowEnergyCharacteristicData],
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyServiceData::setCharacteristics(const
    QList<QLowEnergyCharacteristicData> &characteristics)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservicedata.html#setCharacteristics

    Parameters
    ----------

    characteristics : QList[QLowEnergyCharacteristicData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QLowEnergyServiceData::setCharacteristics(const
    #      QList<QLowEnergyCharacteristicData> &characteristics)
    self.uglySide.call(
        'ritual_ZN21QLowEnergyServiceData18setCharacteristicsERK5QListI28QL'
        'owEnergyCharacteristicDataE',
        self._valueOf(characteristics),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QLowEnergyServiceData) -> bool:
    """
    Calls Qt's 'bool operator==(const QLowEnergyServiceData &a, const
    QLowEnergyServiceData &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservicedata.html#operator==

    Parameters
    ----------

    b : QLowEnergyServiceData
      Passed on as a value: Qt reads the C++ QLowEnergyServiceData, which
      stays Python's own.
    """
    #  bool operator==(const QLowEnergyServiceData &a, const
    #      QLowEnergyServiceData &b)
    return Rituals.call(
        'ritual_ZeqRK21QLowEnergyServiceDataS1_',
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
  def __ne__(self, b: QLowEnergyServiceData) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLowEnergyServiceData &a, const
    QLowEnergyServiceData &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservicedata.html#operator!=

    Parameters
    ----------

    b : QLowEnergyServiceData
      Passed on as a value: Qt reads the C++ QLowEnergyServiceData, which
      stays Python's own.
    """
    #  bool operator!=(const QLowEnergyServiceData &a, const
    #      QLowEnergyServiceData &b)
    return Rituals.call(
        'ritual_ZneRK21QLowEnergyServiceDataS1_',
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
    'QLowEnergyServiceData::QLowEnergyServiceData()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservicedata.html#QLowEnergyServiceData
    """
    #  QLowEnergyServiceData::QLowEnergyServiceData()
    self._noteCreation(QLowEnergyServiceData, lambda: Rituals.call(
        'ritual_ZN21QLowEnergyServiceDataC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLowEnergyServiceData) -> None:
    """
    Notes what was given, for Qt's
    'QLowEnergyServiceData::QLowEnergyServiceData(const QLowEnergyServiceData
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservicedata.html#QLowEnergyServiceData

    Parameters
    ----------

    other : QLowEnergyServiceData
      Passed on as a value: Qt reads the C++ QLowEnergyServiceData, which
      stays Python's own.
    """
    #  QLowEnergyServiceData::QLowEnergyServiceData(const
    #      QLowEnergyServiceData &other)
    self._noteCreation(QLowEnergyServiceData, lambda: Rituals.call(
        'ritual_ZN21QLowEnergyServiceDataC1ERKS_', self._valueOf(other),
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

  @overload(QLowEnergyService)
  @overload(NoneType)
  def addIncludedService(self, service: Optional[QLowEnergyService]) -> None:
    """
    Calls Qt's 'void
    QLowEnergyServiceData::addIncludedService(QLowEnergyService *service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservicedata.html#addIncludedService

    Parameters
    ----------

    service : Optional[QLowEnergyService]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLowEnergyServiceData::addIncludedService(QLowEnergyService
    #      *service)
    self.uglySide.call(
        'ritual_ZN21QLowEnergyServiceData18addIncludedServiceEP17QLowEnergy'
        'Service',
        self._addressOf(service),
    )

  @overload(QLowEnergyCharacteristicData)
  def addCharacteristic(
      self,
      characteristic: QLowEnergyCharacteristicData,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyServiceData::addCharacteristic(const
    QLowEnergyCharacteristicData &characteristic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyservicedata.html#addCharacteristic

    Parameters
    ----------

    characteristic : QLowEnergyCharacteristicData
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristicData,
      which stays Python's own.
    """
    #  void QLowEnergyServiceData::addCharacteristic(const
    #      QLowEnergyCharacteristicData &characteristic)
    self.uglySide.call(
        'ritual_ZN21QLowEnergyServiceData17addCharacteristicERK28QLowEnergy'
        'CharacteristicData',
        self._valueOf(characteristic),
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyServiceData::swap(QLowEnergyServiceData &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLowEnergyServiceData.swap' has no cute function yet. Qt's 'void "
        "QLowEnergyServiceData::swap(QLowEnergyServiceData &other)': takes "
        "a type Python has no way to hand over yet.")
