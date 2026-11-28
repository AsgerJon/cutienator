"""
QHostAddress binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qhostaddress.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QAbstractSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QIPv6Address
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIPv6Address = WAIT['QIPv6Address']


class QHostAddress(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHostAddress: a plain Python object standing in front
  of one C++ QHostAddress.

  C++ hands a QHostAddress around as a copy, so every C++ QHostAddress behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHostAddress that has a ritual and that Python can
  call so far, 20 names in all: 'setAddress', 'protocol', 'toIPv6Address',
  'toString', 'scopeId', 'setScopeId', 'isEqual', '__eq__', '__ne__',
  'isNull', 'clear', 'isInSubnet', 'isLoopback', 'isGlobal', 'isLinkLocal',
  'isSiteLocal', 'isUniqueLocalUnicast', 'isMulticast', 'isBroadcast',
  'isPrivateUse'. It can be made from Python, in 6 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHostAddress::QHostAddress(const quint8 *ip6Addr)': names 'quint8',
    which has no cute class yet.
  - Qt's 'QHostAddress::QHostAddress(const sockaddr *address)': names
    'sockaddr', which has no cute class yet.
  - Qt's 'QHostAddress::QHostAddress(QHostAddress &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QHostAddress::~QHostAddress()': the destructor: Python removes its
    C++ QHostAddress by it, and has no other use for it.
  - Qt's 'QHostAddress &QHostAddress::operator=(QHostAddress &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QHostAddress &QHostAddress::operator=(const QHostAddress &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QHostAddress &QHostAddress::operator=(SpecialAddress address)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QHostAddress::swap(QHostAddress &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QHostAddress::setAddress(const quint8 *ip6Addr)': names
    'quint8', which has no cute class yet.
  - Qt's 'void QHostAddress::setAddress(const sockaddr *address)': names
    'sockaddr', which has no cute class yet.
  - Qt's 'quint32 QHostAddress::toIPv4Address(bool *ok) const': takes a
    number to change where it is.
  - Qt's 'bool QHostAddress::isInSubnet(const std::pair<QHostAddress, int>
    &subnet) const': takes a type Python has no way to hand over yet.
  - Qt's 'std::pair<QHostAddress, int> QHostAddress::parseSubnet(const
    QString &subnet)': gives a type Python has no way to take yet.
  - Qt's 'bool operator==(QHostAddress::SpecialAddress lhs, const
    QHostAddress &rhs)': takes in Python what 'bool
    QHostAddress::operator==(SpecialAddress address) const' takes.
  - Qt's 'bool operator!=(QHostAddress::SpecialAddress lhs, const
    QHostAddress &rhs)': takes in Python what 'bool
    QHostAddress::operator!=(SpecialAddress address) const' takes.

  What has no ritual
  ------------------

  3 of the 49 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QHostAddress is created at the first use, not by
    'QHostAddress(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHostAddress back gives a copy the ritual made for
    Python, in a new cute QHostAddress.
  - Each name of Qt's QHostAddress that has no cute function yet,
    'parseSubnet', 'swap', 'toIPv4Address', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QHostAddress, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ConversionModeFlag(CuteFlags):
    """
    The flags enum 'QHostAddress::ConversionModeFlag' of Qt, with the 6 names
    Qt gives in it. Qt names the type of its combinations
    'QHostAddress::ConversionMode'.
    """

    ConvertV4MappedToIPv4 = 0x1
    ConvertV4CompatToIPv4 = 0x2
    ConvertUnspecifiedAddress = 0x4
    ConvertLocalHost = 0x8
    TolerantConversion = 0xff
    StrictConversion = 0x0

  ConversionMode = ConversionModeFlag

  class SpecialAddress(CuteNum):
    """
    The enum 'QHostAddress::SpecialAddress' of Qt, with the 7 names Qt gives
    in it.
    """

    Null = Kee[int](0)
    Broadcast = Kee[int](1)
    LocalHost = Kee[int](2)
    LocalHostIPv6 = Kee[int](3)
    Any = Kee[int](4)
    AnyIPv6 = Kee[int](5)
    AnyIPv4 = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHostAddress'

  #  Qt's '~QHostAddress()'. Naming it makes this a value class: Python owns
  #  every C++ QHostAddress behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QHostAddressD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def protocol(self) -> QAbstractSocket.NetworkLayerProtocol:
    """
    Calls Qt's 'NetworkLayerProtocol QHostAddress::protocol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#protocol

    Returns
    -------

    QAbstractSocket.NetworkLayerProtocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.NetworkLayerProtocol(number)' gives.
    """
    #  NetworkLayerProtocol QHostAddress::protocol() const
    return QAbstractSocket.NetworkLayerProtocol(self.uglySide.call(
        'ritual_ZNK12QHostAddress8protocolEv',
    ))

  def toIPv6Address(self) -> QIPv6Address:
    """
    Calls Qt's 'Q_IPV6ADDR QHostAddress::toIPv6Address() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#toIPv6Address

    Returns
    -------

    QIPv6Address
      A new cute QIPv6Address around the copy Qt gave back. Python owns it.
    """
    #  Q_IPV6ADDR QHostAddress::toIPv6Address() const
    address = self.uglySide.call('ritual_ZNK12QHostAddress13toIPv6AddressEv')
    from . import QIPv6Address
    return QIPv6Address._cuteOwning(address)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QHostAddress::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHostAddress::toString() const
    return self.uglySide.call('ritual_ZNK12QHostAddress8toStringEv')

  def scopeId(self) -> str:
    """
    Calls Qt's 'QString QHostAddress::scopeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#scopeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHostAddress::scopeId() const
    return self.uglySide.call('ritual_ZNK12QHostAddress7scopeIdEv')

  @overload(THIS)
  @overload(THIS, ConversionMode)
  def isEqual(
      self,
      address: QHostAddress,
      mode: ConversionMode = ConversionMode.TolerantConversion,
  ) -> bool:
    """
    Calls Qt's 'bool QHostAddress::isEqual(const QHostAddress &address,
    ConversionMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#isEqual

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    mode : ConversionMode
      Passed on as its number. May be left out, as in Qt: it is then
      ConversionMode.TolerantConversion.
    """
    #  bool QHostAddress::isEqual(const QHostAddress &address, ConversionMode
    #      mode) const
    return self.uglySide.call(
        'ritual_ZNK12QHostAddress7isEqualERKS_6QFlagsINS_18ConversionModeFl'
        'agEE',
        self._valueOf(address), mode.value,
    )

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QHostAddress::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#isNull
    """
    #  bool QHostAddress::isNull() const
    return self.uglySide.call('ritual_ZNK12QHostAddress6isNullEv')

  @overload(THIS, int)
  def isInSubnet(self, subnet: QHostAddress, netmask: int) -> bool:
    """
    Calls Qt's 'bool QHostAddress::isInSubnet(const QHostAddress &subnet, int
    netmask) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#isInSubnet

    Parameters
    ----------

    subnet : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    netmask : int
      Passed on as it is.
    """
    #  bool QHostAddress::isInSubnet(const QHostAddress &subnet, int netmask)
    #      const
    return self.uglySide.call(
        'ritual_ZNK12QHostAddress10isInSubnetERKS_i',
        self._valueOf(subnet), netmask,
    )

  def isLoopback(self) -> bool:
    """
    Calls Qt's 'bool QHostAddress::isLoopback() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#isLoopback
    """
    #  bool QHostAddress::isLoopback() const
    return self.uglySide.call('ritual_ZNK12QHostAddress10isLoopbackEv')

  def isGlobal(self) -> bool:
    """
    Calls Qt's 'bool QHostAddress::isGlobal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#isGlobal
    """
    #  bool QHostAddress::isGlobal() const
    return self.uglySide.call('ritual_ZNK12QHostAddress8isGlobalEv')

  def isLinkLocal(self) -> bool:
    """
    Calls Qt's 'bool QHostAddress::isLinkLocal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#isLinkLocal
    """
    #  bool QHostAddress::isLinkLocal() const
    return self.uglySide.call('ritual_ZNK12QHostAddress11isLinkLocalEv')

  def isSiteLocal(self) -> bool:
    """
    Calls Qt's 'bool QHostAddress::isSiteLocal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#isSiteLocal
    """
    #  bool QHostAddress::isSiteLocal() const
    return self.uglySide.call('ritual_ZNK12QHostAddress11isSiteLocalEv')

  def isUniqueLocalUnicast(self) -> bool:
    """
    Calls Qt's 'bool QHostAddress::isUniqueLocalUnicast() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhostaddress.html#isUniqueLocalUnicast
    """
    #  bool QHostAddress::isUniqueLocalUnicast() const
    return self.uglySide.call(
        'ritual_ZNK12QHostAddress20isUniqueLocalUnicastEv',
    )

  def isMulticast(self) -> bool:
    """
    Calls Qt's 'bool QHostAddress::isMulticast() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#isMulticast
    """
    #  bool QHostAddress::isMulticast() const
    return self.uglySide.call('ritual_ZNK12QHostAddress11isMulticastEv')

  def isBroadcast(self) -> bool:
    """
    Calls Qt's 'bool QHostAddress::isBroadcast() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#isBroadcast
    """
    #  bool QHostAddress::isBroadcast() const
    return self.uglySide.call('ritual_ZNK12QHostAddress11isBroadcastEv')

  def isPrivateUse(self) -> bool:
    """
    Calls Qt's 'bool QHostAddress::isPrivateUse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#isPrivateUse
    """
    #  bool QHostAddress::isPrivateUse() const
    return self.uglySide.call('ritual_ZNK12QHostAddress12isPrivateUseEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setAddress(self, ip4Addr: int) -> None:
    """
    Calls Qt's 'void QHostAddress::setAddress(quint32 ip4Addr)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#setAddress

    Parameters
    ----------

    ip4Addr : int
      Passed on as it is.
    """
    #  void QHostAddress::setAddress(quint32 ip4Addr)
    self.uglySide.call('ritual_ZN12QHostAddress10setAddressEj', ip4Addr)

  @overload(QIPv6Address)
  def setAddress(self, ip6Addr: QIPv6Address) -> None:
    """
    Calls Qt's 'void QHostAddress::setAddress(const Q_IPV6ADDR &ip6Addr)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#setAddress

    Parameters
    ----------

    ip6Addr : QIPv6Address
      Passed on as a value: Qt reads the C++ QIPv6Address, which stays
      Python's own.
    """
    #  void QHostAddress::setAddress(const Q_IPV6ADDR &ip6Addr)
    self.uglySide.call(
        'ritual_ZN12QHostAddress10setAddressERK12QIPv6Address',
        self._valueOf(ip6Addr),
    )

  @overload(str)
  def setAddress(self, address: str) -> bool:
    """
    Calls Qt's 'bool QHostAddress::setAddress(const QString &address)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#setAddress

    Parameters
    ----------

    address : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHostAddress::setAddress(const QString &address)
    return self.uglySide.call(
        'ritual_ZN12QHostAddress10setAddressERK7QString', address,
    )

  @overload(SpecialAddress)
  def setAddress(self, address: SpecialAddress) -> None:
    """
    Calls Qt's 'void QHostAddress::setAddress(SpecialAddress address)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#setAddress

    Parameters
    ----------

    address : SpecialAddress
      Passed on as its number.
    """
    #  void QHostAddress::setAddress(SpecialAddress address)
    self.uglySide.call(
        'ritual_ZN12QHostAddress10setAddressENS_14SpecialAddressE',
        address.value,
    )

  @overload(str)
  def setScopeId(self, id: str) -> None:
    """
    Calls Qt's 'void QHostAddress::setScopeId(const QString &id)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#setScopeId

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHostAddress::setScopeId(const QString &id)
    self.uglySide.call('ritual_ZN12QHostAddress10setScopeIdERK7QString', id)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, address: QHostAddress) -> bool:
    """
    Calls Qt's 'bool QHostAddress::operator==(const QHostAddress &address)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#operator==

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  bool QHostAddress::operator==(const QHostAddress &address) const
    return self.uglySide.call(
        'ritual_ZNK12QHostAddresseqERKS_', self._valueOf(address),
    )

  @overload(SpecialAddress)
  def __eq__(self, address: SpecialAddress) -> bool:
    """
    Calls Qt's 'bool QHostAddress::operator==(SpecialAddress address) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#operator==

    Parameters
    ----------

    address : SpecialAddress
      Passed on as its number.
    """
    #  bool QHostAddress::operator==(SpecialAddress address) const
    return self.uglySide.call(
        'ritual_ZNK12QHostAddresseqENS_14SpecialAddressE', address.value,
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
  def __ne__(self, address: QHostAddress) -> bool:
    """
    Calls Qt's 'bool QHostAddress::operator!=(const QHostAddress &address)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#operator!=

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  bool QHostAddress::operator!=(const QHostAddress &address) const
    return self.uglySide.call(
        'ritual_ZNK12QHostAddressneERKS_', self._valueOf(address),
    )

  @overload(SpecialAddress)
  def __ne__(self, address: SpecialAddress) -> bool:
    """
    Calls Qt's 'bool QHostAddress::operator!=(SpecialAddress address) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#operator!=

    Parameters
    ----------

    address : SpecialAddress
      Passed on as its number.
    """
    #  bool QHostAddress::operator!=(SpecialAddress address) const
    return self.uglySide.call(
        'ritual_ZNK12QHostAddressneENS_14SpecialAddressE', address.value,
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
    Notes what was given, for Qt's 'QHostAddress::QHostAddress()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#QHostAddress
    """
    #  QHostAddress::QHostAddress()
    self._noteCreation(QHostAddress, lambda: Rituals.call(
        'ritual_ZN12QHostAddressC1Ev',
    ))

  @overload(int)
  def __init__(self, ip4Addr: int) -> None:
    """
    Notes what was given, for Qt's 'QHostAddress::QHostAddress(quint32
    ip4Addr)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#QHostAddress

    Parameters
    ----------

    ip4Addr : int
      Passed on as it is.
    """
    #  QHostAddress::QHostAddress(quint32 ip4Addr)
    self._noteCreation(QHostAddress, lambda: Rituals.call(
        'ritual_ZN12QHostAddressC1Ej', ip4Addr,
    ))

  @overload(QIPv6Address)
  def __init__(self, ip6Addr: QIPv6Address) -> None:
    """
    Notes what was given, for Qt's 'QHostAddress::QHostAddress(const
    Q_IPV6ADDR &ip6Addr)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#QHostAddress

    Parameters
    ----------

    ip6Addr : QIPv6Address
      Passed on as a value: Qt reads the C++ QIPv6Address, which stays
      Python's own.
    """
    #  QHostAddress::QHostAddress(const Q_IPV6ADDR &ip6Addr)
    self._noteCreation(QHostAddress, lambda: Rituals.call(
        'ritual_ZN12QHostAddressC1ERK12QIPv6Address', self._valueOf(ip6Addr),
    ))

  @overload(str)
  def __init__(self, address: str) -> None:
    """
    Notes what was given, for Qt's 'QHostAddress::QHostAddress(const QString
    &address)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#QHostAddress

    Parameters
    ----------

    address : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QHostAddress::QHostAddress(const QString &address)
    self._noteCreation(QHostAddress, lambda: Rituals.call(
        'ritual_ZN12QHostAddressC1ERK7QString', address,
    ))

  @overload(THIS)
  def __init__(self, copy: QHostAddress) -> None:
    """
    Notes what was given, for Qt's 'QHostAddress::QHostAddress(const
    QHostAddress &copy)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#QHostAddress

    Parameters
    ----------

    copy : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  QHostAddress::QHostAddress(const QHostAddress &copy)
    self._noteCreation(QHostAddress, lambda: Rituals.call(
        'ritual_ZN12QHostAddressC1ERKS_', self._valueOf(copy),
    ))

  @overload(SpecialAddress)
  def __init__(self, address: SpecialAddress) -> None:
    """
    Notes what was given, for Qt's 'QHostAddress::QHostAddress(SpecialAddress
    address)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#QHostAddress

    Parameters
    ----------

    address : SpecialAddress
      Passed on as its number.
    """
    #  QHostAddress::QHostAddress(SpecialAddress address)
    self._noteCreation(QHostAddress, lambda: Rituals.call(
        'ritual_ZN12QHostAddressC1ENS_14SpecialAddressE', address.value,
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QHostAddress::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddress.html#clear
    """
    #  void QHostAddress::clear()
    self.uglySide.call('ritual_ZN12QHostAddress5clearEv')

  @staticmethod
  def parseSubnet(*__, **_) -> Never:
    """
    Qt's 'std::pair<QHostAddress, int> QHostAddress::parseSubnet(const
    QString &subnet)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHostAddress.parseSubnet' has no cute function yet. Qt's "
        "'std::pair<QHostAddress, int> QHostAddress::parseSubnet(const "
        "QString &subnet)': gives a type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHostAddress::swap(QHostAddress &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHostAddress.swap' has no cute function yet. Qt's 'void "
        "QHostAddress::swap(QHostAddress &other)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def toIPv4Address(*__, **_) -> Never:
    """
    Qt's 'quint32 QHostAddress::toIPv4Address(bool *ok) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QHostAddress.toIPv4Address' has no cute function yet. Qt's "
        "'quint32 QHostAddress::toIPv4Address(bool *ok) const': takes a "
        "number to change where it is.")


#  Qt's 'QList<QHostAddress>': the list of QHostAddress, which
#  'QList[QHostAddress]' gives. It is made here, so that there is one as soon
#  as there can be a QHostAddress.
QList.createKind(
    QHostAddress, 'value',
    make='ritual_list_make_QHostAddress',
    add='ritual_list_add_QHostAddress',
    size='ritual_list_size_QHostAddress',
    at='ritual_list_at_QHostAddress',
    drop='ritual_list_drop_QHostAddress',
)
