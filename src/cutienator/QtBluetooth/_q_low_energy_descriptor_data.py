"""
QLowEnergyDescriptorData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qlowenergydescriptordata.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QBluetooth

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


class QLowEnergyDescriptorData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLowEnergyDescriptorData: a plain Python object
  standing in front of one C++ QLowEnergyDescriptorData.

  C++ hands a QLowEnergyDescriptorData around as a copy, so every C++
  QLowEnergyDescriptorData behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLowEnergyDescriptorData that has a ritual and that
  Python can call so far, 14 names in all: '__eq__', '__ne__', 'value',
  'setValue', 'uuid', 'setUuid', 'isValid', 'setReadPermissions',
  'isReadable', 'readConstraints', 'setWritePermissions', 'isWritable',
  'writeConstraints', 'equals'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLowEnergyDescriptorData::~QLowEnergyDescriptorData()': the
    destructor: Python removes its C++ QLowEnergyDescriptorData by it, and
    has no other use for it.
  - Qt's 'QLowEnergyDescriptorData &QLowEnergyDescriptorData::operator=(const
    QLowEnergyDescriptorData &other)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'void QLowEnergyDescriptorData::swap(QLowEnergyDescriptorData
    &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QLowEnergyDescriptorData is created at the first use, not by
    'QLowEnergyDescriptorData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLowEnergyDescriptorData back gives a copy the ritual
    made for Python, in a new cute QLowEnergyDescriptorData.
  - Each name of Qt's QLowEnergyDescriptorData that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(
      a: QLowEnergyDescriptorData,
      b: QLowEnergyDescriptorData,
  ) -> bool:
    """
    Calls Qt's 'bool QLowEnergyDescriptorData::equals(const
    QLowEnergyDescriptorData &a, const QLowEnergyDescriptorData &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#equals

    Parameters
    ----------

    a : QLowEnergyDescriptorData
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptorData, which
      stays Python's own.

    b : QLowEnergyDescriptorData
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptorData, which
      stays Python's own.
    """
    #  bool QLowEnergyDescriptorData::equals(const QLowEnergyDescriptorData
    #      &a, const QLowEnergyDescriptorData &b)
    return Rituals.call(
        'ritual_ZN24QLowEnergyDescriptorData6equalsERKS_S1_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLowEnergyDescriptorData'

  #  Qt's '~QLowEnergyDescriptorData()'. Naming it makes this a value class:
  #  Python owns every C++ QLowEnergyDescriptorData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QLowEnergyDescriptorDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QLowEnergyDescriptorData::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#value

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QLowEnergyDescriptorData::value() const
    address = self.uglySide.call(
        'ritual_ZNK24QLowEnergyDescriptorData5valueEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def uuid(self) -> QBluetoothUuid:
    """
    Calls Qt's 'QBluetoothUuid QLowEnergyDescriptorData::uuid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergydescriptordata.html#uuid

    Returns
    -------

    QBluetoothUuid
      A new cute QBluetoothUuid around the copy Qt gave back. Python owns it.
    """
    #  QBluetoothUuid QLowEnergyDescriptorData::uuid() const
    address = self.uglySide.call(
        'ritual_ZNK24QLowEnergyDescriptorData4uuidEv',
    )
    from . import QBluetoothUuid
    return QBluetoothUuid._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QLowEnergyDescriptorData::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#isValid
    """
    #  bool QLowEnergyDescriptorData::isValid() const
    return self.uglySide.call(
        'ritual_ZNK24QLowEnergyDescriptorData7isValidEv',
    )

  def isReadable(self) -> bool:
    """
    Calls Qt's 'bool QLowEnergyDescriptorData::isReadable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#isReadable
    """
    #  bool QLowEnergyDescriptorData::isReadable() const
    return self.uglySide.call(
        'ritual_ZNK24QLowEnergyDescriptorData10isReadableEv',
    )

  def readConstraints(self) -> QBluetooth.AttAccessConstraints:
    """
    Calls Qt's 'QBluetooth::AttAccessConstraints
    QLowEnergyDescriptorData::readConstraints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#readConstraints

    Returns
    -------

    QBluetooth.AttAccessConstraints
      The value standing for the combination Qt gave back.
    """
    #  QBluetooth::AttAccessConstraints
    #      QLowEnergyDescriptorData::readConstraints() const
    return QBluetooth.AttAccessConstraints(self.uglySide.call(
        'ritual_ZNK24QLowEnergyDescriptorData15readConstraintsEv',
    ))

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QLowEnergyDescriptorData::isWritable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#isWritable
    """
    #  bool QLowEnergyDescriptorData::isWritable() const
    return self.uglySide.call(
        'ritual_ZNK24QLowEnergyDescriptorData10isWritableEv',
    )

  def writeConstraints(self) -> QBluetooth.AttAccessConstraints:
    """
    Calls Qt's 'QBluetooth::AttAccessConstraints
    QLowEnergyDescriptorData::writeConstraints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#writeConstraints

    Returns
    -------

    QBluetooth.AttAccessConstraints
      The value standing for the combination Qt gave back.
    """
    #  QBluetooth::AttAccessConstraints
    #      QLowEnergyDescriptorData::writeConstraints() const
    return QBluetooth.AttAccessConstraints(self.uglySide.call(
        'ritual_ZNK24QLowEnergyDescriptorData16writeConstraintsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setValue(self, value: QByteArray) -> None:
    """
    Calls Qt's 'void QLowEnergyDescriptorData::setValue(const QByteArray
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#setValue

    Parameters
    ----------

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyDescriptorData::setValue(const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN24QLowEnergyDescriptorData8setValueERK10QByteArray',
        self._valueOf(value),
    )

  @overload(QBluetoothUuid)
  def setUuid(self, uuid: QBluetoothUuid) -> None:
    """
    Calls Qt's 'void QLowEnergyDescriptorData::setUuid(const QBluetoothUuid
    &uuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#setUuid

    Parameters
    ----------

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.
    """
    #  void QLowEnergyDescriptorData::setUuid(const QBluetoothUuid &uuid)
    self.uglySide.call(
        'ritual_ZN24QLowEnergyDescriptorData7setUuidERK14QBluetoothUuid',
        self._valueOf(uuid),
    )

  @overload(bool)
  @overload(bool, QBluetooth.AttAccessConstraints)
  def setReadPermissions(
      self,
      readable: bool,
      constraints: QBluetooth.AttAccessConstraints = (
          QBluetooth.AttAccessConstraints()),
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyDescriptorData::setReadPermissions(bool
    readable, QBluetooth::AttAccessConstraints constraints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#setReadPermissions

    Parameters
    ----------

    readable : bool
      Passed on as it is.

    constraints : QBluetooth.AttAccessConstraints
      Passed on as its number. May be left out, as in Qt: it is then
      QBluetooth.AttAccessConstraints().
    """
    #  void QLowEnergyDescriptorData::setReadPermissions(bool readable,
    #      QBluetooth::AttAccessConstraints constraints)
    self.uglySide.call(
        'ritual_ZN24QLowEnergyDescriptorData18setReadPermissionsEb6QFlagsIN'
        '10QBluetooth19AttAccessConstraintEE',
        readable, constraints.value,
    )

  @overload(bool)
  @overload(bool, QBluetooth.AttAccessConstraints)
  def setWritePermissions(
      self,
      writable: bool,
      constraints: QBluetooth.AttAccessConstraints = (
          QBluetooth.AttAccessConstraints()),
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyDescriptorData::setWritePermissions(bool
    writable, QBluetooth::AttAccessConstraints constraints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#setWritePermissions

    Parameters
    ----------

    writable : bool
      Passed on as it is.

    constraints : QBluetooth.AttAccessConstraints
      Passed on as its number. May be left out, as in Qt: it is then
      QBluetooth.AttAccessConstraints().
    """
    #  void QLowEnergyDescriptorData::setWritePermissions(bool writable,
    #      QBluetooth::AttAccessConstraints constraints)
    self.uglySide.call(
        'ritual_ZN24QLowEnergyDescriptorData19setWritePermissionsEb6QFlagsI'
        'N10QBluetooth19AttAccessConstraintEE',
        writable, constraints.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QLowEnergyDescriptorData) -> bool:
    """
    Calls Qt's 'bool operator==(const QLowEnergyDescriptorData &a, const
    QLowEnergyDescriptorData &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#operator==

    Parameters
    ----------

    b : QLowEnergyDescriptorData
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptorData, which
      stays Python's own.
    """
    #  bool operator==(const QLowEnergyDescriptorData &a, const
    #      QLowEnergyDescriptorData &b)
    return Rituals.call(
        'ritual_ZeqRK24QLowEnergyDescriptorDataS1_',
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
  def __ne__(self, b: QLowEnergyDescriptorData) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLowEnergyDescriptorData &a, const
    QLowEnergyDescriptorData &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html#operator!=

    Parameters
    ----------

    b : QLowEnergyDescriptorData
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptorData, which
      stays Python's own.
    """
    #  bool operator!=(const QLowEnergyDescriptorData &a, const
    #      QLowEnergyDescriptorData &b)
    return Rituals.call(
        'ritual_ZneRK24QLowEnergyDescriptorDataS1_',
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
    'QLowEnergyDescriptorData::QLowEnergyDescriptorData()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html
    """
    #  QLowEnergyDescriptorData::QLowEnergyDescriptorData()
    self._noteCreation(QLowEnergyDescriptorData, lambda: Rituals.call(
        'ritual_ZN24QLowEnergyDescriptorDataC1Ev',
    ))

  @overload(QBluetoothUuid, QByteArray)
  def __init__(self, uuid: QBluetoothUuid, value: QByteArray) -> None:
    """
    Notes what was given, for Qt's
    'QLowEnergyDescriptorData::QLowEnergyDescriptorData(const QBluetoothUuid
    &uuid, const QByteArray &value)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html

    Parameters
    ----------

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QLowEnergyDescriptorData::QLowEnergyDescriptorData(const
    #      QBluetoothUuid &uuid, const QByteArray &value)
    self._noteCreation(QLowEnergyDescriptorData, lambda: Rituals.call(
        'ritual_ZN24QLowEnergyDescriptorDataC1ERK14QBluetoothUuidRK10QByteA'
        'rray',
        self._valueOf(uuid), self._valueOf(value),
    ))

  @overload(THIS)
  def __init__(self, other: QLowEnergyDescriptorData) -> None:
    """
    Notes what was given, for Qt's
    'QLowEnergyDescriptorData::QLowEnergyDescriptorData(const
    QLowEnergyDescriptorData &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptordata.html

    Parameters
    ----------

    other : QLowEnergyDescriptorData
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptorData, which
      stays Python's own.
    """
    #  QLowEnergyDescriptorData::QLowEnergyDescriptorData(const
    #      QLowEnergyDescriptorData &other)
    self._noteCreation(QLowEnergyDescriptorData, lambda: Rituals.call(
        'ritual_ZN24QLowEnergyDescriptorDataC1ERKS_', self._valueOf(other),
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
    Qt's 'void QLowEnergyDescriptorData::swap(QLowEnergyDescriptorData
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLowEnergyDescriptorData.swap' has no cute function yet. Qt's "
        "'void QLowEnergyDescriptorData::swap(QLowEnergyDescriptorData "
        "&other)': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<QLowEnergyDescriptorData>': the list of
#  QLowEnergyDescriptorData, which 'QList[QLowEnergyDescriptorData]' gives.
#  It is made here, so that there is one as soon as there can be a
#  QLowEnergyDescriptorData.
QList.createKind(
    QLowEnergyDescriptorData, 'value',
    make='ritual_list_make_QLowEnergyDescriptorData',
    add='ritual_list_add_QLowEnergyDescriptorData',
    size='ritual_list_size_QLowEnergyDescriptorData',
    at='ritual_list_at_QLowEnergyDescriptorData',
    drop='ritual_list_drop_QLowEnergyDescriptorData',
)
