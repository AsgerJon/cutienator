"""
QNetworkInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkinterface.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QHostAddress, QNetworkAddressEntry


class QNetworkInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkInterface: a plain Python object standing in
  front of one C++ QNetworkInterface.

  C++ hands a QNetworkInterface around as a copy, so every C++
  QNetworkInterface behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNetworkInterface that has a ritual and that Python
  can call so far, 15 names in all: 'isValid', 'index',
  'maximumTransmissionUnit', 'name', 'humanReadableName', 'flags', 'type',
  'hardwareAddress', 'addressEntries', 'interfaceIndexFromName',
  'interfaceFromName', 'interfaceFromIndex', 'interfaceNameFromIndex',
  'allInterfaces', 'allAddresses'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkInterface &QNetworkInterface::operator=(QNetworkInterface
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QNetworkInterface &QNetworkInterface::operator=(const
    QNetworkInterface &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QNetworkInterface::~QNetworkInterface()': the destructor: Python
    removes its C++ QNetworkInterface by it, and has no other use for it.
  - Qt's 'void QNetworkInterface::swap(QNetworkInterface &other)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 24 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QNetworkInterface is created at the first use, not by
    'QNetworkInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkInterface back gives a copy the ritual made
    for Python, in a new cute QNetworkInterface.
  - Each name of Qt's QNetworkInterface that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QNetworkInterface, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class InterfaceFlag(CuteFlags):
    """
    The flags enum 'QNetworkInterface::InterfaceFlag' of Qt, with the 6 names
    Qt gives in it. Qt names the type of its combinations
    'QNetworkInterface::InterfaceFlags'.
    """

    IsUp = 0x1
    IsRunning = 0x2
    CanBroadcast = 0x4
    IsLoopBack = 0x8
    IsPointToPoint = 0x10
    CanMulticast = 0x20

  InterfaceFlags = InterfaceFlag

  class InterfaceType(CuteNum):
    """
    The enum 'QNetworkInterface::InterfaceType' of Qt, with the 15 names Qt
    gives in it.
    """

    Loopback = Kee[int](1)
    Virtual = Kee[int](2)
    Ethernet = Kee[int](3)
    Slip = Kee[int](4)
    CanBus = Kee[int](5)
    Ppp = Kee[int](6)
    Fddi = Kee[int](7)
    Wifi = Kee[int](8)
    Ieee80211 = Kee[int](8)
    Phonet = Kee[int](9)
    Ieee802154 = Kee[int](10)
    SixLoWPAN = Kee[int](11)
    Ieee80216 = Kee[int](12)
    Ieee1394 = Kee[int](13)
    Unknown = Kee[int](0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def interfaceIndexFromName(name: str) -> int:
    """
    Calls Qt's 'int QNetworkInterface::interfaceIndexFromName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterface.html#interfaceIndexFromName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QNetworkInterface::interfaceIndexFromName(const QString &name)
    return Rituals.call(
        'ritual_ZN17QNetworkInterface22interfaceIndexFromNameERK7QString',
        name,
    )

  @staticmethod
  @overload(str)
  def interfaceFromName(name: str) -> QNetworkInterface:
    """
    Calls Qt's 'QNetworkInterface QNetworkInterface::interfaceFromName(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterface.html#interfaceFromName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QNetworkInterface
      A new cute QNetworkInterface around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkInterface QNetworkInterface::interfaceFromName(const QString
    #      &name)
    address = Rituals.call(
        'ritual_ZN17QNetworkInterface17interfaceFromNameERK7QString', name,
    )
    return QNetworkInterface._cuteOwning(address)

  @staticmethod
  @overload(int)
  def interfaceFromIndex(index: int) -> QNetworkInterface:
    """
    Calls Qt's 'QNetworkInterface QNetworkInterface::interfaceFromIndex(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterface.html#interfaceFromIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QNetworkInterface
      A new cute QNetworkInterface around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkInterface QNetworkInterface::interfaceFromIndex(int index)
    address = Rituals.call(
        'ritual_ZN17QNetworkInterface18interfaceFromIndexEi', index,
    )
    return QNetworkInterface._cuteOwning(address)

  @staticmethod
  @overload(int)
  def interfaceNameFromIndex(index: int) -> str:
    """
    Calls Qt's 'QString QNetworkInterface::interfaceNameFromIndex(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterface.html#interfaceNameFromIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkInterface::interfaceNameFromIndex(int index)
    return Rituals.call(
        'ritual_ZN17QNetworkInterface22interfaceNameFromIndexEi', index,
    )

  @staticmethod
  def allInterfaces() -> QList[QNetworkInterface]:
    """
    Calls Qt's 'QList<QNetworkInterface> QNetworkInterface::allInterfaces()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterface.html#allInterfaces

    Returns
    -------

    QList[QNetworkInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QNetworkInterface> QNetworkInterface::allInterfaces()
    address = Rituals.call('ritual_ZN17QNetworkInterface13allInterfacesEv')
    return QList[QNetworkInterface]._cuteOwning(address)

  @staticmethod
  def allAddresses() -> QList[QHostAddress]:
    """
    Calls Qt's 'QList<QHostAddress> QNetworkInterface::allAddresses()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterface.html#allAddresses

    Returns
    -------

    QList[QHostAddress]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHostAddress> QNetworkInterface::allAddresses()
    address = Rituals.call('ritual_ZN17QNetworkInterface12allAddressesEv')
    from . import QHostAddress
    return QList[QHostAddress]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkInterface'

  #  Qt's '~QNetworkInterface()'. Naming it makes this a value class: Python
  #  owns every C++ QNetworkInterface behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QNetworkInterfaceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QNetworkInterface::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkinterface.html#isValid
    """
    #  bool QNetworkInterface::isValid() const
    return self.uglySide.call('ritual_ZNK17QNetworkInterface7isValidEv')

  def index(self) -> int:
    """
    Calls Qt's 'int QNetworkInterface::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkinterface.html#index
    """
    #  int QNetworkInterface::index() const
    return self.uglySide.call('ritual_ZNK17QNetworkInterface5indexEv')

  def maximumTransmissionUnit(self) -> int:
    """
    Calls Qt's 'int QNetworkInterface::maximumTransmissionUnit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterface.html#maximumTransmissionUnit
    """
    #  int QNetworkInterface::maximumTransmissionUnit() const
    return self.uglySide.call(
        'ritual_ZNK17QNetworkInterface23maximumTransmissionUnitEv',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString QNetworkInterface::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkinterface.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkInterface::name() const
    return self.uglySide.call('ritual_ZNK17QNetworkInterface4nameEv')

  def humanReadableName(self) -> str:
    """
    Calls Qt's 'QString QNetworkInterface::humanReadableName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterface.html#humanReadableName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkInterface::humanReadableName() const
    return self.uglySide.call(
        'ritual_ZNK17QNetworkInterface17humanReadableNameEv',
    )

  def flags(self) -> InterfaceFlags:
    """
    Calls Qt's 'InterfaceFlags QNetworkInterface::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkinterface.html#flags

    Returns
    -------

    InterfaceFlags
      The value standing for the combination Qt gave back.
    """
    #  InterfaceFlags QNetworkInterface::flags() const
    return QNetworkInterface.InterfaceFlags(self.uglySide.call(
        'ritual_ZNK17QNetworkInterface5flagsEv',
    ))

  def type(self) -> InterfaceType:
    """
    Calls Qt's 'InterfaceType QNetworkInterface::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkinterface.html#type

    Returns
    -------

    InterfaceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'InterfaceType(number)'
      gives.
    """
    #  InterfaceType QNetworkInterface::type() const
    return QNetworkInterface.InterfaceType(self.uglySide.call(
        'ritual_ZNK17QNetworkInterface4typeEv',
    ))

  def hardwareAddress(self) -> str:
    """
    Calls Qt's 'QString QNetworkInterface::hardwareAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterface.html#hardwareAddress

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkInterface::hardwareAddress() const
    return self.uglySide.call(
        'ritual_ZNK17QNetworkInterface15hardwareAddressEv',
    )

  def addressEntries(self) -> QList[QNetworkAddressEntry]:
    """
    Calls Qt's 'QList<QNetworkAddressEntry>
    QNetworkInterface::addressEntries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterface.html#addressEntries

    Returns
    -------

    QList[QNetworkAddressEntry]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QNetworkAddressEntry> QNetworkInterface::addressEntries() const
    address = self.uglySide.call(
        'ritual_ZNK17QNetworkInterface14addressEntriesEv',
    )
    from . import QNetworkAddressEntry
    return QList[QNetworkAddressEntry]._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QNetworkInterface::QNetworkInterface()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterface.html#QNetworkInterface
    """
    #  QNetworkInterface::QNetworkInterface()
    self._noteCreation(QNetworkInterface, lambda: Rituals.call(
        'ritual_ZN17QNetworkInterfaceC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QNetworkInterface) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkInterface::QNetworkInterface(const QNetworkInterface &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterface.html#QNetworkInterface

    Parameters
    ----------

    other : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  QNetworkInterface::QNetworkInterface(const QNetworkInterface &other)
    self._noteCreation(QNetworkInterface, lambda: Rituals.call(
        'ritual_ZN17QNetworkInterfaceC1ERKS_', self._valueOf(other),
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
    Qt's 'void QNetworkInterface::swap(QNetworkInterface &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkInterface.swap' has no cute function yet. Qt's 'void "
        "QNetworkInterface::swap(QNetworkInterface &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QNetworkInterface>': the list of QNetworkInterface, which
#  'QList[QNetworkInterface]' gives. It is made here, so that there is one as
#  soon as there can be a QNetworkInterface.
QList.createKind(
    QNetworkInterface, 'value',
    make='ritual_list_make_QNetworkInterface',
    add='ritual_list_add_QNetworkInterface',
    size='ritual_list_size_QNetworkInterface',
    at='ritual_list_at_QNetworkInterface',
    drop='ritual_list_drop_QNetworkInterface',
)
