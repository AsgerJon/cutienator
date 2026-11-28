"""
QLowEnergyAdvertisingData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qlowenergyadvertisingdata.h, Qt 6.12.0. Changes made here are
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
  from typing import Never

  from ..QtCore import QByteArray
  from . import QBluetoothUuid
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothUuid = WAIT['QBluetoothUuid']
  QByteArray = WAIT['QByteArray']


class QLowEnergyAdvertisingData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLowEnergyAdvertisingData: a plain Python object
  standing in front of one C++ QLowEnergyAdvertisingData.

  C++ hands a QLowEnergyAdvertisingData around as a copy, so every C++
  QLowEnergyAdvertisingData behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLowEnergyAdvertisingData that has a ritual and that
  Python can call so far, 17 names in all: '__eq__', '__ne__',
  'setLocalName', 'localName', 'invalidManufacturerId',
  'setManufacturerData', 'manufacturerId', 'manufacturerData',
  'setIncludePowerLevel', 'includePowerLevel', 'setDiscoverability',
  'discoverability', 'setServices', 'services', 'setRawData', 'rawData',
  'equals'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLowEnergyAdvertisingData::~QLowEnergyAdvertisingData()': the
    destructor: Python removes its C++ QLowEnergyAdvertisingData by it, and
    has no other use for it.
  - Qt's 'QLowEnergyAdvertisingData
    &QLowEnergyAdvertisingData::operator=(const QLowEnergyAdvertisingData
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QLowEnergyAdvertisingData::swap(QLowEnergyAdvertisingData
    &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QLowEnergyAdvertisingData is created at the first use, not by
    'QLowEnergyAdvertisingData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLowEnergyAdvertisingData back gives a copy the
    ritual made for Python, in a new cute QLowEnergyAdvertisingData.
  - Each name of Qt's QLowEnergyAdvertisingData that has no cute function
    yet, 'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QLowEnergyAdvertisingData, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Discoverability(CuteNum):
    """
    The enum 'QLowEnergyAdvertisingData::Discoverability' of Qt, with the 3
    names Qt gives in it.
    """

    DiscoverabilityNone = Kee[int](0)
    DiscoverabilityLimited = Kee[int](1)
    DiscoverabilityGeneral = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def invalidManufacturerId() -> int:
    """
    Calls Qt's 'quint16 QLowEnergyAdvertisingData::invalidManufacturerId()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html
    """
    #  quint16 QLowEnergyAdvertisingData::invalidManufacturerId()
    return Rituals.call(
        'ritual_ZN25QLowEnergyAdvertisingData21invalidManufacturerIdEv',
    )

  @staticmethod
  @overload(THIS, THIS)
  def equals(
      a: QLowEnergyAdvertisingData,
      b: QLowEnergyAdvertisingData,
  ) -> bool:
    """
    Calls Qt's 'bool QLowEnergyAdvertisingData::equals(const
    QLowEnergyAdvertisingData &a, const QLowEnergyAdvertisingData &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#equals

    Parameters
    ----------

    a : QLowEnergyAdvertisingData
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingData, which
      stays Python's own.

    b : QLowEnergyAdvertisingData
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingData, which
      stays Python's own.
    """
    #  bool QLowEnergyAdvertisingData::equals(const QLowEnergyAdvertisingData
    #      &a, const QLowEnergyAdvertisingData &b)
    return Rituals.call(
        'ritual_ZN25QLowEnergyAdvertisingData6equalsERKS_S1_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLowEnergyAdvertisingData'

  #  Qt's '~QLowEnergyAdvertisingData()'. Naming it makes this a value class:
  #  Python owns every C++ QLowEnergyAdvertisingData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QLowEnergyAdvertisingDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def localName(self) -> str:
    """
    Calls Qt's 'QString QLowEnergyAdvertisingData::localName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#localName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLowEnergyAdvertisingData::localName() const
    return self.uglySide.call(
        'ritual_ZNK25QLowEnergyAdvertisingData9localNameEv',
    )

  def manufacturerId(self) -> int:
    """
    Calls Qt's 'quint16 QLowEnergyAdvertisingData::manufacturerId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#manufacturerId
    """
    #  quint16 QLowEnergyAdvertisingData::manufacturerId() const
    return self.uglySide.call(
        'ritual_ZNK25QLowEnergyAdvertisingData14manufacturerIdEv',
    )

  def manufacturerData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QLowEnergyAdvertisingData::manufacturerData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#manufacturerData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QLowEnergyAdvertisingData::manufacturerData() const
    address = self.uglySide.call(
        'ritual_ZNK25QLowEnergyAdvertisingData16manufacturerDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def includePowerLevel(self) -> bool:
    """
    Calls Qt's 'bool QLowEnergyAdvertisingData::includePowerLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#includePowerLevel
    """
    #  bool QLowEnergyAdvertisingData::includePowerLevel() const
    return self.uglySide.call(
        'ritual_ZNK25QLowEnergyAdvertisingData17includePowerLevelEv',
    )

  def discoverability(self) -> Discoverability:
    """
    Calls Qt's 'Discoverability QLowEnergyAdvertisingData::discoverability()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#discoverability

    Returns
    -------

    Discoverability
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Discoverability(number)'
      gives.
    """
    #  Discoverability QLowEnergyAdvertisingData::discoverability() const
    return QLowEnergyAdvertisingData.Discoverability(self.uglySide.call(
        'ritual_ZNK25QLowEnergyAdvertisingData15discoverabilityEv',
    ))

  def services(self) -> QList[QBluetoothUuid]:
    """
    Calls Qt's 'QList<QBluetoothUuid> QLowEnergyAdvertisingData::services()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#services

    Returns
    -------

    QList[QBluetoothUuid]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBluetoothUuid> QLowEnergyAdvertisingData::services() const
    address = self.uglySide.call(
        'ritual_ZNK25QLowEnergyAdvertisingData8servicesEv',
    )
    from . import QBluetoothUuid
    return QList[QBluetoothUuid]._cuteOwning(address)

  def rawData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QLowEnergyAdvertisingData::rawData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#rawData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QLowEnergyAdvertisingData::rawData() const
    address = self.uglySide.call(
        'ritual_ZNK25QLowEnergyAdvertisingData7rawDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLocalName(self, name: str) -> None:
    """
    Calls Qt's 'void QLowEnergyAdvertisingData::setLocalName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#setLocalName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLowEnergyAdvertisingData::setLocalName(const QString &name)
    self.uglySide.call(
        'ritual_ZN25QLowEnergyAdvertisingData12setLocalNameERK7QString',
        name,
    )

  @overload(int, QByteArray)
  def setManufacturerData(self, id: int, data: QByteArray) -> None:
    """
    Calls Qt's 'void QLowEnergyAdvertisingData::setManufacturerData(quint16
    id, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#setManufacturerData

    Parameters
    ----------

    id : int
      Passed on as it is.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyAdvertisingData::setManufacturerData(quint16 id, const
    #      QByteArray &data)
    self.uglySide.call(
        'ritual_ZN25QLowEnergyAdvertisingData19setManufacturerDataEtRK10QBy'
        'teArray',
        id, self._valueOf(data),
    )

  @overload(bool)
  def setIncludePowerLevel(self, doInclude: bool) -> None:
    """
    Calls Qt's 'void QLowEnergyAdvertisingData::setIncludePowerLevel(bool
    doInclude)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html

    Parameters
    ----------

    doInclude : bool
      Passed on as it is.
    """
    #  void QLowEnergyAdvertisingData::setIncludePowerLevel(bool doInclude)
    self.uglySide.call(
        'ritual_ZN25QLowEnergyAdvertisingData20setIncludePowerLevelEb',
        doInclude,
    )

  @overload(Discoverability)
  def setDiscoverability(self, mode: Discoverability) -> None:
    """
    Calls Qt's 'void
    QLowEnergyAdvertisingData::setDiscoverability(Discoverability mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#setDiscoverability

    Parameters
    ----------

    mode : Discoverability
      Passed on as its number.
    """
    #  void QLowEnergyAdvertisingData::setDiscoverability(Discoverability
    #      mode)
    self.uglySide.call(
        'ritual_ZN25QLowEnergyAdvertisingData18setDiscoverabilityENS_15Disc'
        'overabilityE',
        mode.value,
    )

  @overload(QList[QBluetoothUuid])
  def setServices(self, services: QList[QBluetoothUuid]) -> None:
    """
    Calls Qt's 'void QLowEnergyAdvertisingData::setServices(const
    QList<QBluetoothUuid> &services)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#setServices

    Parameters
    ----------

    services : QList[QBluetoothUuid]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QLowEnergyAdvertisingData::setServices(const
    #      QList<QBluetoothUuid> &services)
    self.uglySide.call(
        'ritual_ZN25QLowEnergyAdvertisingData11setServicesERK5QListI14QBlue'
        'toothUuidE',
        self._valueOf(services),
    )

  @overload(QByteArray)
  def setRawData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QLowEnergyAdvertisingData::setRawData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#setRawData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyAdvertisingData::setRawData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN25QLowEnergyAdvertisingData10setRawDataERK10QByteArray',
        self._valueOf(data),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QLowEnergyAdvertisingData) -> bool:
    """
    Calls Qt's 'bool operator==(const QLowEnergyAdvertisingData &a, const
    QLowEnergyAdvertisingData &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#operator==

    Parameters
    ----------

    b : QLowEnergyAdvertisingData
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingData, which
      stays Python's own.
    """
    #  bool operator==(const QLowEnergyAdvertisingData &a, const
    #      QLowEnergyAdvertisingData &b)
    return Rituals.call(
        'ritual_ZeqRK25QLowEnergyAdvertisingDataS1_',
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
  def __ne__(self, b: QLowEnergyAdvertisingData) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLowEnergyAdvertisingData &a, const
    QLowEnergyAdvertisingData &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html#operator!=

    Parameters
    ----------

    b : QLowEnergyAdvertisingData
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingData, which
      stays Python's own.
    """
    #  bool operator!=(const QLowEnergyAdvertisingData &a, const
    #      QLowEnergyAdvertisingData &b)
    return Rituals.call(
        'ritual_ZneRK25QLowEnergyAdvertisingDataS1_',
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
    'QLowEnergyAdvertisingData::QLowEnergyAdvertisingData()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html
    """
    #  QLowEnergyAdvertisingData::QLowEnergyAdvertisingData()
    self._noteCreation(QLowEnergyAdvertisingData, lambda: Rituals.call(
        'ritual_ZN25QLowEnergyAdvertisingDataC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLowEnergyAdvertisingData) -> None:
    """
    Notes what was given, for Qt's
    'QLowEnergyAdvertisingData::QLowEnergyAdvertisingData(const
    QLowEnergyAdvertisingData &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingdata.html

    Parameters
    ----------

    other : QLowEnergyAdvertisingData
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingData, which
      stays Python's own.
    """
    #  QLowEnergyAdvertisingData::QLowEnergyAdvertisingData(const
    #      QLowEnergyAdvertisingData &other)
    self._noteCreation(QLowEnergyAdvertisingData, lambda: Rituals.call(
        'ritual_ZN25QLowEnergyAdvertisingDataC1ERKS_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyAdvertisingData::swap(QLowEnergyAdvertisingData
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLowEnergyAdvertisingData.swap' has no cute function yet. Qt's "
        "'void QLowEnergyAdvertisingData::swap(QLowEnergyAdvertisingData "
        "&other)': takes a type Python has no way to hand over yet.")
