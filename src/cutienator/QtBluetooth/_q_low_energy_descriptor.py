"""
QLowEnergyDescriptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qlowenergydescriptor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList
from . import QBluetoothUuid

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray


class QLowEnergyDescriptor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLowEnergyDescriptor: a plain Python object standing
  in front of one C++ QLowEnergyDescriptor.

  C++ hands a QLowEnergyDescriptor around as a copy, so every C++
  QLowEnergyDescriptor behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLowEnergyDescriptor that has a ritual and that
  Python can call so far, 10 names in all: '__eq__', '__ne__', 'isValid',
  'value', 'uuid', 'name', 'type', 'handle', 'characteristicHandle',
  'equals'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLowEnergyDescriptor::~QLowEnergyDescriptor()': the destructor:
    Python removes its C++ QLowEnergyDescriptor by it, and has no other use
    for it.
  - Qt's 'QLowEnergyDescriptor &QLowEnergyDescriptor::operator=(const
    QLowEnergyDescriptor &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QLowEnergyDescriptor::QLowEnergyDescriptor(
    QSharedPointer<QLowEnergyServicePrivate> p, QLowEnergyHandle charHandle,
    QLowEnergyHandle descHandle)': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QLowEnergyDescriptor is created at the first use, not by
    'QLowEnergyDescriptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLowEnergyDescriptor back gives a copy the ritual
    made for Python, in a new cute QLowEnergyDescriptor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(a: QLowEnergyDescriptor, b: QLowEnergyDescriptor) -> bool:
    """
    Calls Qt's 'bool QLowEnergyDescriptor::equals(const QLowEnergyDescriptor
    &a, const QLowEnergyDescriptor &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergydescriptor.html#equals

    Parameters
    ----------

    a : QLowEnergyDescriptor
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptor, which
      stays Python's own.

    b : QLowEnergyDescriptor
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptor, which
      stays Python's own.
    """
    #  bool QLowEnergyDescriptor::equals(const QLowEnergyDescriptor &a, const
    #      QLowEnergyDescriptor &b)
    return Rituals.call(
        'ritual_ZN20QLowEnergyDescriptor6equalsERKS_S1_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLowEnergyDescriptor'

  #  Qt's '~QLowEnergyDescriptor()'. Naming it makes this a value class:
  #  Python owns every C++ QLowEnergyDescriptor behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QLowEnergyDescriptorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QLowEnergyDescriptor::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergydescriptor.html#isValid
    """
    #  bool QLowEnergyDescriptor::isValid() const
    return self.uglySide.call('ritual_ZNK20QLowEnergyDescriptor7isValidEv')

  def value(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QLowEnergyDescriptor::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergydescriptor.html#value

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QLowEnergyDescriptor::value() const
    address = self.uglySide.call('ritual_ZNK20QLowEnergyDescriptor5valueEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def uuid(self) -> QBluetoothUuid:
    """
    Calls Qt's 'QBluetoothUuid QLowEnergyDescriptor::uuid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergydescriptor.html#uuid

    Returns
    -------

    QBluetoothUuid
      A new cute QBluetoothUuid around the copy Qt gave back. Python owns it.
    """
    #  QBluetoothUuid QLowEnergyDescriptor::uuid() const
    address = self.uglySide.call('ritual_ZNK20QLowEnergyDescriptor4uuidEv')
    return QBluetoothUuid._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QLowEnergyDescriptor::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergydescriptor.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLowEnergyDescriptor::name() const
    return self.uglySide.call('ritual_ZNK20QLowEnergyDescriptor4nameEv')

  def type(self) -> QBluetoothUuid.DescriptorType:
    """
    Calls Qt's 'QBluetoothUuid::DescriptorType QLowEnergyDescriptor::type()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergydescriptor.html#type

    Returns
    -------

    QBluetoothUuid.DescriptorType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QBluetoothUuid.DescriptorType(number)' gives.
    """
    #  QBluetoothUuid::DescriptorType QLowEnergyDescriptor::type() const
    return QBluetoothUuid.DescriptorType(self.uglySide.call(
        'ritual_ZNK20QLowEnergyDescriptor4typeEv',
    ))

  def handle(self) -> int:
    """
    Calls Qt's 'QLowEnergyHandle QLowEnergyDescriptor::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlowenergydescriptor.html#handle
    """
    #  QLowEnergyHandle QLowEnergyDescriptor::handle() const
    return self.uglySide.call('ritual_ZNK20QLowEnergyDescriptor6handleEv')

  def characteristicHandle(self) -> int:
    """
    Calls Qt's 'QLowEnergyHandle QLowEnergyDescriptor::characteristicHandle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptor.html#characteristicHandle
    """
    #  QLowEnergyHandle QLowEnergyDescriptor::characteristicHandle() const
    return self.uglySide.call(
        'ritual_ZNK20QLowEnergyDescriptor20characteristicHandleEv',
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
  def __eq__(self, b: QLowEnergyDescriptor) -> bool:
    """
    Calls Qt's 'bool operator==(const QLowEnergyDescriptor &a, const
    QLowEnergyDescriptor &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptor.html#operator==

    Parameters
    ----------

    b : QLowEnergyDescriptor
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptor, which
      stays Python's own.
    """
    #  bool operator==(const QLowEnergyDescriptor &a, const
    #      QLowEnergyDescriptor &b)
    return Rituals.call(
        'ritual_ZeqRK20QLowEnergyDescriptorS1_',
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
  def __ne__(self, b: QLowEnergyDescriptor) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLowEnergyDescriptor &a, const
    QLowEnergyDescriptor &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptor.html#operator!=

    Parameters
    ----------

    b : QLowEnergyDescriptor
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptor, which
      stays Python's own.
    """
    #  bool operator!=(const QLowEnergyDescriptor &a, const
    #      QLowEnergyDescriptor &b)
    return Rituals.call(
        'ritual_ZneRK20QLowEnergyDescriptorS1_',
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
    'QLowEnergyDescriptor::QLowEnergyDescriptor()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptor.html#QLowEnergyDescriptor
    """
    #  QLowEnergyDescriptor::QLowEnergyDescriptor()
    self._noteCreation(QLowEnergyDescriptor, lambda: Rituals.call(
        'ritual_ZN20QLowEnergyDescriptorC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLowEnergyDescriptor) -> None:
    """
    Notes what was given, for Qt's
    'QLowEnergyDescriptor::QLowEnergyDescriptor(const QLowEnergyDescriptor
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergydescriptor.html#QLowEnergyDescriptor

    Parameters
    ----------

    other : QLowEnergyDescriptor
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptor, which
      stays Python's own.
    """
    #  QLowEnergyDescriptor::QLowEnergyDescriptor(const QLowEnergyDescriptor
    #      &other)
    self._noteCreation(QLowEnergyDescriptor, lambda: Rituals.call(
        'ritual_ZN20QLowEnergyDescriptorC1ERKS_', self._valueOf(other),
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


#  Qt's 'QList<QLowEnergyDescriptor>': the list of QLowEnergyDescriptor,
#  which 'QList[QLowEnergyDescriptor]' gives. It is made here, so that there
#  is one as soon as there can be a QLowEnergyDescriptor.
QList.createKind(
    QLowEnergyDescriptor, 'value',
    make='ritual_list_make_QLowEnergyDescriptor',
    add='ritual_list_add_QLowEnergyDescriptor',
    size='ritual_list_size_QLowEnergyDescriptor',
    at='ritual_list_at_QLowEnergyDescriptor',
    drop='ritual_list_drop_QLowEnergyDescriptor',
)
