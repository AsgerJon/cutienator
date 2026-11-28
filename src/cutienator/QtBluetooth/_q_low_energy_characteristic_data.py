"""
QLowEnergyCharacteristicData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qlowenergycharacteristicdata.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QBluetooth, QLowEnergyCharacteristic

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
  from . import QBluetoothUuid, QLowEnergyDescriptorData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothUuid = WAIT['QBluetoothUuid']
  QByteArray = WAIT['QByteArray']
  QLowEnergyDescriptorData = WAIT['QLowEnergyDescriptorData']


class QLowEnergyCharacteristicData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLowEnergyCharacteristicData: a plain Python object
  standing in front of one C++ QLowEnergyCharacteristicData.

  C++ hands a QLowEnergyCharacteristicData around as a copy, so every C++
  QLowEnergyCharacteristicData behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QLowEnergyCharacteristicData that has a ritual and
  that Python can call so far, 20 names in all: '__eq__', '__ne__', 'uuid',
  'setUuid', 'value', 'setValue', 'properties', 'setProperties',
  'descriptors', 'setDescriptors', 'addDescriptor', 'setReadConstraints',
  'readConstraints', 'setWriteConstraints', 'writeConstraints',
  'setValueLength', 'minimumValueLength', 'maximumValueLength', 'isValid',
  'equals'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLowEnergyCharacteristicData::~QLowEnergyCharacteristicData()': the
    destructor: Python removes its C++ QLowEnergyCharacteristicData by it,
    and has no other use for it.
  - Qt's 'QLowEnergyCharacteristicData
    &QLowEnergyCharacteristicData::operator=(const
    QLowEnergyCharacteristicData &other)': assignment: Python binds a name
    and has no operator for it.
  - Qt's 'void
    QLowEnergyCharacteristicData::swap(QLowEnergyCharacteristicData &other)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QLowEnergyCharacteristicData is created at the first use, not by
    'QLowEnergyCharacteristicData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLowEnergyCharacteristicData back gives a copy the
    ritual made for Python, in a new cute QLowEnergyCharacteristicData.
  - Each name of Qt's QLowEnergyCharacteristicData that has no cute function
    yet, 'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(
      a: QLowEnergyCharacteristicData,
      b: QLowEnergyCharacteristicData,
  ) -> bool:
    """
    Calls Qt's 'bool QLowEnergyCharacteristicData::equals(const
    QLowEnergyCharacteristicData &a, const QLowEnergyCharacteristicData &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#equals

    Parameters
    ----------

    a : QLowEnergyCharacteristicData
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristicData,
      which stays Python's own.

    b : QLowEnergyCharacteristicData
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristicData,
      which stays Python's own.
    """
    #  bool QLowEnergyCharacteristicData::equals(const
    #      QLowEnergyCharacteristicData &a, const
    #      QLowEnergyCharacteristicData &b)
    return Rituals.call(
        'ritual_ZN28QLowEnergyCharacteristicData6equalsERKS_S1_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLowEnergyCharacteristicData'

  #  Qt's '~QLowEnergyCharacteristicData()'. Naming it makes this a value
  #  class: Python owns every C++ QLowEnergyCharacteristicData behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QLowEnergyCharacteristicDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def uuid(self) -> QBluetoothUuid:
    """
    Calls Qt's 'QBluetoothUuid QLowEnergyCharacteristicData::uuid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#uuid

    Returns
    -------

    QBluetoothUuid
      A new cute QBluetoothUuid around the copy Qt gave back. Python owns it.
    """
    #  QBluetoothUuid QLowEnergyCharacteristicData::uuid() const
    address = self.uglySide.call(
        'ritual_ZNK28QLowEnergyCharacteristicData4uuidEv',
    )
    from . import QBluetoothUuid
    return QBluetoothUuid._cuteOwning(address)

  def value(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QLowEnergyCharacteristicData::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#value

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QLowEnergyCharacteristicData::value() const
    address = self.uglySide.call(
        'ritual_ZNK28QLowEnergyCharacteristicData5valueEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def properties(self) -> QLowEnergyCharacteristic.PropertyTypes:
    """
    Calls Qt's 'QLowEnergyCharacteristic::PropertyTypes
    QLowEnergyCharacteristicData::properties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#properties

    Returns
    -------

    QLowEnergyCharacteristic.PropertyTypes
      The value standing for the combination Qt gave back.
    """
    #  QLowEnergyCharacteristic::PropertyTypes
    #      QLowEnergyCharacteristicData::properties() const
    return QLowEnergyCharacteristic.PropertyTypes(self.uglySide.call(
        'ritual_ZNK28QLowEnergyCharacteristicData10propertiesEv',
    ))

  def descriptors(self) -> QList[QLowEnergyDescriptorData]:
    """
    Calls Qt's 'QList<QLowEnergyDescriptorData>
    QLowEnergyCharacteristicData::descriptors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#descriptors

    Returns
    -------

    QList[QLowEnergyDescriptorData]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLowEnergyDescriptorData>
    #      QLowEnergyCharacteristicData::descriptors() const
    address = self.uglySide.call(
        'ritual_ZNK28QLowEnergyCharacteristicData11descriptorsEv',
    )
    from . import QLowEnergyDescriptorData
    return QList[QLowEnergyDescriptorData]._cuteOwning(address)

  def readConstraints(self) -> QBluetooth.AttAccessConstraints:
    """
    Calls Qt's 'QBluetooth::AttAccessConstraints
    QLowEnergyCharacteristicData::readConstraints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#readConstraints

    Returns
    -------

    QBluetooth.AttAccessConstraints
      The value standing for the combination Qt gave back.
    """
    #  QBluetooth::AttAccessConstraints
    #      QLowEnergyCharacteristicData::readConstraints() const
    return QBluetooth.AttAccessConstraints(self.uglySide.call(
        'ritual_ZNK28QLowEnergyCharacteristicData15readConstraintsEv',
    ))

  def writeConstraints(self) -> QBluetooth.AttAccessConstraints:
    """
    Calls Qt's 'QBluetooth::AttAccessConstraints
    QLowEnergyCharacteristicData::writeConstraints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#writeConstraints

    Returns
    -------

    QBluetooth.AttAccessConstraints
      The value standing for the combination Qt gave back.
    """
    #  QBluetooth::AttAccessConstraints
    #      QLowEnergyCharacteristicData::writeConstraints() const
    return QBluetooth.AttAccessConstraints(self.uglySide.call(
        'ritual_ZNK28QLowEnergyCharacteristicData16writeConstraintsEv',
    ))

  def minimumValueLength(self) -> int:
    """
    Calls Qt's 'int QLowEnergyCharacteristicData::minimumValueLength()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html
    """
    #  int QLowEnergyCharacteristicData::minimumValueLength() const
    return self.uglySide.call(
        'ritual_ZNK28QLowEnergyCharacteristicData18minimumValueLengthEv',
    )

  def maximumValueLength(self) -> int:
    """
    Calls Qt's 'int QLowEnergyCharacteristicData::maximumValueLength()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html
    """
    #  int QLowEnergyCharacteristicData::maximumValueLength() const
    return self.uglySide.call(
        'ritual_ZNK28QLowEnergyCharacteristicData18maximumValueLengthEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QLowEnergyCharacteristicData::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#isValid
    """
    #  bool QLowEnergyCharacteristicData::isValid() const
    return self.uglySide.call(
        'ritual_ZNK28QLowEnergyCharacteristicData7isValidEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBluetoothUuid)
  def setUuid(self, uuid: QBluetoothUuid) -> None:
    """
    Calls Qt's 'void QLowEnergyCharacteristicData::setUuid(const
    QBluetoothUuid &uuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#setUuid

    Parameters
    ----------

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.
    """
    #  void QLowEnergyCharacteristicData::setUuid(const QBluetoothUuid &uuid)
    self.uglySide.call(
        'ritual_ZN28QLowEnergyCharacteristicData7setUuidERK14QBluetoothUuid',
        self._valueOf(uuid),
    )

  @overload(QByteArray)
  def setValue(self, value: QByteArray) -> None:
    """
    Calls Qt's 'void QLowEnergyCharacteristicData::setValue(const QByteArray
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#setValue

    Parameters
    ----------

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyCharacteristicData::setValue(const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN28QLowEnergyCharacteristicData8setValueERK10QByteArray',
        self._valueOf(value),
    )

  @overload(QLowEnergyCharacteristic.PropertyTypes)
  def setProperties(
      self,
      properties: QLowEnergyCharacteristic.PropertyTypes,
  ) -> None:
    """
    Calls Qt's 'void
    QLowEnergyCharacteristicData::setProperties(QLowEnergyCharacteristic::
    PropertyTypes properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#setProperties

    Parameters
    ----------

    properties : QLowEnergyCharacteristic.PropertyTypes
      Passed on as its number.
    """
    #  void QLowEnergyCharacteristicData::setProperties(
    #      QLowEnergyCharacteristic::PropertyTypes properties)
    self.uglySide.call(
        'ritual_ZN28QLowEnergyCharacteristicData13setPropertiesE6QFlagsIN24'
        'QLowEnergyCharacteristic12PropertyTypeEE',
        properties.value,
    )

  @overload(QList[QLowEnergyDescriptorData])
  def setDescriptors(
      self,
      descriptors: QList[QLowEnergyDescriptorData],
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyCharacteristicData::setDescriptors(const
    QList<QLowEnergyDescriptorData> &descriptors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#setDescriptors

    Parameters
    ----------

    descriptors : QList[QLowEnergyDescriptorData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QLowEnergyCharacteristicData::setDescriptors(const
    #      QList<QLowEnergyDescriptorData> &descriptors)
    self.uglySide.call(
        'ritual_ZN28QLowEnergyCharacteristicData14setDescriptorsERK5QListI2'
        '4QLowEnergyDescriptorDataE',
        self._valueOf(descriptors),
    )

  @overload(QBluetooth.AttAccessConstraints)
  def setReadConstraints(
      self,
      constraints: QBluetooth.AttAccessConstraints,
  ) -> None:
    """
    Calls Qt's 'void
    QLowEnergyCharacteristicData::setReadConstraints(QBluetooth::
    AttAccessConstraints constraints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html

    Parameters
    ----------

    constraints : QBluetooth.AttAccessConstraints
      Passed on as its number.
    """
    #  void QLowEnergyCharacteristicData::setReadConstraints(QBluetooth::
    #      AttAccessConstraints constraints)
    self.uglySide.call(
        'ritual_ZN28QLowEnergyCharacteristicData18setReadConstraintsE6QFlag'
        'sIN10QBluetooth19AttAccessConstraintEE',
        constraints.value,
    )

  @overload(QBluetooth.AttAccessConstraints)
  def setWriteConstraints(
      self,
      constraints: QBluetooth.AttAccessConstraints,
  ) -> None:
    """
    Calls Qt's 'void
    QLowEnergyCharacteristicData::setWriteConstraints(QBluetooth::
    AttAccessConstraints constraints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html

    Parameters
    ----------

    constraints : QBluetooth.AttAccessConstraints
      Passed on as its number.
    """
    #  void QLowEnergyCharacteristicData::setWriteConstraints(QBluetooth::
    #      AttAccessConstraints constraints)
    self.uglySide.call(
        'ritual_ZN28QLowEnergyCharacteristicData19setWriteConstraintsE6QFla'
        'gsIN10QBluetooth19AttAccessConstraintEE',
        constraints.value,
    )

  @overload(int, int)
  def setValueLength(self, minimum: int, maximum: int) -> None:
    """
    Calls Qt's 'void QLowEnergyCharacteristicData::setValueLength(int
    minimum, int maximum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#setValueLength

    Parameters
    ----------

    minimum : int
      Passed on as it is.

    maximum : int
      Passed on as it is.
    """
    #  void QLowEnergyCharacteristicData::setValueLength(int minimum, int
    #      maximum)
    self.uglySide.call(
        'ritual_ZN28QLowEnergyCharacteristicData14setValueLengthEii',
        minimum, maximum,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QLowEnergyCharacteristicData) -> bool:
    """
    Calls Qt's 'bool operator==(const QLowEnergyCharacteristicData &a, const
    QLowEnergyCharacteristicData &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#operator==

    Parameters
    ----------

    b : QLowEnergyCharacteristicData
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristicData,
      which stays Python's own.
    """
    #  bool operator==(const QLowEnergyCharacteristicData &a, const
    #      QLowEnergyCharacteristicData &b)
    return Rituals.call(
        'ritual_ZeqRK28QLowEnergyCharacteristicDataS1_',
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
  def __ne__(self, b: QLowEnergyCharacteristicData) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLowEnergyCharacteristicData &a, const
    QLowEnergyCharacteristicData &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#operator!=

    Parameters
    ----------

    b : QLowEnergyCharacteristicData
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristicData,
      which stays Python's own.
    """
    #  bool operator!=(const QLowEnergyCharacteristicData &a, const
    #      QLowEnergyCharacteristicData &b)
    return Rituals.call(
        'ritual_ZneRK28QLowEnergyCharacteristicDataS1_',
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
    'QLowEnergyCharacteristicData::QLowEnergyCharacteristicData()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html
    """
    #  QLowEnergyCharacteristicData::QLowEnergyCharacteristicData()
    self._noteCreation(QLowEnergyCharacteristicData, lambda: Rituals.call(
        'ritual_ZN28QLowEnergyCharacteristicDataC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLowEnergyCharacteristicData) -> None:
    """
    Notes what was given, for Qt's
    'QLowEnergyCharacteristicData::QLowEnergyCharacteristicData(const
    QLowEnergyCharacteristicData &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html

    Parameters
    ----------

    other : QLowEnergyCharacteristicData
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristicData,
      which stays Python's own.
    """
    #  QLowEnergyCharacteristicData::QLowEnergyCharacteristicData(const
    #      QLowEnergyCharacteristicData &other)
    self._noteCreation(QLowEnergyCharacteristicData, lambda: Rituals.call(
        'ritual_ZN28QLowEnergyCharacteristicDataC1ERKS_',
        self._valueOf(other),
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

  @overload(QLowEnergyDescriptorData)
  def addDescriptor(self, descriptor: QLowEnergyDescriptorData) -> None:
    """
    Calls Qt's 'void QLowEnergyCharacteristicData::addDescriptor(const
    QLowEnergyDescriptorData &descriptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristicdata.html#addDescriptor

    Parameters
    ----------

    descriptor : QLowEnergyDescriptorData
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptorData, which
      stays Python's own.
    """
    #  void QLowEnergyCharacteristicData::addDescriptor(const
    #      QLowEnergyDescriptorData &descriptor)
    self.uglySide.call(
        'ritual_ZN28QLowEnergyCharacteristicData13addDescriptorERK24QLowEne'
        'rgyDescriptorData',
        self._valueOf(descriptor),
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void
    QLowEnergyCharacteristicData::swap(QLowEnergyCharacteristicData &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLowEnergyCharacteristicData.swap' has no cute function yet. Qt's "
        "'void "
        "QLowEnergyCharacteristicData::swap(QLowEnergyCharacteristicData "
        "&other)': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<QLowEnergyCharacteristicData>': the list of
#  QLowEnergyCharacteristicData, which 'QList[QLowEnergyCharacteristicData]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QLowEnergyCharacteristicData.
QList.createKind(
    QLowEnergyCharacteristicData, 'value',
    make='ritual_list_make_QLowEnergyCharacteristicData',
    add='ritual_list_add_QLowEnergyCharacteristicData',
    size='ritual_list_size_QLowEnergyCharacteristicData',
    at='ritual_list_at_QLowEnergyCharacteristicData',
    drop='ritual_list_drop_QLowEnergyCharacteristicData',
)
