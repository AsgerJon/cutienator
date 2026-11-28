"""
QLowEnergyCharacteristic binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qlowenergycharacteristic.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
  from . import QBluetoothUuid, QLowEnergyDescriptor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothUuid = WAIT['QBluetoothUuid']


class QLowEnergyCharacteristic(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLowEnergyCharacteristic: a plain Python object
  standing in front of one C++ QLowEnergyCharacteristic.

  C++ hands a QLowEnergyCharacteristic around as a copy, so every C++
  QLowEnergyCharacteristic behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLowEnergyCharacteristic that has a ritual and that
  Python can call so far, 13 names in all: '__eq__', '__ne__', 'name',
  'uuid', 'value', 'properties', 'descriptor', 'descriptors',
  'clientCharacteristicConfiguration', 'isValid', 'handle',
  'attributeHandle', 'equals'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLowEnergyCharacteristic::~QLowEnergyCharacteristic()': the
    destructor: Python removes its C++ QLowEnergyCharacteristic by it, and
    has no other use for it.
  - Qt's 'QLowEnergyCharacteristic &QLowEnergyCharacteristic::operator=(const
    QLowEnergyCharacteristic &other)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QLowEnergyCharacteristic::QLowEnergyCharacteristic(
    QSharedPointer<QLowEnergyServicePrivate> p, QLowEnergyHandle handle)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QLowEnergyCharacteristic is created at the first use, not by
    'QLowEnergyCharacteristic(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLowEnergyCharacteristic back gives a copy the ritual
    made for Python, in a new cute QLowEnergyCharacteristic.
  """

  #  The enums Qt writes inside QLowEnergyCharacteristic, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class PropertyType(CuteFlags):
    """
    The flags enum 'QLowEnergyCharacteristic::PropertyType' of Qt, with the 9
    names Qt gives in it. Qt names the type of its combinations
    'QLowEnergyCharacteristic::PropertyTypes'.
    """

    Unknown = 0x0
    Broadcasting = 0x1
    Read = 0x2
    WriteNoResponse = 0x4
    Write = 0x8
    Notify = 0x10
    Indicate = 0x20
    WriteSigned = 0x40
    ExtendedProperty = 0x80

  PropertyTypes = PropertyType

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(
      a: QLowEnergyCharacteristic,
      b: QLowEnergyCharacteristic,
  ) -> bool:
    """
    Calls Qt's 'bool QLowEnergyCharacteristic::equals(const
    QLowEnergyCharacteristic &a, const QLowEnergyCharacteristic &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html#equals

    Parameters
    ----------

    a : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.

    b : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.
    """
    #  bool QLowEnergyCharacteristic::equals(const QLowEnergyCharacteristic
    #      &a, const QLowEnergyCharacteristic &b)
    return Rituals.call(
        'ritual_ZN24QLowEnergyCharacteristic6equalsERKS_S1_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLowEnergyCharacteristic'

  #  Qt's '~QLowEnergyCharacteristic()'. Naming it makes this a value class:
  #  Python owns every C++ QLowEnergyCharacteristic behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QLowEnergyCharacteristicD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QLowEnergyCharacteristic::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergycharacteristic.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLowEnergyCharacteristic::name() const
    return self.uglySide.call('ritual_ZNK24QLowEnergyCharacteristic4nameEv')

  def uuid(self) -> QBluetoothUuid:
    """
    Calls Qt's 'QBluetoothUuid QLowEnergyCharacteristic::uuid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergycharacteristic.html#uuid

    Returns
    -------

    QBluetoothUuid
      A new cute QBluetoothUuid around the copy Qt gave back. Python owns it.
    """
    #  QBluetoothUuid QLowEnergyCharacteristic::uuid() const
    address = self.uglySide.call(
        'ritual_ZNK24QLowEnergyCharacteristic4uuidEv',
    )
    from . import QBluetoothUuid
    return QBluetoothUuid._cuteOwning(address)

  def value(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QLowEnergyCharacteristic::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html#value

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QLowEnergyCharacteristic::value() const
    address = self.uglySide.call(
        'ritual_ZNK24QLowEnergyCharacteristic5valueEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def properties(self) -> PropertyTypes:
    """
    Calls Qt's 'QLowEnergyCharacteristic::PropertyTypes
    QLowEnergyCharacteristic::properties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html#properties

    Returns
    -------

    PropertyTypes
      The value standing for the combination Qt gave back.
    """
    #  QLowEnergyCharacteristic::PropertyTypes
    #      QLowEnergyCharacteristic::properties() const
    return QLowEnergyCharacteristic.PropertyTypes(self.uglySide.call(
        'ritual_ZNK24QLowEnergyCharacteristic10propertiesEv',
    ))

  @overload(QBluetoothUuid)
  def descriptor(self, uuid: QBluetoothUuid) -> QLowEnergyDescriptor:
    """
    Calls Qt's 'QLowEnergyDescriptor
    QLowEnergyCharacteristic::descriptor(const QBluetoothUuid &uuid) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html#descriptor

    Parameters
    ----------

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.

    Returns
    -------

    QLowEnergyDescriptor
      A new cute QLowEnergyDescriptor around the copy Qt gave back. Python
      owns it.
    """
    #  QLowEnergyDescriptor QLowEnergyCharacteristic::descriptor(const
    #      QBluetoothUuid &uuid) const
    address = self.uglySide.call(
        'ritual_ZNK24QLowEnergyCharacteristic10descriptorERK14QBluetoothUui'
        'd',
        self._valueOf(uuid),
    )
    from . import QLowEnergyDescriptor
    return QLowEnergyDescriptor._cuteOwning(address)

  def descriptors(self) -> QList[QLowEnergyDescriptor]:
    """
    Calls Qt's 'QList<QLowEnergyDescriptor>
    QLowEnergyCharacteristic::descriptors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html#descriptors

    Returns
    -------

    QList[QLowEnergyDescriptor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLowEnergyDescriptor> QLowEnergyCharacteristic::descriptors()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QLowEnergyCharacteristic11descriptorsEv',
    )
    from . import QLowEnergyDescriptor
    return QList[QLowEnergyDescriptor]._cuteOwning(address)

  def clientCharacteristicConfiguration(self) -> QLowEnergyDescriptor:
    """
    Calls Qt's 'QLowEnergyDescriptor
    QLowEnergyCharacteristic::clientCharacteristicConfiguration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html

    Returns
    -------

    QLowEnergyDescriptor
      A new cute QLowEnergyDescriptor around the copy Qt gave back. Python
      owns it.
    """
    #  QLowEnergyDescriptor
    #      QLowEnergyCharacteristic::clientCharacteristicConfiguration()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QLowEnergyCharacteristic33clientCharacteristicConfigur'
        'ationEv',
    )
    from . import QLowEnergyDescriptor
    return QLowEnergyDescriptor._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QLowEnergyCharacteristic::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html#isValid
    """
    #  bool QLowEnergyCharacteristic::isValid() const
    return self.uglySide.call(
        'ritual_ZNK24QLowEnergyCharacteristic7isValidEv',
    )

  def handle(self) -> int:
    """
    Calls Qt's 'QLowEnergyHandle QLowEnergyCharacteristic::handle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html#handle
    """
    #  QLowEnergyHandle QLowEnergyCharacteristic::handle() const
    return self.uglySide.call(
        'ritual_ZNK24QLowEnergyCharacteristic6handleEv',
    )

  def attributeHandle(self) -> int:
    """
    Calls Qt's 'QLowEnergyHandle QLowEnergyCharacteristic::attributeHandle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html#attributeHandle
    """
    #  QLowEnergyHandle QLowEnergyCharacteristic::attributeHandle() const
    return self.uglySide.call(
        'ritual_ZNK24QLowEnergyCharacteristic15attributeHandleEv',
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

  @overload(THIS)
  def __eq__(self, b: QLowEnergyCharacteristic) -> bool:
    """
    Calls Qt's 'bool operator==(const QLowEnergyCharacteristic &a, const
    QLowEnergyCharacteristic &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html#operator==

    Parameters
    ----------

    b : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.
    """
    #  bool operator==(const QLowEnergyCharacteristic &a, const
    #      QLowEnergyCharacteristic &b)
    return Rituals.call(
        'ritual_ZeqRK24QLowEnergyCharacteristicS1_',
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
  def __ne__(self, b: QLowEnergyCharacteristic) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLowEnergyCharacteristic &a, const
    QLowEnergyCharacteristic &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html#operator!=

    Parameters
    ----------

    b : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.
    """
    #  bool operator!=(const QLowEnergyCharacteristic &a, const
    #      QLowEnergyCharacteristic &b)
    return Rituals.call(
        'ritual_ZneRK24QLowEnergyCharacteristicS1_',
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
    'QLowEnergyCharacteristic::QLowEnergyCharacteristic()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html
    """
    #  QLowEnergyCharacteristic::QLowEnergyCharacteristic()
    self._noteCreation(QLowEnergyCharacteristic, lambda: Rituals.call(
        'ritual_ZN24QLowEnergyCharacteristicC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLowEnergyCharacteristic) -> None:
    """
    Notes what was given, for Qt's
    'QLowEnergyCharacteristic::QLowEnergyCharacteristic(const
    QLowEnergyCharacteristic &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergycharacteristic.html

    Parameters
    ----------

    other : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.
    """
    #  QLowEnergyCharacteristic::QLowEnergyCharacteristic(const
    #      QLowEnergyCharacteristic &other)
    self._noteCreation(QLowEnergyCharacteristic, lambda: Rituals.call(
        'ritual_ZN24QLowEnergyCharacteristicC1ERKS_', self._valueOf(other),
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


#  Qt's 'QList<QLowEnergyCharacteristic>': the list of
#  QLowEnergyCharacteristic, which 'QList[QLowEnergyCharacteristic]' gives.
#  It is made here, so that there is one as soon as there can be a
#  QLowEnergyCharacteristic.
QList.createKind(
    QLowEnergyCharacteristic, 'value',
    make='ritual_list_make_QLowEnergyCharacteristic',
    add='ritual_list_add_QLowEnergyCharacteristic',
    size='ritual_list_size_QLowEnergyCharacteristic',
    at='ritual_list_at_QLowEnergyCharacteristic',
    drop='ritual_list_drop_QLowEnergyCharacteristic',
)
