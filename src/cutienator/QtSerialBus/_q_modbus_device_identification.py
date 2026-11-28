"""
QModbusDeviceIdentification binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qmodbusdeviceidentification.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QModbusDeviceIdentification(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QModbusDeviceIdentification: a plain Python object
  standing in front of one C++ QModbusDeviceIdentification.

  C++ hands a QModbusDeviceIdentification around as a copy, so every C++
  QModbusDeviceIdentification behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QModbusDeviceIdentification that has a ritual and
  that Python can call so far, 8 names in all: 'isValid', 'remove',
  'contains', 'insert', 'value', 'conformityLevel', 'setConformityLevel',
  'fromByteArray'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<int> QModbusDeviceIdentification::objectIds() const': gives a
    type Python has no way to take yet.
  - Qt's 'QModbusDeviceIdentification::~QModbusDeviceIdentification()': the
    destructor: Python removes its C++ QModbusDeviceIdentification by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QModbusDeviceIdentification is created at the first use, not by
    'QModbusDeviceIdentification(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QModbusDeviceIdentification back gives a copy the
    ritual made for Python, in a new cute QModbusDeviceIdentification.
  - Each name of Qt's QModbusDeviceIdentification that has no cute function
    yet, 'objectIds', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QModbusDeviceIdentification, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ConformityLevel(CuteNum):
    """
    The enum 'QModbusDeviceIdentification::ConformityLevel' of Qt, with the 6
    names Qt gives in it.
    """

    BasicConformityLevel = Kee[int](1)
    RegularConformityLevel = Kee[int](2)
    ExtendedConformityLevel = Kee[int](3)
    BasicIndividualConformityLevel = Kee[int](129)
    RegularIndividualConformityLevel = Kee[int](130)
    ExtendedIndividualConformityLevel = Kee[int](131)

  class ObjectId(CuteNum):
    """
    The enum 'QModbusDeviceIdentification::ObjectId' of Qt, with the 10 names
    Qt gives in it.
    """

    VendorNameObjectId = Kee[int](0)
    ProductCodeObjectId = Kee[int](1)
    MajorMinorRevisionObjectId = Kee[int](2)
    VendorUrlObjectId = Kee[int](3)
    ProductNameObjectId = Kee[int](4)
    ModelNameObjectId = Kee[int](5)
    UserApplicationNameObjectId = Kee[int](6)
    ReservedObjectId = Kee[int](7)
    ProductDependentObjectId = Kee[int](128)
    UndefinedObjectId = Kee[int](256)

  class ReadDeviceIdCode(CuteNum):
    """
    The enum 'QModbusDeviceIdentification::ReadDeviceIdCode' of Qt, with the
    4 names Qt gives in it.
    """

    BasicReadDeviceIdCode = Kee[int](1)
    RegularReadDeviceIdCode = Kee[int](2)
    ExtendedReadDeviceIdCode = Kee[int](3)
    IndividualReadDeviceIdCode = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray)
  def fromByteArray(ba: QByteArray) -> QModbusDeviceIdentification:
    """
    Calls Qt's 'QModbusDeviceIdentification
    QModbusDeviceIdentification::fromByteArray(const QByteArray &ba)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdeviceidentification.html#fromByteArray

    Parameters
    ----------

    ba : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QModbusDeviceIdentification
      A new cute QModbusDeviceIdentification around the copy Qt gave back.
      Python owns it.
    """
    #  QModbusDeviceIdentification
    #      QModbusDeviceIdentification::fromByteArray(const QByteArray &ba)
    address = Rituals.call(
        'ritual_ZN27QModbusDeviceIdentification13fromByteArrayERK10QByteArr'
        'ay',
        CuteMixin._valueOf(ba),
    )
    return QModbusDeviceIdentification._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusDeviceIdentification'

  #  Qt's '~QModbusDeviceIdentification()'. Naming it makes this a value
  #  class: Python owns every C++ QModbusDeviceIdentification behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QModbusDeviceIdentificationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QModbusDeviceIdentification::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdeviceidentification.html#isValid
    """
    #  bool QModbusDeviceIdentification::isValid() const
    return self.uglySide.call(
        'ritual_ZNK27QModbusDeviceIdentification7isValidEv',
    )

  @overload(int)
  def contains(self, objectId: int) -> bool:
    """
    Calls Qt's 'bool QModbusDeviceIdentification::contains(uint objectId)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdeviceidentification.html#contains

    Parameters
    ----------

    objectId : int
      Passed on as it is.
    """
    #  bool QModbusDeviceIdentification::contains(uint objectId) const
    return self.uglySide.call(
        'ritual_ZNK27QModbusDeviceIdentification8containsEj', objectId,
    )

  @overload(int)
  def value(self, objectId: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QModbusDeviceIdentification::value(uint objectId)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdeviceidentification.html#value

    Parameters
    ----------

    objectId : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QModbusDeviceIdentification::value(uint objectId) const
    address = self.uglySide.call(
        'ritual_ZNK27QModbusDeviceIdentification5valueEj', objectId,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def conformityLevel(self) -> ConformityLevel:
    """
    Calls Qt's 'ConformityLevel
    QModbusDeviceIdentification::conformityLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdeviceidentification.html#conformityLevel

    Returns
    -------

    ConformityLevel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ConformityLevel(number)'
      gives.
    """
    #  ConformityLevel QModbusDeviceIdentification::conformityLevel() const
    return QModbusDeviceIdentification.ConformityLevel(self.uglySide.call(
        'ritual_ZNK27QModbusDeviceIdentification15conformityLevelEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ConformityLevel)
  def setConformityLevel(self, level: ConformityLevel) -> None:
    """
    Calls Qt's 'void
    QModbusDeviceIdentification::setConformityLevel(ConformityLevel level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdeviceidentification.html

    Parameters
    ----------

    level : ConformityLevel
      Passed on as its number.
    """
    #  void QModbusDeviceIdentification::setConformityLevel(ConformityLevel
    #      level)
    self.uglySide.call(
        'ritual_ZN27QModbusDeviceIdentification18setConformityLevelENS_15Co'
        'nformityLevelE',
        level.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QModbusDeviceIdentification::QModbusDeviceIdentification()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdeviceidentification.html
    """
    #  QModbusDeviceIdentification::QModbusDeviceIdentification()
    self._noteCreation(QModbusDeviceIdentification, lambda: Rituals.call(
        'ritual_ZN27QModbusDeviceIdentificationC1Ev',
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

  @overload(int)
  def remove(self, objectId: int) -> None:
    """
    Calls Qt's 'void QModbusDeviceIdentification::remove(uint objectId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdeviceidentification.html#remove

    Parameters
    ----------

    objectId : int
      Passed on as it is.
    """
    #  void QModbusDeviceIdentification::remove(uint objectId)
    self.uglySide.call(
        'ritual_ZN27QModbusDeviceIdentification6removeEj', objectId,
    )

  @overload(int, QByteArray)
  def insert(self, objectId: int, data: QByteArray) -> bool:
    """
    Calls Qt's 'bool QModbusDeviceIdentification::insert(uint objectId, const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdeviceidentification.html#insert

    Parameters
    ----------

    objectId : int
      Passed on as it is.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QModbusDeviceIdentification::insert(uint objectId, const
    #      QByteArray &data)
    return self.uglySide.call(
        'ritual_ZN27QModbusDeviceIdentification6insertEjRK10QByteArray',
        objectId, self._valueOf(data),
    )

  @staticmethod
  def objectIds(*__, **_) -> Never:
    """
    Qt's 'QList<int> QModbusDeviceIdentification::objectIds() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QModbusDeviceIdentification.objectIds' has no cute function yet. "
        "Qt's 'QList<int> QModbusDeviceIdentification::objectIds() const': "
        "gives a type Python has no way to take yet.")
